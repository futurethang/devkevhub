class Session:
    def __init__(self):
        self.data = {}

    def update_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        return self.data.get(key)

    def clear_data(self):
        self.data = {}

session = Session()