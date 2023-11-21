import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from control import ControlUnit

# control units
unit = ControlUnit(initial_value=0, outflow_rate=0.2, delay=8, molecular_activity=4, threshold=6)

# simulation
simulation_time = 200
threshold_values = [unit.threshold] * simulation_time
results = list(map(lambda _: unit.perform_step(), range(simulation_time)))

# results
figure(figsize=(16, 9), dpi=80)
plt.plot(results)
plt.plot(threshold_values)
plt.show()
