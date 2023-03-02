import pytest

from vacuumCleaner.irobo0Main import run_optimal_agent
from vacuumCleaner.irobo0Main import run_rnd_agent
from vacuumCleaner.irobo0Main import run_sim_agent
from vacuumCleaner.irobo0Main import run_sim_rnd_agent
from vacuumCleaner.irobo0Main import play

def gen_inputs():
    inputs = [3, 2, 3]
    for action in inputs:
        yield action

GEN=gen_inputs()

def test_play(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda : next(GEN)) 
    a = 0.1
    p = play()
    assert type(a) == type(p)
    assert 15.0 == p

def test_run_optimal_agent():
    p = run_optimal_agent()
    assert 15.0 == p


def test_run_rnd_agent():
    p = run_rnd_agent()
    assert p <= 15.0


def test_run_sim_agent():
    p = run_sim_agent()
    assert p <= 15.0


def test_run_sim_rnd_agent():
    rl = run_sim_rnd_agent()
    # 100 steps
    assert rl[0] == 100
    # mean profit is less than 15.0
    assert rl[1] < 15.0
    # variance is less than 15.0
    assert rl[2] < 15.0
