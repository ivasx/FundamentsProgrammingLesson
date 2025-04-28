class Clock:
    def __init__(self, time = 0):
        self.__time = None
        self.set_time(time)

    def set_time(self, time):
        if self.__check_time(time):
            self.__time = time
        else:
            self.__time = 0


    def get_time(self):
        return self.__time
    
    @staticmethod
    def __check_time(time):
        if isinstance(time, int) and 0 <= time < 100000:
            return True
        else:
            return False

if __name__ == '__main__':
    clock = Clock(4530)
    print(clock.get_time())