class AppStore:
    def __init__(self):
        self.applications = []

    def add_application(self, app):
        if app not in self.applications:
            self.applications.append(app)

    def remove_application(self, app):
        if app in self.applications:
            self.applications.remove(app)

    def block_application(self, app):
        if app in self.applications:
            app.blocked = True

    def total_apps(self):
        return len(self.applications)

class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False

