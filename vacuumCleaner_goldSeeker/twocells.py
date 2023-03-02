from typing import List

class Environment:
    # Initial state: (("agent", "dirt"), ("nobody", "dirt"))  
    def __init__(self):
        self.steps_left = 50
        # (("agent", "dirt"), ("nobody", "dirt"))  
        self.state = [[1, 1], [0, 1]]
        self.agent_pos = 0

    def show_state(self, i, a):
        agent = [" ", "irobo0"]
        floor = ["clean", "dirt"]
        pos = ["left", "right"]
        actions = ["pass", "left", "right", "suck"]
        cells = [[
            agent[self.state[0][0]],
            floor[self.state[0][1]]],
            [agent[self.state[1][0]],
             floor[self.state[1][1]]]]
        print("t=", i, ":", cells,
              "Pos:", pos[self.agent_pos],
              "Cmd:", actions[a])

    def get_observation(self) -> List[int]:
        return [self.agent_pos, self.state[self.agent_pos][1]]

    def show_observation(self, observation):
        print(observation)
        pos = ["left", "right"]
        cell = ["clean", "dirty"]
        print("Percept. Pos:", pos[observation[0]],
              "Cell:", cell[observation[1]])

        # Actions: 0=pass, 1=left, 2=right, 3=suck

    @staticmethod
    def get_actions() -> List[int]:
        return [0, 1, 2, 3]

    def is_clean(self) -> bool:
        return (self.state[0][1] == 0) and (self.state[1][1] == 0)

    def is_terminated(self) -> bool:
        return self.steps_left == 0

    def execute(self, action: int):
        if self.is_terminated():
            raise Exception("Game over")
        # pass
        if action == 0:
            pass
        # pass if cmd left and pos left 
        if (action == 1) and (self.agent_pos == 0):
            pass
            # left if cmd left and pos right
        if (action == 1) and (self.agent_pos == 1):
            self.state[self.agent_pos][0] = 0
            self.agent_pos = 0
            self.state[self.agent_pos][0] = 1
        # right if cmd right and pos left 
        if (action == 2) and (self.agent_pos == 0):
            self.state[self.agent_pos][0] = 0
            self.agent_pos = 1
            self.state[self.agent_pos][0] = 1
        # pass if cmd right and pos right
        if (action == 2) and (self.agent_pos == 1):
            pass
            # pass if cmd suck and clean
        if (action == 3) and (self.state[self.agent_pos][1] == 0):
            pass
            # suck if cmd suck and dirty
        if (action == 3) and (self.state[self.agent_pos][1] == 1):
            self.state[self.agent_pos][1] = 0
        self.steps_left -= 1
        return self.get_observation()


class SimEnvironment(Environment):
    def show_observation(self, observation):
        pass

    def show_state(self, i, a):
        pass

