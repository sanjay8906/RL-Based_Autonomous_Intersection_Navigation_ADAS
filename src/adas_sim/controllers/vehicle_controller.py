class VehicleController:

    def __init__(self):

        self.manual = False

        self.steering = 0.0
        self.throttle = 0.0

    def toggle(self):
        self.manual = not self.manual
        print(f"Mode: {'MANUAL' if self.manual else 'AUTO'}")

    def auto_drive(self):
        return [0.0, 0.5]

    def manual_drive(self):

        return [self.steering, self.throttle]