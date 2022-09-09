class SMSSubscribers:
    def __init__(self):
        self.subscribers = {}
        self.number = 0

    def add_subscriber(self, subscriber):
        self.number += 1
        self.subscribers[self.number] = subscriber

    def __str__(self):
        return str(self.subscribers)


class StoreSubscribers:
    @staticmethod
    def store_subscribers(filename, subscribers):
        with open(filename, 'w') as f:
            f.write(str(subscribers))


s = SMSSubscribers()
s.add_subscriber('0917000000')
s.add_subscriber('09170000001')


save = StoreSubscribers()
save.store_subscribers('subscribers.txt', s)


# This way, we can still utilize objects derived from SMSSubscribers()
#   without needing to update/change the SMSSubscribers() class

