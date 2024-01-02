class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom:
            target_floor = self.bottom
        elif target_floor > self.top:
            target_floor = self.top

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator going up. Current floor: {self.current_floor}")
        else:
            print("Already in the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator going down. Current floor: {self.current_floor}")
        else:
            print("Already in the bottom floor.")


def main():
    my_elevator = Elevator(1, 15)
    my_elevator.go_to_floor(12)
    my_elevator.go_to_floor(1)


main()
