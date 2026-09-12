import os
import pytest
from visualization.renderer import GridWorldRenderer
from visualization.gif_generator import GIFGenerator

def test_visualization_smoke_test(tmp_path):
    """Test 8: Verify renderer does not crash."""
    renderer = GridWorldRenderer(grid_size=5)
    gif_gen = GIFGenerator(grid_size=5)
    trajectory = [
        {
            "step": 0,
            "agent_0_position": [0, 0],
            "agent_1_position": [1, 0],
            "target_position": [2, 2],
            "captured": False,
            "reward": 0.0
        },
        {
            "step": 1,
            "agent_0_position": [1, 0],
            "agent_1_position": [2, 0],
            "target_position": [2, 1],
            "captured": True,
            "reward": 10.0
        }
    ]
    
    png_path = tmp_path / "test.png"
    gif_path = tmp_path / "test.gif"
    
    # Should not crash
    renderer.plot_static_trajectory(trajectory, "Test", str(png_path))
    assert os.path.exists(png_path)
    
    # Rendering GIF might fail if imagemagick/pillow isn't setup right, but pillow writer is built-in
    gif_gen.generate(trajectory, "Test GIF", str(gif_path))
    assert os.path.exists(gif_path)
