class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, destination_floor):
        if destination_floor < self.bottom_floor:
            destination_floor = self.bottom_floor
        elif destination_floor > self.top_floor:
            destination_floor = self.top_floor

        while self.current_floor != destination_floor:
            if self.current_floor < destination_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator going up. Current floor: {self.current_floor}")
        else:
            print("Already in the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator going down. Current floor: {self.current_floor}")
        else:
            print("Already in the bottom floor.")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print("Invalid elevator number")
            return
        
        print(f'Elevator {elevator_number} going to floor {destination_floor}')
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)
        print(f'Elevator {elevator_number} has arrived on floor {destination_floor}')
    

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)
        print('Fire alarm rang! All elevators have gone to the bottom floor.')


def main():
    building = Building(1, 15, 4)
    building.run_elevator(3, 15)
    building.run_elevator(2, 4)
    building.fire_alarm()

main()
