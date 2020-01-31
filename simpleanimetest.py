import time


class SimpleAnime:
    timeDelay = 1000  # unit is ms
    move_step = '  '
    mode = 0
    steps = 10
    str1 = 'a'
    void_str = ''

    def time_delay(self):
        time.sleep(self.timeDelay / 1000)  # function sleep receive the para in second unit

    def move_rightward(self):
        for i in range(self.steps):
            print('\r', self.str1, end='')
            self.time_delay()
            self.str1 = self.move_step + self.str1

    def clear_line(self):
        print('\r', self.void_str, end='')



if __name__ == "__main__":
    aaa = SimpleAnime()
    aaa.move_rightward()
    aaa.clear_line()

