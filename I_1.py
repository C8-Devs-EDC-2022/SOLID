'''
I - Interface Segregation

“do not force any client to implement an interface which is irrelevant to them“.

Here you should prefer
            MANY client interfaces
            rather than one general interface and
        each interface should have a specific responsibility.

'''


from abc import ABC, abstractmethod


class NotificationManager(ABC):
    def email(self):
        pass

    def text(self):
        pass

    def viber(self):
        pass


class NotificationManagerEDC(NotificationManager):
    def email(self):
        pass # email for EDC

    def text(self):
        pass # sms for EDC

    def viber(self):
        pass # viber for EDC


class NotificationManagerOld(NotificationManager):
    def email(self):
        pass # email for Old

    def text(self):
        pass # sms for Old

    def viber(self):
        pass # viber for Old