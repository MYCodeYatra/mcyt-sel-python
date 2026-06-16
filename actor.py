class BrowseTheWeb:
    def __init__(self, driver):
        self.driver = driver
class Actor:
    def __init__(self, name):
        self.name = name
        self.ability = None
    def can(self, ability):
        self.ability = ability
        return self
    def attempts_to(self, *tasks):
        for task in tasks:
            task.perform_as(self)
    def asks(self, question):
        return question.answered_by(self)