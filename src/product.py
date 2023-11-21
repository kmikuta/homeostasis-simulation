class ProductState:
    def __init__(self, initial_value):
        self.value = initial_value

    def add(self, value):
        self.value = round(self.value + value, 4)

    def subtract(self, value):
        self.value = round(self.value - value, 4)
