import os
import sys
import csv
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import configs.evaluation_config as cfg
from experiments.evaluation_utils import evaluate_policy
from experiments.statistical_analysis import aggregate_and_plot

from env.target_capture_env import TargetCaptureEnv
from env.rewards import RewardCalculator

from agents.random_agent import RandomAgent
from agents.heuristic_agent import HeuristicAgent
from agents.q_learning_agent import QLearningAgent
from algorithms.cooperative_q_learning import SharedQTable
from agents.shared_q_agent import SharedQAgent

def save_raw_results(results, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if not results:
        return
    keys = results[0].keys()
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

def save_experiment_metadata():
    os.makedirs(cfg.SUMMARIES_DIR, exist_ok=True)
    metadata = {
        "GRID_SIZE": cfg.GRID_SIZE,
        "MAX_STEPS": cfg.MAX_STEPS,
        "TRAIN_EPISODES": cfg.TRAIN_EPISODES,
        "EVAL_EPISODES": cfg.EVAL_EPISODES,
        "SEEDS": cfg.SEEDS
    }
    with open(os.path.join(cfg.SUMMARIES_DIR, "experiment_config.json"), 'w') as f:
        json.dump(metadata, f, indent=4)

def train_independent_q(seed: int):
    """Trains an Independent Q-Learning setup for the given seed."""
    env = TargetCaptureEnv(grid_size=cfg.GRID_SIZE, max_steps=cfg.MAX_STEPS)
    reward_calc = RewardCalculator()
    
    agent0 = QLearningAgent()
    agent1 = QLearningAgent()
    
    for ep in range(cfg.TRAIN_EPISODES):
        state = env.reset(seed=seed + ep * 1000) # Ensure diverse starting states
        done = False
        while not done:
            obs0 = {"agent_position": state["agent_0"], "target_position": state["target"]}
            obs1 = {"agent_position": state["agent_1"], "target_position": state["target"]}
            
            a0 = agent0.select_action(obs0)
            a1 = agent1.select_action(obs1)
            
            next_state, info = env.step({"agent_0": a0, "agent_1": a1})
            rewards = reward_calc.calculate(
                agents=[env.agent_0, env.agent_1],
                target=env.target,
                previous_positions=state,
                captured=info.get("captured", False)
            )
            step_reward = rewards["total_reward"]
            
            next_obs0 = {"agent_position": next_state["agent_0"], "target_position": next_state["target"]}
            next_obs1 = {"agent_position": next_state["agent_1"], "target_position": next_state["target"]}
            
            agent0.update(obs0, a0, step_reward, next_obs0)
            agent1.update(obs1, a1, step_reward, next_obs1)
            
            state = next_state
            if info.get("terminated", False) or info.get("truncated", False):
                done = True
                
        agent0.decay_epsilon()
        agent1.decay_epsilon()
        
    # Save checkpoint
    path0 = os.path.join(cfg.CHECKPOINTS_DIR, "independent_q", f"seed_{seed}_agent0.pkl")
    path1 = os.path.join(cfg.CHECKPOINTS_DIR, "independent_q", f"seed_{seed}_agent1.pkl")
    os.makedirs(os.path.dirname(path0), exist_ok=True)
    agent0.save(path0)
    agent1.save(path1)
    return agent0, agent1

def train_cooperative_q(seed: int):
    """Trains a Shared-Policy Cooperative Q-Learning setup for the given seed."""
    env = TargetCaptureEnv(grid_size=cfg.GRID_SIZE, max_steps=cfg.MAX_STEPS)
    reward_calc = RewardCalculator()
    
    shared_table = SharedQTable()
    agent0 = SharedQAgent(shared_table, "agent_0", "agent_1", seed=seed)
    agent1 = SharedQAgent(shared_table, "agent_1", "agent_0", seed=seed+1)
    
    for ep in range(cfg.TRAIN_EPISODES):
        state = env.reset(seed=seed + ep * 1000)
        done = False
        while not done:
            a0 = agent0.select_action(state)
            a1 = agent1.select_action(state)
            
            next_state, info = env.step({"agent_0": a0, "agent_1": a1})
            rewards = reward_calc.calculate(
                agents=[env.agent_0, env.agent_1],
                target=env.target,
                previous_positions=state,
                captured=info.get("captured", False)
            )
            step_reward = rewards["total_reward"]
            is_term = info.get("terminated", False)
            
            agent0.update(state, a0, step_reward, next_state, is_term)
            agent1.update(state, a1, step_reward, next_state, is_term)
            
            state = next_state
            if info.get("terminated", False) or info.get("truncated", False):
                done = True
                
        agent0.decay_epsilon()
        agent1.decay_epsilon()
        
    path = os.path.join(cfg.CHECKPOINTS_DIR, "cooperative_q", f"seed_{seed}.pkl")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    shared_table.save(path)
    return agent0, agent1

def main():
    print("--- Starting Phase 11 Experimental Evaluation ---")
    save_experiment_metadata()
    
    # Random Baseline
    print("Evaluating Random Baseline...")
    random_results = []
    for seed in cfg.SEEDS:
        a0 = RandomAgent(seed=seed)
        a1 = RandomAgent(seed=seed+1)
        res = evaluate_policy(a0, a1, "Random", seed, cfg.EVAL_EPISODES, cfg.GRID_SIZE, cfg.MAX_STEPS)
        random_results.extend(res)
    save_raw_results(random_results, os.path.join(cfg.RAW_RESULTS_DIR, "random_results.csv"))
    
    # Heuristic Baseline
    print("Evaluating Heuristic Baseline...")
    heuristic_results = []
    for seed in cfg.SEEDS:
        a0 = HeuristicAgent()
        a1 = HeuristicAgent()
        res = evaluate_policy(a0, a1, "Heuristic", seed, cfg.EVAL_EPISODES, cfg.GRID_SIZE, cfg.MAX_STEPS)
        heuristic_results.extend(res)
    save_raw_results(heuristic_results, os.path.join(cfg.RAW_RESULTS_DIR, "heuristic_results.csv"))
    
    # Independent Q-Learning
    print("Training and Evaluating Independent Q-Learning...")
    indep_q_results = []
    for seed in cfg.SEEDS:
        print(f"  Seed {seed}...")
        a0, a1 = train_independent_q(seed)
        res = evaluate_policy(a0, a1, "Independent Q-Learning", seed, cfg.EVAL_EPISODES, cfg.GRID_SIZE, cfg.MAX_STEPS)
        indep_q_results.extend(res)
    save_raw_results(indep_q_results, os.path.join(cfg.RAW_RESULTS_DIR, "independent_q_results.csv"))
    
    # Cooperative Q-Learning
    print("Training and Evaluating Cooperative Q-Learning...")
    coop_q_results = []
    for seed in cfg.SEEDS:
        print(f"  Seed {seed}...")
        a0, a1 = train_cooperative_q(seed)
        res = evaluate_policy(a0, a1, "Cooperative Q-Learning", seed, cfg.EVAL_EPISODES, cfg.GRID_SIZE, cfg.MAX_STEPS)
        coop_q_results.extend(res)
    save_raw_results(coop_q_results, os.path.join(cfg.RAW_RESULTS_DIR, "cooperative_q_results.csv"))

    print("\nAll experiments complete. Running statistical analysis...")
    aggregate_and_plot()
    print("Analysis complete! See results/summaries/ and results/plots/")

if __name__ == "__main__":
    main()
