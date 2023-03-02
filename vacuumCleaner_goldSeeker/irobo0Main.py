import twocells
import irobo0
from taskenvironment import TaskEnvironment


def play():
    env = twocells.Environment()
    maxi = irobo0.HumanAgent()
    te = TaskEnvironment()

    profit = te.run(maxi, env)
    print("Game over. Your profit:", profit)
    return profit


def run_optimal_agent():
    env = twocells.Environment()
    maxi = irobo0.OptAgent()
    te = TaskEnvironment()

    profit = te.run(maxi, env)
    print("Game over. Your profit:", profit)
    return profit


def run_rnd_agent():
    env = twocells.Environment()
    maxi = irobo0.Agent()
    te = TaskEnvironment()

    profit = te.run(maxi, env)
    print("Game over. Your profit:", profit)
    return profit


def run_sim_agent():
    env = twocells.SimEnvironment()
    maxi = irobo0.Agent()
    te = TaskEnvironment()

    profit = te.run(maxi, env)
    print("Game over. Your profit:", profit)
    return profit


def run_sim_rnd_agent():
    def mean(x):
        return sum(x) / len(x)

    def var(xx):
        m = sum(xx) / len(xx)
        return sum([(x - m) ** 2 for x in xx]) / len(xx)

    sim_profit = []
    steps = 100

    for i in range(1, steps):
        p = run_sim_agent()
        sim_profit.append(p)

    mp = mean(sim_profit)
    v = var(sim_profit) ** 0.5
    print("iRobo0 Random Agent 2 Cells.\n", "Steps:",
          steps, "Trials. Mean Profit:", mp, "StdDev:", v)

    return [steps, mp, v, ]
