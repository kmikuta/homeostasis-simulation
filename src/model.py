import matplotlib.pyplot as plt
from effector import Effector


class Model:
    def __init__(self, effectors: list[Effector]) -> None:
        self.effectors = effectors
        self.results = dict[Effector, list[float]]()
        self.thresholds = dict[Effector, list[float]]()

        for effector in self.effectors:
            self.results[effector] = [effector.state.value]
            self.thresholds[effector] = [effector.receptor.threshold]

    def perform_step(self) -> None:
        for effector in self.effectors:
            effector.perform_production()
            effector.state.perform_outflow()
            effector.receptor.evaluate()

        for effector in self.effectors:
            self.results[effector].append(effector.state.value)
            self.thresholds[effector].append(effector.receptor.threshold)

    def plot_results(self, plot_colors: list[str]) -> None:
        plt.figure(figsize=(16, 9), dpi=80)

        for idx, effector in enumerate(self.effectors):
            plt.plot(self.results[effector], plot_colors[idx] + '-')
            plt.plot(self.thresholds[effector], plot_colors[idx] + '--')

        plt.show()
