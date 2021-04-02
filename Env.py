import gym
from gym import spaces
import numpy as np

class CarDrivingEnvironment(gym.Env):
  """Environment for a self driving race car"""
  metadata = {'render.modes': ['human']}

  def __init__(self):
    super(CarDrivingEnv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects
    # 3 actions for the car:
    # Gas, Brake, Steer (left/right)
    self.action_space = spaces.Box(low = np.array([-1,0,0]), high = np.array([+1,+1,+1]))
    # Prices contains the OHCL values for the last five prices
    self.observation_space = spaces.Box(
      low=0, high=1, shape=(6, 6), dtype=np.float16)

  def step(self, action):
    # Execute one time step within the environment
    return
  def reset(self):
    # Reset the state of the environment to an initial state
    
    return
  def render(self, mode='human', close=False):
    # Render the environment to the screen
    return