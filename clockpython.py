import time

class Counter:
    def __init__(self, _name):
        self._name = _name
        self._count = 0

    def Increment(self):
        self._count += 1

    def Reset(self):
        self._count = 0

    @property
    def Ticks(self):
        return self._count

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

class Clock:
    def __init__(self):
        self.seconds = Counter("seconds")
        self.minutes = Counter("minutes")
        self.hours = Counter("hours")

    def Tick(self):
        if self.seconds.Ticks != 59:
            self.seconds.Increment()
        elif self.minutes.Ticks != 59 and self.seconds.Ticks == 59:
            self.minutes.Increment()
            self.seconds.Reset()
        else:
            self.hours.Increment()
            self.minutes.Reset()
            self.seconds.Reset()
        if self.hours.Ticks == 24:
            self.hours.Reset()
            self.minutes.Reset()
            self.seconds.Reset()

    def Read(self):
        return f"{self.hours.Ticks:02d}:{self.minutes.Ticks:02d}:{self.seconds.Ticks:02d}"

    def Reset(self):
        self.seconds.Reset()
        self.minutes.Reset()
        self.hours.Reset()

myClock = Clock()

# while True:
#     print(myClock.Read())
#     myClock.Tick()
#     time.sleep(1)

for i in range(86402):
    print(myClock.Read())
    myClock.Tick()
