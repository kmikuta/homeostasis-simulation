class Effector:
    def __init__(self, molecular_activity):
        self._molecular_activity = molecular_activity

    def perform_production(self, signal):
        return round(signal * self._molecular_activity, 2)
