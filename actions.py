class EnterText:
    def __init__(self, text, locator):
        self.text = text
        self.locator = locator
    def perform_as(self, actor):
        driver = actor.ability.driver
        driver.find_element(*self.locator).send_keys(self.text)
class Click:
    def __init__(self, locator):
        self.locator = locator
    def perform_as(self, actor):
        driver = actor.ability.driver
        driver.find_element(*self.locator).click()