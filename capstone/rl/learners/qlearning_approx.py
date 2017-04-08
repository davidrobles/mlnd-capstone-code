import numpy as np
import random
from collections import deque
from ..learner import Learner
from ..utils import max_qvalue, min_qvalue


class ApproximateQLearning(Learner):
    '''Q-learning with a function approximator'''

    def __init__(self, env, policy, qfunction, discount_factor=1.0, selfplay=False,
                 experience_replay=True, batch_size=32, replay_memory_size=10000):
        super(ApproximateQLearning, self).__init__(env)
        self.policy = policy
        self.qfunction = qfunction
        self.discount_factor = discount_factor
        self.selfplay = selfplay
        self.experience_replay = experience_replay
        self.batch_size = batch_size
        self.replay_memory_size = replay_memory_size
        if self.experience_replay:
            self.replay_memory = deque(maxlen=self.replay_memory_size)

    def best_qvalue(self, state):
        func = None
        if self.selfplay:
            func = np.max if state.cur_player() == 0 else np.min
        else:
            func = np.max
        return self.qfunction.best_value(state, self.env.actions(state), func)

    ###########
    # Learner #
    ###########

    def episode(self):
        while not self.env.is_terminal():
            state = self.env.cur_state()
            action = self.policy.action(state)
            reward, next_state = self.env.do_action(action)
            if self.experience_replay:
                experience = (state, action, reward, next_state)
                self.replay_memory.append(experience)
                batch_size = min(len(self.replay_memory), self.batch_size)
                experiences = random.sample(self.replay_memory, batch_size)
                updates = []
                for experience in experiences:
                    ss, aa, rr, ns = experience
                    if ns.is_over():
                        update = rr
                    else:
                        best_qvalue = self.best_qvalue(ns)
                        update = rr + (self.discount_factor * best_qvalue)
                    updates.append(update)
                self.qfunction.minibatch_update(experiences, updates)
            else:
                best_qvalue = self.best_qvalue(next_state)
                update = reward + (self.discount_factor * best_qvalue)
                self.qfunction.update(state, action, update)
