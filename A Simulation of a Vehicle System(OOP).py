import random
class Vehicle:
    def __init__(self, make, model, year, speed=0, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
        self.mileage = mileage
    def accelerate(self, increment):
        self.speed += increment
        if self.speed < 0:
            self.speed = 0
    def brake(self, decrement):
        self.speed -= decrement
        if self.speed < 0:
            self.speed = 0
    def drive(self, distance):
        if self.speed > 0:
            self.mileage += distance
        else:
            print("Vehicle must be moving to drive.")
    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Speed: {self.speed} mph, Mileage: {self.mileage} miles"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, speed=0, mileage=0):
        super().__init__(make, model, year, speed, mileage)
        self.num_doors = num_doors
    def get_info(self):
        return f"{super().get_info()}, Doors: {self.num_doors}"
    def honk(self):
      return "Honk Honk!"

class Truck(Vehicle):

    def __init__(self, make, model, year, cargo_capacity, speed=0, mileage=0):
        super().__init__(make, model, year, speed, mileage)
        self.cargo_capacity = cargo_capacity
    def load_cargo(self, cargo_weight):
        if cargo_weight <= self.cargo_capacity:
            print(f"Loaded {cargo_weight} lbs of cargo.")
        else:
            print("Cargo exceeds capacity.")
    def get_info(self):
      return f"{super().get_info()}, Capacity: {self.cargo_capacity}lbs"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size, speed=0, mileage=0):
        super().__init__(make, model, year, speed, mileage)
        self.engine_size = engine_size
    def wheelie(self):
        if self.speed>10:
            print("Doing a wheelie!")
        else:
            print("Speed up to do a wheelie!")
    def get_info(self):
        return f"{super().get_info()}, Engine Size: {self.engine_size}cc"
def simulate_vehicle_system():
    vehicles = []
    vehicles.append(Car("Toyota", "Camry", 2022, 4))
    vehicles.append(Truck("Ford", "F-150", 2021, 2000))
    vehicles.append(Motorcycle("Harley-Davidson", "Sportster", 2020, 1200))
    for vehicle in vehicles:
        print(vehicle.get_info())
        for _ in range(3):
            acceleration = random.randint(5, 20)
            braking = random.randint(5, 15)
            distance = random.randint(10, 50)
            vehicle.accelerate(acceleration)
            vehicle.drive(distance)
            vehicle.brake(braking)
            print(vehicle.get_info())
        if isinstance(vehicle, Car):
          print(vehicle.honk())
        if isinstance(vehicle, Truck):
          vehicle.load_cargo(random.randint(100, vehicle.cargo_capacity))
        if isinstance(vehicle, Motorcycle):
          vehicle.wheelie()
        print("-" * 20)
if __name__ == "__main__":
    simulate_vehicle_system()