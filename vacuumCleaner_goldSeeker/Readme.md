# Vacuum Cleaner

2-cell vacuum cleaner and three agents.

**taskenvironment.py**

The class **TaskEnvironment** 
counts steps, cost computation at the agent
and implements the communication between 
agent and environment:

**irobo0.py**

The class **irobo0.py** contains the different agents:
(Class **Agent** implements a random agent, 
class **OptAgent** an optimal agent, and
class **HumanAgent** a game interface)

**twocells.py** 

The class **Environment**
implements the two cell vaccum cleaner world.
The class **SimEnvironment** is for simulations and 
output not needed for simulations is not shown.


Run Tests:

   python3 -m pytest tests/test_twocells.py
   python3 -m pytest tests/


