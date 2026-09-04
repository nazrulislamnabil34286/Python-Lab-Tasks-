class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.10
        return total_fare + maintenance_charge


bus = Bus("AIUB Bus", 40)

print("Bus Name:", bus.name)
print("Seating Capacity:", bus.seating_capacity)
print("Total Fare:", bus.fare())