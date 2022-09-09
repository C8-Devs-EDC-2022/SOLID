from abc import ABC, abstractmethod


class Email(ABC):
    @abstractmethod
    def email(self, group_name):
        pass


class Text(ABC):
    @abstractmethod
    def text(self, group_name):
        pass


class Viber(ABC):
    @abstractmethod
    def viber(self, group_name):
        pass


class NotificationManagerEDC(Email, Text, Viber):
    def email(self, group_name):
        pass  # email for EDC

    def text(self, group_name):
        pass  # sms for EDC

    def viber(self, group_name):
        pass  # viber for EDC


class NotificationManagerOld(Text):
    def text(self, group_name):
        pass  # sms for Old


class NotificationElmer(Viber):
    def viber(self, group_name):
        pass


elmer = NotificationElmer()
elmer.viber()

GROUP_NAME_TO_NOTIFY = 'PI-SUPPORT'

old = NotificationManagerOld()
old.text(GROUP_NAME_TO_NOTIFY)

edc = NotificationManagerEDC()
edc.text(GROUP_NAME_TO_NOTIFY)
edc.email(GROUP_NAME_TO_NOTIFY)
edc.viber(GROUP_NAME_TO_NOTIFY)
