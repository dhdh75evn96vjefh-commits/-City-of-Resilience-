class EnergyManager:
    def __init__(self, initial_energy):
        self.stored = initial_energy
    def produce(self, amount):
        self.stored += amount
    def consume(self, amount):
        if self.stored >= amount:
            self.stored -= amount
            return True
        return False
