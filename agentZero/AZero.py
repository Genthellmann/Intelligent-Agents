import random
from typing import List


class Environment:
    def __init__(self):
        self.steps_left = 10
        self.state = [0.0, 0.0, 0.0]

    def get_observation(self) -> List[float]:
        return self.state

    def get_actions(self) -> List[bool]:
        return [False, True]

    def is_terminated(self) -> bool:
        return self.steps_left == 0

    def execute(self, action: int) -> float:
        if self.is_terminated():
            raise Exception("Game over", action)
        self.steps_left -= 1
        return random.random()


class Agent:
    def __init__(self, en: Environment):
        self.total_reward = 0.0
        self.round = 0
        self.actions = en.get_actions()

    def display(self, o):
        print(o)
        return o

    def observe(self, en: Environment):
        return self.display(en.get_observation())

    def act(self, en: Environment) -> float:
        return en.execute(self.display(random.choice(self.actions)))

    def step(self, en: Environment):
        self.round += 1
        print("Round: ", self.round)
        reward = self.act(en)
        self.total_reward += reward


if __name__ == "__main__":
    env = Environment()
    agent = Agent(env)

    while not env.is_terminated():
        agent.step(env)

    print('Total reward: %.4f' % agent.total_reward)
