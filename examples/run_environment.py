import random
import sys
import os

# Ensure the root directory is in the path to import env
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from env import TargetCaptureEnv, Action

def main():
    env = TargetCaptureEnv(grid_size=10, max_steps=50)
    
    print("Initializing Environment...")
    env.reset(seed=123)
    
    actions_list = list(Action)
    
    # Run 50 random actions
    for _ in range(50):
        env.render()
        
        actions = {
            "agent_0": random.choice(actions_list),
            "agent_1": random.choice(actions_list)
        }
        
        env.step(actions)

if __name__ == "__main__":
    main()
