"""
Ok, I don't actually know how cars work.

But I CAN tell you this is ugly code.
"""
class Engine:
    def __init__(self, weight, torque):
        self.weight = weight
        self.torque = torque
        self.speed = 0
        self.gas_on = False

    def max_speed(self):
        return self.torque / self.weight

    def burn_gas(self):
        self.gas_on = True
        if self.speed < self.max_speed:
            self.speed += 1

    def shut_off_gas(self):
        self.gas_off = False
        if self.speed > 0:
            self.speed -= 1

class GasPedal:
    def __init__(self, engine):
        self.engine = engine
        self.is_pressed = False

    def press_pedal(self):
        self.is_pressed = True
        self.engine.burn_gas()

    def release_pedal(self):
        self.is_pressed = False
        self.engine.shut_off_gas()

class SelfDrivingCar:
    def __init__(self, pedal):
        self.pedal = pedal

    def accelerate(self, desired_speed):
        while self.pedal.engine.speed < desired_speed:
            self.pedal.engine.burn_gas()
        self.pedal.engine.shut_off_gas()

    def decelerate(self, desired_speed):
        while self.pedal.engine.speed > desired_speed:
            self.pedal.engine.shut_off_gas()  # not how a car works but whatever


