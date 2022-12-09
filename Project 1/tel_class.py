
from remote import *
from PyQt5.QtWidgets import *



class Television(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 50
    MIN_CHANNEL = 0
    MAX_CHANNEL = 10

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setMinimum(0)
        self.view.setPixmap(QtGui.QPixmap("0x0.jpg"))




        self.power_but.clicked.connect(self.power)
        self.vol_up_but.clicked.connect(self.volume_up)
        self.vol_down_but.clicked.connect(self.volume_down)
        self.ch_up_but.clicked.connect(self.channel_up)
        self.ch_down_but.clicked.connect(self.channel_down)
        self.mute_but.clicked.connect(self.mute)

    def power(self):
        #tv off
        if self.status == True:
            self.status = False
            self.power_label.setText('OFF')
            self.ch_label.setText(f'')
            self.horizontalSlider.setValue(self.MIN_VOLUME)
            self.view.setPixmap(QtGui.QPixmap("0x0.jpg"))
        #tv on
        else:
            self.status = True
            self.power_label.setText('ON')
            self.horizontalSlider.setValue(self.volume)
            self.channel = self.channel
            self.ch_label.setText(f'{self.channel}')
            if self.channel == 0:
                self.view.setPixmap(QtGui.QPixmap('bravo.png'))
            elif self.channel == 1:
                self.view.setPixmap(QtGui.QPixmap('cbs.png'))
            elif self.channel == 2:
                self.view.setPixmap(QtGui.QPixmap('disney.jpg'))
            elif self.channel == 3:
                self.view.setPixmap(QtGui.QPixmap('food.png'))
            elif self.channel == 4:
                self.view.setPixmap(QtGui.QPixmap('hbo.png'))
            elif self.channel == 5:
                self.view.setPixmap(QtGui.QPixmap('history.jpg'))
            elif self.channel == 6:
                self.view.setPixmap(QtGui.QPixmap('lifetime.png'))
            elif self.channel == 7:
                self.view.setPixmap(QtGui.QPixmap('nbc.jpg'))
            elif self.channel == 8:
                self.view.setPixmap(QtGui.QPixmap('tlc.png'))
            elif self.channel == 9:
                self.view.setPixmap(QtGui.QPixmap('travel.png'))
            elif self.channel == 10:
                self.view.setPixmap(QtGui.QPixmap('usa.png'))



    #volume up
    def volume_up(self):
        if self.status == True:
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1
                self.horizontalSlider.setValue(self.volume)
            if self.volume >= Television.MAX_VOLUME:
                pass

    #volume down
    def volume_down(self):
        if self.status == True:
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1
                self.horizontalSlider.setValue(self.volume)
            if self.volume <= Television.MIN_VOLUME:
                pass

    #channel change up
    def channel_up(self):
        if self.status == True:
            if self.channel < Television.MAX_CHANNEL:
                self.channel += 1
                if self.channel == 1:
                    self.view.setPixmap(QtGui.QPixmap('cbs.png'))
                elif self.channel == 2:
                    self.view.setPixmap(QtGui.QPixmap('disney.jpg'))
                elif self.channel == 3:
                    self.view.setPixmap(QtGui.QPixmap('food.png'))
                elif self.channel == 4:
                    self.view.setPixmap(QtGui.QPixmap('hbo.png'))
                elif self.channel == 5:
                    self.view.setPixmap(QtGui.QPixmap('history.jpg'))
                elif self.channel == 6:
                    self.view.setPixmap(QtGui.QPixmap('lifetime.png'))
                elif self.channel == 7:
                    self.view.setPixmap(QtGui.QPixmap('nbc.jpg'))
                elif self.channel == 8:
                    self.view.setPixmap(QtGui.QPixmap('tlc.png'))
                elif self.channel == 9:
                    self.view.setPixmap(QtGui.QPixmap('travel.png'))
                elif self.channel == 10:
                    self.view.setPixmap(QtGui.QPixmap('usa.png'))
            else:
                self.channel = Television.MIN_CHANNEL
            self.ch_label.setText(f'{self.channel}')
            if self.channel == 0:
                self.view.setPixmap(QtGui.QPixmap('bravo.png'))

    #channel change down
    def channel_down(self):
        if self.status == True:
            if self.channel > Television.MIN_CHANNEL:
                self.channel -= 1
                if self.channel == 0:
                    self.view.setPixmap(QtGui.QPixmap('bravo.png'))
                elif self.channel == 1:
                    self.view.setPixmap(QtGui.QPixmap('cbs.png'))
                elif self.channel == 2:
                    self.view.setPixmap(QtGui.QPixmap('disney.jpg'))
                elif self.channel == 3:
                    self.view.setPixmap(QtGui.QPixmap('food.png'))
                elif self.channel == 4:
                    self.view.setPixmap(QtGui.QPixmap('hbo.png'))
                elif self.channel == 5:
                    self.view.setPixmap(QtGui.QPixmap('history.jpg'))
                elif self.channel == 6:
                    self.view.setPixmap(QtGui.QPixmap('lifetime.png'))
                elif self.channel == 7:
                    self.view.setPixmap(QtGui.QPixmap('nbc.jpg'))
                elif self.channel == 8:
                    self.view.setPixmap(QtGui.QPixmap('tlc.png'))
                elif self.channel == 9:
                    self.view.setPixmap(QtGui.QPixmap('travel.png'))

            else:
                self.channel = Television.MAX_CHANNEL
            self.ch_label.setText(f'{self.channel}')
            if self.channel == 10:
                self.view.setPixmap(QtGui.QPixmap('usa.png'))

    #tv mute
    def mute(self):
        if self.status == True:
            if self.muted == False:
                self.muted = True
                self.mutes = self.volume
                self.volume = Television.MIN_VOLUME
                self.horizontalSlider.setValue(self.volume)
            else:
                self.muted = False
                self.volume = self.mutes
                self.horizontalSlider.setValue(self.volume)





def main():
    Television()

if __name__ == '__main__':
    main()
