from abc import ABC, abstractmethod


class Subscribers(ABC):
    @abstractmethod
    def subscribed(self):
        print(f'Subscription {self.subscribed()}')
        pass


class Uploader(ABC):
    @abstractmethod
    def upload(self, filename):
        print("Upload base")
        pass


class SMS(Subscribers, Uploader):
    def subscribed(self):
        return SMS_SUBSCRIBERS

    def upload(self, filename):
        print(f"Save to {filename}")
        with open(filename, 'w') as f:
            f.write(str(SMS_SUBSCRIBERS))
        return "Success"


class Email(Subscribers, Uploader):
    def subscribed(self):
        return EMAIL_SUBSCRIBERS

    def upload(self, filename):
        print(f"Save to {filename}")
        with open(filename, 'w') as f:
            f.write(str(Email().subscribed()))
        return "Success"


class Telegram(Subscribers, Uploader):
    def subscribed(self):
        return TELEGRAM_SUBSCRIBERS

    def upload(self, filename):
        print(f"Save to {filename}")
        with open(filename, 'w') as f:
            f.write(str(Telegram().subscribed()))
        return "Success"


SMS_SUBSCRIBERS = {1: '0917000000', 2: '09170000001'}
EMAIL_SUBSCRIBERS = {1: 'aa@a.com', 2: 'bb@b.com'}
TELEGRAM_SUBSCRIBERS = {1: 'aaa', 2: 'bbb'}

s = SMS()
sub = s.subscribed()
print(sub)
s.upload('subscribers.txt')

e = Email()
sub_e = e.subscribed()
print(sub_e)
e.upload('esub.txt')

# Open for extension i.e. telegram


