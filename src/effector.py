from product import ProductState
from receptor import Receptor


class Effector:
    def __init__(self,
                 state: ProductState,
                 substrate: ProductState,
                 receptor: Receptor,
                 molecular_activity: float) -> None:
        self.state = state
        self.substrate = substrate
        self.receptor = receptor
        self.molecular_activity = molecular_activity

    def perform_production(self) -> None:
        signal = self.receptor.read_signal()
        amount = min(self.molecular_activity, self.substrate.value)
        prod = round(signal * amount, 2)

        self.substrate.subtract(prod)
        self.state.add(prod)
