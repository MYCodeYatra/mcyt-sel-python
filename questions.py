class TextOf:
    def __init__(self, locator):
        self.locator = locator
    def answered_by(self, actor):
        driver = actor.ability.driver
        return driver.find_element(*self.locator).text