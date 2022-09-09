class StorageSubscribers:
    def __init__(self, subscribe):
        self.subscribe = subscribe

    def subscribed(self):
        if self.subscribe == 'sms':
            print(SMS_SUBSCRIBERS)
        elif self.subscribe == 'email':
            print(EMAIL_SUBSCRIBERS)
        elif self.subscribe == 'telegram':
            print(TELEGRAM_SUBSCRIBERS)
        return self.subscribe

    def upload(self, filename):
        if self.subscribe == 'sms':
            print(f"Upload sms subscribers code to {filename}")
        elif self.subscribe == 'email':
            print(f"Upload email subscribers code to {filename}")
        elif self.subscribe == 'telegram':
            print(f"Upload telegram subscribers to {filename}")


SMS_SUBSCRIBERS = {1: '0917000000', 2: '09170000001'}
EMAIL_SUBSCRIBERS = {1: 'aa@a.com', 2: 'bb@b.com'}
TELEGRAM_SUBSCRIBERS = {1: 'aaa', 2: 'bbb'}

sub = StorageSubscribers('sms').subscribed()
print(sub)

sub = StorageSubscribers('email').subscribed()
print(sub)


# needs add new code to both subscribed() and upload()
# time consuming and less manageable if we are working with a large chunk of code

# we can optimize this by using the Open-Closed principle

# create abstract classes Subscribers and Uploader
#   then create a class for each type of subscription inheriting the abstract classes