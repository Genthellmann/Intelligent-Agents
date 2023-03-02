class TaskEnvironment:
    def __init__(self):
        self.name = "Task Environment"
        self.i = 0

    def run(self, agent, env):
        percept = env.get_observation()
        env.show_state(self.i, 0)
        print("Percept:", percept)
        env.show_observation(percept)
        while not env.is_terminated():
            if env.is_clean():
                agent.show_costs()
                break
            action = agent.act(percept)
            percept = env.execute(action) 
            env.show_state(self.i, action)
            env.show_observation(percept)
            self.i += 1
        return agent.get_costs()
        
