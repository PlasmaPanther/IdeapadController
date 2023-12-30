from tkinter import *
from BatterySettings import BatterySettings
from MiscModes import MiscellaneousModes

class Panel:
    def __init__(self):

        self.root = None

        self.BatteryPanel = None
        self.MiscPanel = None

    def Load(self):

        print("Initializing panel...")

        self.root = Tk()

        self.BatteryPanel = BatterySettings(self.root)
        self.MiscPanel = MiscellaneousModes(self.root)

        self.root.title("IdeapadController")

        self.LoadGUI()

    def LoadGUI(self):
        
        self.BatteryPanel.LoadBatterySettings()
        self.MiscPanel.LoadMiscModes()
        
        print("Finished initializing!")


    def OnClose(self):
        self.BatteryThresholdTxt = open("Preferences.txt", "w")
        
        self.BatteryThresholdTxt.write(str(self.BatteryPanel.BatteryThresholdPreference))
        
        self.BatteryThresholdTxt.close()

        print("Closing")


    def MainLoop(self):
        self.BatteryPanel.UpdateBattery()
        self.root.mainloop()
