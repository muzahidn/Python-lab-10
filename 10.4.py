from random import randint

class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

    def accelerate(self, change_of_speed):
        if change_of_speed < 0:
            if self.current_speed + change_of_speed < 0:
                self.current_speed = 0 
            else:
                self.current_speed = self.current_speed - change_of_speed
        elif change_of_speed > 0:
            if self.current_speed + change_of_speed > self.maximum_speed:
                self.current_speed = self.maximum_speed
            else:
                self.current_speed = self.current_speed + change_of_speed

    def drive(self, number_of_hours_drove):
        self.travelled_distance += (self.current_speed * number_of_hours_drove)


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_increase = randint(-10, 15)
            car.accelerate(speed_increase)
            car.drive(1)

    def print_status(self):
        print(f"{'Reg-Number':<12} | {'Max-Speed (km/h)':<16} | {'Distance (km)':<12}")
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                distance = f'{car.travelled_distance} -> (Winner)'
            else:
                distance = car.travelled_distance
            print(f"{car.registration_number:<12} | {car.maximum_speed:<16} | {distance:<12}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


def main():
    cars = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        maximum_speed = randint(100, 200)
        car = Car(registration_number, maximum_speed)
        cars.append(car)

    grand_derby = Race("Grand Demolition Derby", 8000, cars)

    hour_counter = 0
    while not grand_derby.race_finished():
        grand_derby.hour_passes()
        hour_counter += 1
        if hour_counter % 10 == 0:
            print(f"Race Status after {hour_counter} hours:")
            grand_derby.print_status()
            print()

    print("Final Race Status:")
    grand_derby.print_status()


main()
