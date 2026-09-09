from typing import List, Dict, Any, Callable
from env.target_capture_env import TargetCaptureEnv
from env.rewards import RewardCalculator

def evaluate_policy(
    agent0, 
    agent1, 
    method_name: str, 
    training_seed: int, 
    eval_episodes: int, 
    grid_size: int, 
    max_steps: int
) -> List[Dict[str, Any]]:
    """
    Evaluates a pair of agents consistently without updating their policies.
    Returns a list of dictionaries, where each dictionary represents one episode's raw results.
    """
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
        
    results = []
    
    for ep in range(eval_episodes):
        # Deterministic but separate seed formula for evaluation
        eval_seed = 1000 + training_seed * 100 + ep
        state = env.reset(seed=eval_seed)
        
        done = False
        episode_reward = 0.0
        
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
            
            # Agents act
            a0 = agent0.select_action(obs0)
            a1 = agent1.select_action(obs1)
            
            # Step env
            next_state, info = env.step({"agent_0": a0, "agent_1": a1})
            
            # Reward
            rewards = reward_calc.calculate(
                agents=[env.agent_0, env.agent_1],
                target=env.target,
                previous_positions=state,
                captured=info.get("captured", False)
            )
            episode_reward += rewards["total_reward"]
            
            state = next_state
            if info.get("terminated", False) or info.get("truncated", False):
                done = True
                
        # Record results
        captured = int(info.get("captured", False))
        ep_len = info.get("step", env.current_step)
        
        results.append({
            "method": method_name,
            "training_seed": training_seed,
            "evaluation_seed": eval_seed,
            "episode": ep,
            "captured": captured,
            "episode_length": ep_len,
            "episode_reward": episode_reward,
            "capture_time": ep_len if captured else None
        })
        
    # Restore exploration
    if old_eps0 is not None:
        agent0.epsilon = old_eps0
    if old_eps1 is not None:
        agent1.epsilon = old_eps1
        
    return results
