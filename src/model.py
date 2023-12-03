import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
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
        legend = []

        for idx, effector in enumerate(self.effectors):
            y_values = np.array(self.results[effector])
            x_values = np.array(range(y_values.size))
            X_Y_Spline = make_interp_spline(x_values, y_values)

            X_ = np.linspace(x_values.min(), x_values.max(), 500)
            Y_ = X_Y_Spline(X_)
            T_ = self.thresholds[effector]

            plt.plot(X_, Y_, plot_colors[idx] + '-')
            plt.plot(T_, plot_colors[idx] + '--')

            legend.append(effector.id + ' value')
            legend.append(effector.id + ' threshold')

        plt.legend(legend)
        plt.show()
