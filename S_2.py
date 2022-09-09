class SMSSubscribers:
    def __init__(self):
        self.subscribers = {}
        self.number = 0

    def add_subscriber(self, subscriber):
        self.number += 1
        self.subscribers[self.number] = subscriber

    def __str__(self):
        return str(self.subscribers)

    def store_subscribers(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.subscribers))


s = SMSSubscribers()
s.add_subscriber('0917000000')
s.add_subscriber('09170000001')

print(s)

s.store_subscribers('subscribers_list.txt')



# store_subscribers() method breaks the single responsibility principle

# to not break the principle we need to create another class StoreSubscribers
#   and add a static method store_subscribers