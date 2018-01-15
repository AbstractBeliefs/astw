import dbus

class Thymio(object):
    def __init__(self, name):
        self.name = name
        self.bus = dbus.SessionBus()
        self.network = dbus.Interface(
            self.bus.get_object("ch.epfl.mobots.Aseba", "/"),
            dbus_interface="ch.epfl.mobots.AsebaNetwork"
        )

        self.left_target = self.left_speed
        self.right_target = self.right_speed

    @property
    def left_speed(self):
        return int(self.network.GetVariable(self.name, "motor.left.speed")[0])
    @property
    def right_speed(self):
        return int(self.network.GetVariable(self.name, "motor.right.speed")[0])

    @property
    def left_target(self):
        return self._left_target
    @left_target.setter
    def left_target(self, speed):
        self._left_target = speed
        self.network.SetVariable(self.name, "motor.left.target", [speed])

    @property
    def right_target(self):
        return self._right_target
    @right_target.setter
    def right_target(self, speed):
        self._right_target = speed
        self.network.SetVariable(self.name, "motor.right.target", [speed])

    @property
    def front_prox(self):
        return map(int, self.network.GetVariable(self.name, "prox.horizontal"))[:5]
    @property
    def rear_prox(self):
        return map(int, self.network.GetVariable(self.name, "prox.horizontal"))[5:]
    @property
    def bottom_prox(self):
        return map(int, self.network.GetVariable(self.name, "prox.ground.delta"))

    def forward(self, speed=100):
        self.left_target = speed
        self.right_target = speed

    def backward(self, speed=100):
        self.forward(-speed)

    def left(self, speed=100):
        self.left_target = -speed
        self.right_target = speed

    def right(self, speed=100):
        self.left(-speed)

    def stop(self):
        self.forward(0)
