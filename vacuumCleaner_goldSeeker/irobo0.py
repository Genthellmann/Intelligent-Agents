import random
from typing import List


class Agent:
    def __init__(self):
        self.cost = [0.0, 1.0, 1.0, 2.0]
        self.reward = 10
        self.tc = 0.0
        self.actions = [0, 1, 2, 3]

    @staticmethod
    def observe(observation) -> List[int]:
        pos = ["left", "right"]
        cell = ["clean", "dirty"]
        print("Percept.  Pos:", pos[observation[0]],
              "Cell:", cell[observation[1]])
        return observation

    def compute_costs(self, action, observation) -> float:
        self.tc -= self.cost[action]
        if (observation[1] == 1) and (action == 3):
            self.tc += self.reward
        return self.tc

    def get_costs(self):
        return self.tc

    def show_costs(self):
        print("Total profit:", self.tc)

    @staticmethod
    def show_action(a: int):
        actions = ["pass", "left", "right", "suck"]
        print("Cmd:", actions[a])

    def act(self, observation: List[int]) -> int:
        action = random.choice(self.actions)
        self.compute_costs(action, observation)
        return action


class OptAgent(Agent):

    def act(self, observation: List[int]) -> int:
        action = 0
        if (observation[0] == 0) and (observation[1] == 1):
            action = 3
        if (observation[0] == 0) and (observation[1] == 0):
            action = 2
        if (observation[0] == 1) and (observation[1] == 1):
            action = 3
        if (observation[0] == 1) and (observation[1] == 0):
            action = 1
        self.compute_costs(action, observation)
        return action


class HumanAgent(Agent):

    def act(self, observation: List[int]) -> int:
        action = 7
        while action not in [0, 1, 2, 3]:
            print("Enter action (0=pass, 1=left, 2=right, 3=suck):")
            action = int(input())
        self.compute_costs(action, observation)
        return action
