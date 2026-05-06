import time

class Clock:
    def __init__ (self, hour=0, min=0, sec=0):
        self.hour = hour
        self.min = min
        self.sec = sec

    def run (self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1

            if self.min == 60:
                self.min = 0
                self.hour += 1

                if self.hour == 24:
                    self.hour = 0
        
    def show (self) :
        print(f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}')


clock = Clock(23, 59, 58)
while True:
    clock.show()
    time.sleep(1)
    clock.run()