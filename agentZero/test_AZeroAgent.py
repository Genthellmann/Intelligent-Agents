from agentZero.AZero import Environment
from agentZero.AZero import Agent


def test_display():
    en = Environment()
    agent = Agent(en)
    assert 'Observation' == agent.display('Observation')


def test_observe():
    en = Environment()
    agent = Agent(en)
    assert [0.0, 0.0, 0.0] == agent.observe(en)


def test_act():
    en = Environment()
    agent = Agent(en)
    a = agent.act(en)
    assert type(a) == type(0.01)

def test_step():
    en = Environment()
    agent = Agent(en)
    preround = agent.round
    pretotal = agent.total_reward
    agent.step(en)
    postround = agent.round
    posttotal = agent.total_reward
    assert (preround+1) == postround
    assert pretotal < posttotal

