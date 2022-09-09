from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f"Send {message} to {self.email} by email")


class Phone(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"Send {message} to {self.phone} by SMS")


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    contact = Contact('Contact A', 'a@a.com', '0917-000-0000')

    s = Phone(contact.phone)
    e = Email(contact.email)

    manager = NotificationManager(s)
    manager.send('Hello!')

    # the child class Phone and Email
    #   can assume the place of Notification abstract class
    #   by making use of NotificationManager

    # manager.notification = s
    # manager.send('Hey again!')

    # manager.notification = e
    # manager.send("Hello!")


# LISKOV:  a child class can assume the place of its parent class


