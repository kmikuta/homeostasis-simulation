class ProductState:
    def __init__(self, initial_value: float, outflow_rate: float) -> None:
        self.value = initial_value
        self.outflow_rate = outflow_rate

    def add(self, value: float) -> None:
        self.value = round(self.value + value, 4)

    def subtract(self, value: float) -> None:
        self.value = round(self.value - value, 4)

    def perform_outflow(self) -> None:
        self.subtract(self.outflow_rate * self.value)
