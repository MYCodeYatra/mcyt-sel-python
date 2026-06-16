from actions import EnterText, Click
class LoginTask:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    # We still store Locators, but we separate them from the Actions!
    USER_INPUT = ("id", "username")
    PASS_INPUT = ("id", "password")
    LOGIN_BTN = ("id", "login-btn")
    def perform_as(self, actor):
        # A Task delegates work to the low-level Actions
        actor.attempts_to(
            EnterText(self.username, self.USER_INPUT),
            EnterText(self.password, self.PASS_INPUT),
            Click(self.LOGIN_BTN)
        )