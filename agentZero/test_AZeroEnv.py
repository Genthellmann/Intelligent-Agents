from agentZero.AZero import Environment
import pytest


def test_get_actions():
    print('Here')
    env = Environment()
    assert [False, True] == env.get_actions()


def test_get_observation():
    env = Environment()
    assert [0.0, 0.0, 0.0] == env.get_observation()


def test_is_terminatedA():
    env = Environment()
    assert False == env.is_terminated()


def test_executeA():
    env = Environment()
    a = env.execute(1)
    assert type(a) == type(0.01)


def test_executeB():
    env = Environment()
    for i in range(1,9):
        a = env.execute(1)
        assert type(a) == type(0.01)

def test_executeC():
    env = Environment()
    with pytest.raises(Exception):
        for i in range(1,12):
            a = env.execute(1)

def test_is_terminatedB():
    env = Environment()
    for i in range(1,11):
        a = env.execute(1)
    assert True == env.is_terminated()


