from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Phone(Notification):
    def notify(self, message, phone):
        print(f"Send {message} to {phone} by SMS")


class Email(Notification):
    def notify(self, message, email):
        print(f"Send {message} to {email} by email")


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification, contact):
        self.notification = notification
        self.contact = contact

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, contact.email)
        elif isinstance(self.notification, Phone):
            self.notification.notify(message, contact.phone)


if __name__ == '__main__':
    contact = Contact('Contact A', 'a@a.com', '0917-000-0000')
    manager = NotificationManager(Phone(), contact)
    manager.send('Hey A!')

    manager = NotificationManager(Email(), contact)
    manager.send('Hey again!')

# LISKOV:  a child class can assume the place of its parent class

# to conform with the Liskov principle,
#   we can redefine notify() under the Notification class
#   so that it doesn't explicitly require the email parameter

# we can do this by removing the email parameter under the Notification class,
#   then adding an init to the Email class
#   init is in a way similar to getter and setter