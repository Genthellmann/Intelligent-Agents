import random
from typing import List


class Environment:
    def __init__(self):
        self.steps_left = 10

    @staticmethod
    def get_observation(self) -> List[float]:
        return [0.0, 0.0, 0.0]

    @staticmethod
    def get_actions() -> List[bool]:
        return [True, False]

    def is_done(self) -> bool:
        return self.steps_left == 0

    def action(self, action: int) -> float:
        if self.is_done():
            raise Exception("Game over", action)
        self.steps_left -= 1
        return random.random()


class Agent:
    def __init__(self):
        self.total_reward = 0.0

    def step(self, en: Environment):
        actions = en.get_actions()
        reward = en.action(random.choice(actions))
        self.total_reward += reward


if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print("Total reward: %.4f" % agent.total_reward)
