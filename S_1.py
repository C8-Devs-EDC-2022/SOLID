'''
S - Single Responsibility Principle

“a class should have only one reason to change”
which means every class should have a:
    single responsibility or
    single job or
    single purpose. "
'''


class SMSSubscribers:
    def __init__(self):
        self.subscribers = {}
        self.number = 0

    def add_subscriber(self, subscriber):
        self.number += 1
        self.subscribers[self.number] = subscriber

    def __str__(self):
        return str(self.subscribers)


s = SMSSubscribers()
s.add_subscriber('09170000000')
s.add_subscriber('09170000001')

print(s)

# if we want to store the subscribers list to a file



