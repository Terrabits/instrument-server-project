class MyDevice:
    def __init__(self, initial_data=0.0):
        # properties
        self.is_open = True
        self._data    = float(initial_data)

    # data (float) property
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = float(data)

    def close(self):
        self.is_open = False
