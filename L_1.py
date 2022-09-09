'''
L - Liskov Substitution

“Derived or child classes must be substitutable for their base or parent classes“

This principle ensures that any class
        that is the child of a parent class should be usable
        in place of its parent without any unexpected behavior.
'''

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f"Send {message} to {email} by email")


e = Email()
e.notify('Hey!', 'aaa@a.com')

# LISKOV:  a child class can assume the place of its parent class

# What if we add SMS notification, sms notifs does not require email argument


class Phone(Notification):
    def notify(self, message, phone):
        print(f"Send {message} to {phone} by SMS")

s = Phone()
s.notify('Hello', 's@s.com')

# LISKOV:  a child class can assume the place of its parent class

# problem: any derived class should be able to implement the superclass
#   here, notification object should still be able to implement the Notification superclass
#       and notification_a class should also be able to implement the Notification superclass
#           * Email and Phone class inherits the Notification class

# we can create a signature for the notify()

