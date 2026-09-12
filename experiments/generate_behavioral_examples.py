import os
import sys
import csv
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import configs.evaluation_config as cfg
from env.target_capture_env import TargetCaptureEnv
from env.rewards import RewardCalculator

from agents.random_agent import RandomAgent
from agents.heuristic_agent import HeuristicAgent
from agents.q_learning_agent import QLearningAgent
from algorithms.cooperative_q_learning import SharedQTable
from agents.shared_q_agent import SharedQAgent

from analysis.trajectory_analysis import TrajectoryRecorder
from analysis.behavioral_metrics import calculate_all_behavioral_metrics
from visualization.renderer import GridWorldRenderer
from visualization.gif_generator import GIFGenerator

def evaluate_with_recorder(
    agent0, 
    agent1, 
    method_name: str, 
    training_seed: int, 
    eval_episodes: int, 
    grid_size: int, 
    max_steps: int
) -> list:
    """Evaluates the agents and returns a list of TrajectoryRecorder objects."""
    env = TargetCaptureEnv(grid_size=grid_size, max_steps=max_steps)
    reward_calc = RewardCalculator()
    
    # Store original epsilons
    old_eps0 = getattr(agent0, "epsilon", None)
    old_eps1 = getattr(agent1, "epsilon", None)
    
    # Disable exploration
    if hasattr(agent0, "epsilon"):
        agent0.epsilon = 0.0
    if hasattr(agent1, "epsilon"):
        agent1.epsilon = 0.0
        
    recorders = []
    
    for ep in range(eval_episodes):
        recorder = TrajectoryRecorder()
        eval_seed = 1000 + training_seed * 100 + ep
        recorder.set_metadata(method_name, training_seed, eval_seed, grid_size, max_steps)
        
        state = env.reset(seed=eval_seed)
        done = False
        
        # Record step 0 initial positions before actions
        recorder.record_step(env.current_step, state, {"agent_0": "START", "agent_1": "START"}, {"target_action": "START"}, 0.0)
        
        while not done:
            obs0 = {
                "agent_position": state["agent_0"], 
                "target_position": state["target"],
                "agent_0": state["agent_0"], 
                "agent_1": state["agent_1"], 
                "target": state["target"]
            }
            obs1 = {
                "agent_position": state["agent_1"], 
                "target_position": state["target"],
                "agent_0": state["agent_0"], 
                "agent_1": state["agent_1"], 
                "target": state["target"]
            }
            
            a0 = agent0.select_action(obs0)
            a1 = agent1.select_action(obs1)
            
            next_state, info = env.step({"agent_0": a0, "agent_1": a1})
            
            rewards = reward_calc.calculate(
                agents=[env.agent_0, env.agent_1],
                target=env.target,
                previous_positions=state,
                captured=info.get("captured", False)
            )
            
            recorder.record_step(
                step=env.current_step,
                state=next_state,
                actions={"agent_0": a0, "agent_1": a1},
                info=info,
                reward=rewards["total_reward"]
            )
            
            state = next_state
            if info.get("terminated", False) or info.get("truncated", False):
                done = True
                
        recorders.append(recorder)
        
    # Restore exploration
    if old_eps0 is not None:
        agent0.epsilon = old_eps0
    if old_eps1 is not None:
        agent1.epsilon = old_eps1
        
    return recorders

def load_independent_q(seed: int):
    path0 = os.path.join(cfg.CHECKPOINTS_DIR, "independent_q", f"seed_{seed}_agent0.pkl")
    path1 = os.path.join(cfg.CHECKPOINTS_DIR, "independent_q", f"seed_{seed}_agent1.pkl")
    a0 = QLearningAgent()
    a0.load(path0)
    a1 = QLearningAgent()
    a1.load(path1)
    return a0, a1

def load_cooperative_q(seed: int):
    path = os.path.join(cfg.CHECKPOINTS_DIR, "cooperative_q", f"seed_{seed}.pkl")
    shared_table = SharedQTable()
    shared_table.load(path)
    a0 = SharedQAgent(shared_table, "agent_0", "agent_1", seed=seed)
    a1 = SharedQAgent(shared_table, "agent_1", "agent_0", seed=seed+1)
    return a0, a1

def find_representative_episodes(recorders: list):
    """Finds a success episode with length closest to median, and one failure episode."""
    successes = [r for r in recorders if r.trajectory[-1]["captured"]]
    failures = [r for r in recorders if not r.trajectory[-1]["captured"]]
    
    rep_success = None
    if successes:
        successes.sort(key=lambda r: len(r.trajectory))
        median_idx = len(successes) // 2
        rep_success = successes[median_idx]
        
    rep_failure = failures[0] if failures else None
    
    return rep_success, rep_failure

def main():
    print("--- Starting Phase 12 Behavioral Generation ---")
    
    EVAL_EPISODES = 100
    SEED = cfg.SEEDS[0] # Just use the first seed for representative behavior
    
    methods = [
        ("Random", lambda: (RandomAgent(seed=SEED), RandomAgent(seed=SEED+1))),
        ("Heuristic", lambda: (HeuristicAgent(), HeuristicAgent())),
        ("Independent Q-Learning", lambda: load_independent_q(SEED)),
        ("Cooperative Q-Learning", lambda: load_cooperative_q(SEED))
    ]
    
    all_metrics = []
    renderer = GridWorldRenderer(grid_size=cfg.GRID_SIZE)
    gif_gen = GIFGenerator(grid_size=cfg.GRID_SIZE)
    
    for name, agent_loader in methods:
        print(f"Processing {name}...")
        a0, a1 = agent_loader()
        
        # 1. Record trajectories
        recorders = evaluate_with_recorder(a0, a1, name, SEED, EVAL_EPISODES, cfg.GRID_SIZE, cfg.MAX_STEPS)
        
        # 2. Compute behavioral metrics
        for i, recorder in enumerate(recorders):
            mets = calculate_all_behavioral_metrics(recorder.trajectory)
            mets["method"] = name
            mets["seed"] = SEED
            mets["episode"] = i
            mets["captured"] = int(recorder.trajectory[-1]["captured"])
            mets["episode_length"] = len(recorder.trajectory)
            all_metrics.append(mets)
            
        # 3. Find representative episodes
        rep_success, rep_fail = find_representative_episodes(recorders)
        
        safe_name = name.lower().replace(" ", "_").replace("-", "_")
        
        if rep_success:
            rep_success.save(f"results/trajectories/{safe_name}_success.json")
            renderer.plot_static_trajectory(rep_success.trajectory, f"{name} Success", f"results/behavioral/{safe_name}_trajectory.png")
            gif_gen.generate(rep_success.trajectory, f"{name}", f"results/gifs/{safe_name}_success.gif")
            
        if rep_fail:
            rep_fail.save(f"results/trajectories/{safe_name}_failure.json")
            gif_gen.generate(rep_fail.trajectory, f"{name} (Failure)", f"results/gifs/{safe_name}_failure.gif")

    # 4. Save metrics to CSV
    os.makedirs("results/behavioral", exist_ok=True)
    if all_metrics:
        keys = ["method", "seed", "episode", "captured", "episode_length", 
                "mean_target_distance", "mean_hunter_separation", 
                "simultaneous_adjacency_fraction", "distinct_side_fraction"]
        with open("results/behavioral/behavioral_metrics.csv", 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(all_metrics)
            
        # Create summary
        summary = []
        import statistics
        from collections import defaultdict
        grouped = defaultdict(list)
        for m in all_metrics:
            grouped[m["method"]].append(m)
            
        for method, metrics_list in grouped.items():
            def mean_std(key):
                vals = [m[key] for m in metrics_list]
                return f"{statistics.mean(vals):.2f} ± {statistics.stdev(vals):.2f}" if len(vals)>1 else f"{statistics.mean(vals):.2f} ± 0.00"
            
            summary.append({
                "method": method,
                "capture_rate": f"{sum(m['captured'] for m in metrics_list) / len(metrics_list):.2f}",
                "episode_length": mean_std("episode_length"),
                "mean_target_distance": mean_std("mean_target_distance"),
                "mean_hunter_separation": mean_std("mean_hunter_separation"),
                "simultaneous_adjacency": mean_std("simultaneous_adjacency_fraction"),
                "distinct_side_positioning": mean_std("distinct_side_fraction")
            })
            
        with open("results/behavioral/behavioral_summary.csv", 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=summary[0].keys())
            writer.writeheader()
            writer.writerows(summary)
            
    print("Phase 12 Generation Complete!")

if __name__ == "__main__":
    main()
