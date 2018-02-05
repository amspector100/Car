class Car:
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph!" .format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 1000

    def step(self):
        self.odometer += self.speed
        self.time += 1

    @property
    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            return 0

if __name__ == '__main__':
    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake,"
            "show [O]domoeter, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that, I'm a car")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == "B":
            my_car.brake()
        elif action == 'O':
            print(("The car has driven {} kilometers"
                .format(my_car.odometer)))
        elif action == 'S':
            print("Average speed = {}".format(my_car.average_speed))
        if my_car.speed > 30:
            print("Oh no! I'm going to crash!")
            break
        my_car.step()
        my_car.say_state()