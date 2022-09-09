'''
D - Dependency Inversion

High-level modules/classes should not depend on low-level modules/classes.

Both should depend upon abstractions.

Abstractions should not depend upon details.

Details should depend upon abstractions.
'''


from abc import ABC, abstractmethod


class NotificationControl(ABC):      # Interface
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class NotificationControlEDC(NotificationControl):
    def turn_on(self):
        print(f"EDC Notification is ON")

    def turn_off(self):
        print(f"EDC Notification is OFF")


class NotificationSetting:
    def __init__(self, c: NotificationControl):
        self.client = c
        self.on = False

    def set(self):
        if self.on:
            self.client.turn_off()
        else:
            self.client.turn_on()
            self.on = True


class NotificationControlA(NotificationControl):
    def turn_on(self):
        print(f"A Notification is ON")

    def turn_off(self):
        print(f"A Notification is OFF")


edc = NotificationControlEDC()
setting = NotificationSetting(edc)
setting.set()   # ON
setting.set()   # OFF


a = NotificationControlA()
a.turn_on()         # Turn on button
a.turn_off()        # Turn off button

setter = NotificationSetting(a)
setter.set()        # Single button
setter.set()


setting = NotificationSetting(a)
setting.set()   # ON
setting.set()   # OFF
setting.set()   # ON
