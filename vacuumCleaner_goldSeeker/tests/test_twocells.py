
from vacuumCleaner import twocells

env = twocells.Environment()

def test_show_state(capsys):
    env.show_state(1, 1)
    captured = capsys.readouterr()
    assert captured.err == ''
    a = "t= 1 : [['irobo0', 'dirt'], [' ', 'dirt']] Pos: left Cmd: left\n"
    assert captured.out == a

def test_get_observation():
    a = env.get_observation()
    assert a == [env.agent_pos, env.state[env.agent_pos][1]]

def test_show_observation(capsys):
    a = env.get_observation()
    env.show_observation(a)
    captured = capsys.readouterr()
    assert captured.err == ''
    print(captured.out)
    b = "[0, 1]\nPercept. Pos: left Cell: dirty\n"
    assert captured.out == b

def test_get_actions():
    a = env.get_actions()
    assert a == [0, 1, 2, 3]

def test_is_cleanF():
    assert env.is_clean() == False

def test_is_cleanT():
    env.state = [[1, 0], [0, 0]]
    assert env.is_clean() == True

def test_is_terminatedF():
    assert env.is_terminated() == False

def test_is_terminatedT():
    env.steps_left = 0
    assert env.is_terminated() == True

def test_is_terminatedF():
    env.steps_left = 50
    assert env.is_terminated() == False

def pre_post_match(state, pos, action, next_state, next_pos):
    env.steps_left = 50
    env.state = state
    env.agent_pos = pos
    o = env.execute(action)
    print(env.state)
    assert env.state == next_state
    assert env.agent_pos == next_pos

def test_executeA():
    pre_post_match([[1, 1], [0, 1]], 0, 0, [[1, 1], [0, 1]], 0)

def test_executeB():
    pre_post_match([[1, 1], [0, 1]], 0, 1, [[1, 1], [0, 1]], 0)

def test_executeC():
    pre_post_match([[1, 1], [0, 1]], 0, 2, [[0, 1], [1, 1]], 1)

def test_executeD():
    pre_post_match([[1, 1], [0, 1]], 0, 3, [[1, 0], [0, 1]], 0)

def test_executeE():
    pre_post_match([[1, 1], [0, 1]], 0, 3, [[1, 0], [0, 1]], 0)

def test_executeF():
    pre_post_match([[1, 0], [0, 1]], 0, 0, [[1, 0], [0, 1]], 0)

def test_executeG():
    pre_post_match([[1, 0], [0, 1]], 0, 1, [[1, 0], [0, 1]], 0)

def test_executeH():
    pre_post_match([[1, 0], [0, 1]], 0, 2, [[0, 0], [1, 1]], 1)

def test_executeI():
    pre_post_match([[1, 0], [0, 1]], 0, 3, [[1, 0], [0, 1]], 0)

def test_executeJ():
    pre_post_match([[0, 0], [1, 1]], 1, 0, [[0, 0], [1, 1]], 1)

def test_executeK():
    pre_post_match([[0, 0], [1, 1]], 1, 1, [[1, 0], [0, 1]], 0)

def test_executeL():
    pre_post_match([[0, 0], [1, 1]], 1, 2, [[0, 0], [1, 1]], 1)

def test_executeM():
    pre_post_match([[0, 0], [1, 1]], 1, 3, [[0, 0], [1, 0]], 1)

