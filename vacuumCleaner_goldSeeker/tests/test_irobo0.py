
from vacuumCleaner.irobo0 import Agent

max = Agent()

def test_observeA():
    o = max.observe([0, 1]) 
    assert o == [0,1] 

def test_observeAS(capsys):
    o = max.observe([0, 1]) 
    captured = capsys.readouterr()
    assert captured.err == ''
    a = "Percept.  Pos: left Cell: dirty\n"
    print(captured.out)
    assert a == captured.out

def test_observeB():
    o = max.observe([0, 0]) 
    assert o == [0,0] 

def test_observeBS(capsys):
    o = max.observe([0, 0]) 
    captured = capsys.readouterr()
    assert captured.err == ''
    a = "Percept.  Pos: left Cell: clean\n"
    print(captured.out)
    assert a == captured.out

def test_observeC():
    o = max.observe([1, 1]) 
    assert o == [1,1] 

def test_observeCS(capsys):
    o = max.observe([1, 1]) 
    captured = capsys.readouterr()
    assert captured.err == ''
    a = "Percept.  Pos: right Cell: dirty\n"
    print(captured.out)
    assert a == captured.out

def test_observeD():
    o = max.observe([1, 0]) 
    assert o == [1,0] 

def test_observeDS(capsys):
    o = max.observe([1, 0]) 
    captured = capsys.readouterr()
    assert captured.err == ''
    a = "Percept.  Pos: right Cell: clean\n"
    print(captured.out)
    assert a == captured.out

def pre_post_cost(pre_cost, action, observation, post_cost):
    max.tc = pre_cost
    c = max.compute_costs(action, observation)
    assert max.tc == c
    assert c == post_cost


def test_compute_costsA():
    pre_post_cost(0.0, 0, [0, 0], 0.0)

def test_compute_costsB():
    pre_post_cost(0.0, 1, [0, 0], -1.0)

def test_compute_costsC():
    pre_post_cost(0.0, 2, [0, 0], -1.0)

def test_compute_costsD():
    pre_post_cost(0.0, 3, [0, 0], -2.0)

def test_compute_costsE():
    pre_post_cost(0.0, 0, [1, 0], 0.0)

def test_compute_costsF():
    pre_post_cost(0.0, 1, [1, 0], -1.0)

def test_compute_costsG():
    pre_post_cost(0.0, 2, [1, 0], -1.0)

def test_compute_costsH():
    pre_post_cost(0.0, 3, [1, 0], -2.0)

def test_compute_costsI():
    pre_post_cost(0.0, 0, [0, 1], 0.0)

def test_compute_costsJ():
    pre_post_cost(0.0, 1, [0, 1], -1.0)

def test_compute_costsK():
    pre_post_cost(0.0, 2, [0, 1], -1.0)

def test_compute_costsL():
    pre_post_cost(0.0, 3, [0, 1], 8.0)

def test_compute_costsM():
    pre_post_cost(0.0, 0, [1, 1], 0.0)

def test_compute_costsN():
    pre_post_cost(0.0, 1, [1, 1], -1.0)

def test_compute_costsO():
    pre_post_cost(0.0, 2, [1, 1], -1.0)

def test_compute_costsP():
    pre_post_cost(0.0, 3, [1, 1], 8.0)

def test_get_costs():
    a = 5.0
    max.tc = a
    assert a == max.get_costs()

def test_show_costs(capsys):
    a = 5.0
    max.tc = a
    max.show_costs()
    captured = capsys.readouterr()
    assert captured.err == ''
    b = "Total profit: 5.0\n"
    assert captured.out == b

def test_show_actionPass(capsys):
    max.show_action(0)
    captured = capsys.readouterr()
    assert captured.err == ''
    b = "Cmd: pass\n"
    assert captured.out == b

def test_show_actionLeft(capsys):
    max.show_action(1)
    captured = capsys.readouterr()
    assert captured.err == ''
    b = "Cmd: left\n"
    assert captured.out == b

def test_show_actionRight(capsys):
    max.show_action(2)
    captured = capsys.readouterr()
    assert captured.err == ''
    b = "Cmd: right\n"
    assert captured.out == b

def test_show_actionRight(capsys):
    max.show_action(3)
    captured = capsys.readouterr()
    assert captured.err == ''
    b = "Cmd: suck\n"
    assert captured.out == b

def rnd_act():
    return max.act([1, 1])

def test_act():
    for i in range(1, 20):
        a = rnd_act()
        assert (a in range(0, 4))

