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
    # gas from -1 to 1, brake 0 to 1, steer -1 to 1
    self.action_space = spaces.Box(low = np.array([-1,0,-1]), high = np.array([+1,+1,+1]))
    # Observations are 4 blocks of the track (current + 3), speed, position(x,y), direction (angle)
    #todo
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