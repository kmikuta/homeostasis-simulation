from effector import Effector
from product import ProductState
from receptor import DelayedReceptor


class ControlUnit:
    def __init__(
        self,
        initial_value,
        outflow_rate,
        delay,
        molecular_activity,
        threshold
    ):
        self.state = ProductState(initial_value)
        self.receptor = DelayedReceptor(threshold, delay, initial_value)
        self.effector = Effector(molecular_activity)
        self.outflow_rate = outflow_rate
        self.threshold = threshold

    def state_snapshot(self):
        return self.state.value

    def perform_step(self):
        self.perform_production()
        self.evaluate_receptor()
        self.perform_outflows()
        return self.state.value

    def perform_production(self):
        signal = self.receptor.read_signal()
        product = self.effector.perform_production(signal)
        self.state.add(product)

    def evaluate_receptor(self):
        self.receptor.update(self.state.value)

    def perform_outflows(self):
        self.state.subtract(self.outflow_rate * self.state.value)
