import pickle

class Speedometer:
    def __init__(self) -> None:
        self.max_speed = "dummy"

    # def __init__(self, max_speed: int) -> None:
    #     self.max_speed = max_speed
    
    # def print_max_speed(self) -> None:
    #     print("this is from Speedometer")
    #     print(self.max_speed)

class Car:
    def __init__(self, max_speed: int) -> None:
        # self.speedometer = Speedometer(max_speed)
        self.max_speed = max_speed

    def print_max_speed(self) -> None:
        # self.speedometer.print_max_speed()
        print(self.max_speed)

    def save(self) -> None:
        with open('pickle.pkl', 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def restore(cls) -> 'Car':
        with open('pickle.pkl', 'rb') as f:
            return pickle.load(f)