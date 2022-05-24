import pickle
from models.car import Car


def save_car() -> None:
    max_speed = 100
    car = Car(max_speed)
    car.print_max_speed()
    car.save()

def load_car() -> None:
    car = Car.restore()
    print(car.speedometer.max_speed)

if __name__ == '__main__':
    # save_car()

    load_car()