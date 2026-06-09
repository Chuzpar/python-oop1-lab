class Coffee:
    def __init__(self, size):
        self.size = size
        self.price = 0

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if new_size in ["Small", "Medium", "Large"]:
            self._size = new_size
        else:
            raise ValueError("Size must be Small, Medium, or Large")

    def tip(self, amount):
        self.price += amount