from queue import Queue


class DelayedReceptor():
    def __init__(self, threshold, delay, initial_value):
        self._threshold = threshold
        self._queue = Queue(delay)

        for _ in range(delay):
            self._queue.put_nowait(initial_value)

    def read_signal(self):
        signal = 1 - self._queue.get_nowait() / self._threshold

        if (signal < 0):
            return 0
        else:
            return round(signal, 4)

    def update(self, current_value):
        self._queue.put_nowait(current_value)
