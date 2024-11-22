class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Default setting for the TV: Power is off, volume is at a min, channel is at a min, mute is off, and last volume is set to min.
        """
        self.__power = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__last_volume = self.MIN_VOLUME

    def power(self) -> None:
        """
        Changes the power state of the TV, and if muted, rests the mute state
        """
        if not self.__power:
            self.__power = True
        else:
            self.__power = False
            if self.__muted:
                self.__muted = False

    def mute(self) -> None:
        """
        Changes the mute state if the TV is on. When muted, the volume is set to 0, when unmuted, it returns to the previous volume.
        """
        if self.__power:
            if not self.__muted:
                self.__muted = True
                self.__last_volume = self.__volume
                self.__volume = 0
            else:
                self.__muted = False
                self.__volume = self.__last_volume

    def channel_up(self) -> None:
        """
        Increases the channel by 1 if the TV is on. It loops back if it goes past the max channel.
        """
        if self.__power:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the channel by 1 if the tv is on. It loops back if it goes pas the min channel.
        """
        if self.__power:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the volume by 1 if the tv is on. Unmutes if the TV is currently muted
        """
        if self.__power:
            if self.__muted:
                self.mute()
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by 1 if the tv is on . Unmutes if the tv is currently muted
        """
        if self.__power:
            if self.__muted:
                self.mute()
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Provides a string statemtn of the TV's current status
        :return: A string describing the power state, channel, and vlume. If Muted, the volume is 0.
        """
        if self.__power:
            return f"Power = {self.__power}, Channel = {self.__channel}, Volume = {0 if self.__muted else self.__volume}"
        else:
            return f"Power = {self.__power}, Channel = {self.__channel}, Volume = {self.__volume}"


