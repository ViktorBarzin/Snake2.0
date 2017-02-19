class Point:

    def __init__(self, cord_x, cord_y, data_cont):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.data_cont = data_cont

    def get_content(self):
        return self.data_cont
