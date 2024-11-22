class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__power = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__last_volume = self.MIN_VOLUME

    def power(self):
        if not self.__power:
            self.__power = True
        else:
            self.__power = False
            if self.__muted:
                self.__muted = False

    def mute(self):
        if self.__power:
            if not self.__muted:
                self.__muted = True
                self.__last_volume = self.__volume
                self.__volume = 0
            else:
                self.__muted = False
                self.__volume = self.__last_volume

    def channel_up(self):
        if self.__power:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__power:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        if self.__power:
            if self.__muted:
                self.mute()
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__power:
            if self.__muted:
                self.mute()
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        if self.__power:
            return f"Power = {self.__power}, Channel = {self.__channel}, Volume = {0 if self.__muted else self.__volume}"
        else:
            return f"Power = {self.__power}, Channel = {self.__channel}, Volume = {self.__volume}"


