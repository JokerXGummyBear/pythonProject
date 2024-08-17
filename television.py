class Television:
    MIN_VOLUME = 0
    MIN_CHANNEL = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 3

    def __init__(self):
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__status = False # TV power is off

    def power(self):     # turns tv on or off
        self.__status = not self.__status

    def mute(self):     # mutes and unmutes tv
        if self.__status:
            self.__muted = True

    def channel_up(self):  # increases the channel
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self): # decreases the channel
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):   # increases the volume
        if self.__status:
            self.muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume +=1

    def volume_down(self):  # decreases the volume
        if self.__status:
            self.muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -=1

    def __str__(self):
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

