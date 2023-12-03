from effector import Effector
from model import Model
from product import ProductState
from receptor import DelayedReceptor

# control units
state1 = ProductState(initial_value=0, outflow_rate=0.1)
state2 = ProductState(initial_value=0, outflow_rate=0.1)
state3 = ProductState(initial_value=0, outflow_rate=0.1)
state4 = ProductState(initial_value=100000000000, outflow_rate=0.1)

effector1 = Effector(
    id='unit1',
    state=state1,
    substrate=state4,
    receptor=DelayedReceptor(delay=5, threshold=6, state=state1),
    molecular_activity=4,
)

effector2 = Effector(
    id='unit2',
    state=state2,
    substrate=state4,
    receptor=DelayedReceptor(delay=5, threshold=4, state=state2),
    molecular_activity=3,
)

effector3 = Effector(
    id='unit3',
    state=state3,
    substrate=state4,
    receptor=DelayedReceptor(delay=5, threshold=3, state=state3),
    molecular_activity=2,
)

model = Model(effectors=[effector1, effector2, effector3])

# simulation
simulation_time = 200

for _ in range(simulation_time):
    model.perform_step()

# results
model.plot_results(['b', 'r', 'g'])
