'''O - Open and Close Principle

“software entities (classes, modules, functions, etc.) should be
    open for extension,
    but closed for modification”

which means you should be able to extend a class behavior, without modifying it.
'''


class StorageSubscribers:
    def __init__(self, subscribe):
        self.subscribe = subscribe

    def subscribed(self):
        if self.subscribe == 'sms':
            print(SMS_SUBSCRIBERS)
        elif self.subscribe == 'email':
            print(EMAIL_SUBSCRIBERS)
        elif self.subscribe == 'viber':
            print("Pass")
        return self.subscribe

    def upload(self, filename):
        if self.subscribe == 'sms':
            pass
        elif self.subscribe == 'email':
            pass


SMS_SUBSCRIBERS = {1: '0917000000', 2: '09170000001'}
EMAIL_SUBSCRIBERS = {1: 'aa@a.com', 2: 'bb@b.com'}

sub = StorageSubscribers('sms').subscribed()
print(sub)

sub = StorageSubscribers('email').subscribed()
print(sub)


# possible problem moving forward
# if we add a type of subscription, say telegram or viber
# 

