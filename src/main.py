from effector import Effector
from model import Model
from product import InifiniteSubstrate, ProductState
from receptor import DelayedReceptor

# states
state1 = ProductState(initial_value=0, outflow_rate=0.1)
state2 = ProductState(initial_value=0, outflow_rate=0.1)
state3 = ProductState(initial_value=0, outflow_rate=0.1)

# units
effector1 = Effector(
    id='unit1',
    state=state1,
    substrate=InifiniteSubstrate(1000),
    receptor=DelayedReceptor(delay=5, threshold=6, state=state1),
    molecular_activity=4,
)

effector2 = Effector(
    id='unit2',
    state=state2,
    substrate=InifiniteSubstrate(1000),
    receptor=DelayedReceptor(delay=5, threshold=4, state=state2),
    molecular_activity=3,
)

effector3 = Effector(
    id='unit3',
    state=state3,
    substrate=InifiniteSubstrate(1000),
    receptor=DelayedReceptor(delay=5, threshold=3, state=state3),
    molecular_activity=2,
)

# simulation
model = Model(effectors=[effector1])
simulation_time = 200

for idx in range(simulation_time):
    # if (idx == 100):
    #     model.effectors[0].state.add(20)
    model.perform_step()

# results
model.plot_results(['b', 'r', 'g'])
