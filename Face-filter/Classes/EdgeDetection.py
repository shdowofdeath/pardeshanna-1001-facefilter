from Constants import const_nums

class EdgeDetection:
    def __init__(self, img):
        self.img = img

    def edge_check_horizontal(self):
        for i in range(const_nums.ROWS):
            for j in range(const_nums.ROWS - 1):
                if(abs(self.img.arr[i][j] - self.img.arr[i][j+1]) > 0.1):
                    self.img.arr[i][j] = -1

    def edge_check_vertical(self):
        for i in range(const_nums.COLS - 1):
            for j in range(const_nums.COLS):
                if((self.img.arr[i][j] != -1 or self.img.arr[i+1][j] != -1) and (abs(self.img.arr[i][j] - self.img.arr[i+1][j]) > 0.1)):
                    self.img.arr[i][j] = -1