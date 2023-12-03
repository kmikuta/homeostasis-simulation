from queue import Queue

from product import ProductState


class Receptor():
    threshold: float

    def read_signal(self) -> float:
        pass

    def evaluate() -> float:
        pass


class DelayedReceptor(Receptor):
    def __init__(self, threshold: float, delay: int, state: ProductState) -> None:
        self.threshold = threshold
        self.state = state

        self._queue = Queue(delay)

        for _ in range(delay):
            self.evaluate()

    def read_signal(self) -> float:
        signal = 1 - self._queue.get_nowait() / self.threshold

        if (signal < 0):
            return 0
        else:
            return round(signal, 4)

    def evaluate(self) -> float:
        self._queue.put_nowait(self.state.value)
