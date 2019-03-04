import numpy as np
# Option 1.1 channel_state: number of users
# Option 1.2 channel_state: interference power
class Environment(object):

    def __init__(self, channel_num):
        """channel_num: number of RF channels in the environment"""
        self.channel_state = np.zeros(channel_num)

    def join(self, channel_index):
        self.channel_state[channel_index] += 1

    def leave(self, channel_index):
        self.channel_state[channel_index] -= 1

    def report(self):
        return self.channel_state

    def get_reward(self):
        # TODO Give success (1/task), conflict(-1/task)

class Agent(object):

    def __init__(self, task_num, channel_num):
        """task_num: number of task to be transmitted"""
        self.task_num = task_num
        self.channels = np.zeros(channel_num)
        self.part_state = []
        self.reward = 0

    def one_time_step(self, env):
        if self.task_num <= 0:
            # TODO Calculate the final reward
            self.reward += env.get_reward()
        # Since we want to finish tasks as soon as possible
        # TODO choose operations (transmit, expand, shrink, 
        # observe, communicate) based on part_state
        self.reward -= 1

    def transmit(self):
        self.task_num -= sum(self.channels)

    def expand(self, env, channel_index):
        """channel_index: the index of channel to occupy"""
        if self.channels[channel_index] == 0:
            self.channels[channel_index] = 1
            env.join(channel_index)
            # Since expand operation need bandwidth to coordinate
            self.reward -= 1
        transmit()

    def shrink(self, env, channel_index):
        """channel_index: the index of channel to release"""
        if self.channels[channel_index] == 1:
            self.channels[channel_index] = 0
            env.leave(channel_index)
            # Since shrink  operation need bandwidth to coordinate
            self.reward -= 1
        transmit()

    def observe(self, env)
        obs = env.report()
        self.part_state.append(obs-self.channels) 
        # Since observe operation need energy to detect
        self.reward -= 1

    def communicate(self):        
        # Since communicate operation need bandwidth to coordinate two group
        # TODO How to communicate efficiently, since the cost is high
        self.reward -= 2
    
    def report(self):
        return self.task_num, self.channels

    def reward(self, env):
        # TODO Try to get back reward from environment (receiver)
