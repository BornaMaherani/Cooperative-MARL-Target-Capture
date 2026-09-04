import sys
import os

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from env import TargetCaptureEnv, Action, RewardCalculator
from env.target_policy import TargetPolicy

class StayPolicy(TargetPolicy):
    def choose_action(self, target, grid):
        return Action.STAY

def run_integration_test():
    print("Initializing Environment and Reward Calculator...")
    env = TargetCaptureEnv(grid_size=10, max_steps=10)
    reward_calc = RewardCalculator()
    
    # Reset
    prev_state = env.reset()
    
    # Force positions for a guaranteed capture scenario
    env.target.position = type(env.target.position)(5, 5)
    env.agent_0.position = type(env.agent_0.position)(5, 3)
    env.agent_1.position = type(env.agent_1.position)(5, 7)
    
    # Mock target policy so it doesn't run away for this demo
    env.target_policy = StayPolicy()
    
    print("\n--- Initial State ---")
    env.render()
    
    # Agents move to capture (distance 1)
    actions = {
        "agent_0": Action.UP,
        "agent_1": Action.DOWN
    }
    
    print(f"Applying Actions: {actions}\n")
    
    # Step the environment
    curr_state, info = env.step(actions)
    
    print("--- State After Actions ---")
    env.render()
    
    print("Environment Info Dictionary:")
    for k, v in info.items():
        print(f"  {k}: {v}")
        
    # Calculate rewards using the new Phase 7 module
    rewards = reward_calc.calculate(
        agents=[env.agent_0, env.agent_1],
        target=env.target,
        previous_positions=prev_state,
        captured=info["captured"]
    )
    
    print("\nCalculated Rewards:")
    for k, v in rewards.items():
        print(f"  {k}: {v}")
        
    print("\nIntegration Test Completed Successfully!")

if __name__ == "__main__":
    run_integration_test()
