from enum import Enum


class Subscription(Enum):
    POWER_PLANT = 1
    WELLS = 2
    TURBINE = 3


class Name:
    def __init__(self, name):
        self.name = name


class NotificationSubscriptions:
    def __init__(self):
        self.notification_subscriptions = []

    def add_notification_subscription(self, name, subscription):
        self.notification_subscriptions.append((name, subscription))


class InspectSubscriptions:
    def __init__(self, name_notification_subscriptions):
        subscriptions = name_notification_subscriptions.notification_subscriptions

        for subscriber in subscriptions:
            if subscriber[1] == Subscription.POWER_PLANT:
                print(f"{subscriber[0].name} is in the PP list")
            elif subscriber[1] == Subscription.WELLS:
                print(f"{subscriber[0].name} is in the Wells list")
            elif subscriber[1] == Subscription.TURBINE:
                print(f"{subscriber[0].name} is in the Turbine list")


employee_1 = Name('Employee 1')
employee_2 = Name('Employee 2')
employee_3 = Name('Employee 3')

notif_subs = NotificationSubscriptions()
notif_subs.add_notification_subscription(employee_1, Subscription.POWER_PLANT)
notif_subs.add_notification_subscription(employee_2, Subscription.WELLS)
notif_subs.add_notification_subscription(employee_3, Subscription.TURBINE)

InspectSubscriptions(notif_subs)




