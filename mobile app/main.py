from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')


class LoginScreen(Screen):

    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def forget_password(self):
        self.manager.transition.direction = "left"
        self.manager.current = "forget_password_screen"

    def login(self, uname, pword):
        with open("original.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Username or Password are incorrect"


class SignUpScreen(Screen):

    def add_user(self, uname, pword):
        with open("original.json") as file:
            users = json.load(file)
            passwords = [users[username]['password'] for username in users]
            if (uname in users) or (pword in passwords):
                self.ids.not_valid.text = "Username or password already exist"
            elif (uname == '') or (pword == ''):
                self.ids.not_valid.text = "Username or password are not valid"
            else:
                users[uname] = {'username': uname, 'password': pword,
                                'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
                self.manager.current = "sign_up_screen_success"
                with open("original.json", 'w') as file:
                    json.dump(users, file)


class SignUpScreenSuccess(Screen):

    def go_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):

    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class ForgetPasswordScreen(Screen):

    def get_password(self, uname):
        with open("original.json") as file:
            users = json.load(file)
        if uname in users:
            self.ids.password.text = "Your password is {}".format(users[uname]['password'])

    def go_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
