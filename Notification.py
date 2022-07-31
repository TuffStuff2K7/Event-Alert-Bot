from plyer import notification
def notify(Heading, Message):
    notification.notify(
        title = Heading,
        message = Message,
        timeout = 5,
        app_icon = "Icon.ico",
        app_name = "Event Bot by Atul"
    )
