import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
kivy.require('1.11.1')


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__()
        self.name = kwargs['name']
        self.controller = kwargs['controller']

    def login(self):
        try:
            self.controller.connect_imap(self.ids.imap_server_url.text,
                                         self.ids.email_address.text,
                                         self.ids.passwd.text)
            print("connected")
            self.manager.transition.direction = 'left'
            self.manager.current = 'mailbox'

        except Exception as e:
            print(e)
            print("could not connect")


class MailBox(Button):

    def __init__(self, **kwargs):
        super(MailBox, self).__init__()
        self.controller = kwargs['controller']
        self.text = kwargs['text']

    def select(self):
        print(self.controller.search_emails(self.text))


class MailBoxContainer(BoxLayout):

    def __init__(self, **kwargs):
        super(MailBoxContainer, self).__init__()
        self.controller = kwargs['controller']
        self.orientation = "vertical"
        listButton = Button(text="list mailboxes")
        listButton.bind(on_press=self.show_mailboxes)
        self.add_widget(listButton)

    def show_mailboxes(self, instance):
        mailboxes = self.controller.list_mailboxes()
        for a_mailbox in mailboxes:
            self.add_widget(MailBox(text=a_mailbox,
                                    controller=self.controller))


class MailScreen(Screen):

    def __init__(self, **kwargs):
        super(MailScreen, self).__init__()
        self.name = kwargs['name']
        self.controller = kwargs['controller']
        side_menu = self.ids["side_menu"]
        side_menu.add_widget(MailBoxContainer(controller=self.controller),
                             index=-1)

    def logout(self):
        try:
            self.controller.close_imap_connection()
            print('disconnected')
        except Exception as e:
            print(e)
            print('dude, try to connect first')


class ViewApp(App):

    def __init__(self, controller=None):
        super(ViewApp, self).__init__()
        self.controller = controller

    def build(self):
        # return LoginView()
        manager = ScreenManager()
        manager.add_widget(LoginScreen(name="login",
                                       controller=self.controller))
        manager.add_widget(MailScreen(name="mailbox",
                                      controller=self.controller))
        return manager


if __name__ == "__main__":
    view = ViewApp()
    view.run()
