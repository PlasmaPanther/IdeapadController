from tkinter import *
from functools import partial
import subprocess

class BatterySettings:
    def __init__(self, root):

        self.BatteryRoot = root

        self.BatteryChargeMin = 60
        self.BatteryChargeMax = 80

        self.IsCharging = False
        self.IsRapidCharging = False

        # Get battery charge
        self.CurrentBatteryPercentage = int(subprocess.run(['cat /sys/class/power_supply/BAT*/capacity'], capture_output=True, text=True, shell=True).stdout)

        self.BatteryThresholdTxt = open("Preferences.txt", "r")
        self.BatteryThresholdPreference = int(self.BatteryThresholdTxt.read())
        self.BatteryThresholdTxt.close()

        # Get path and check charging mode
        self.IdeapadACPIPath = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00"
        self.BatteryFile = open(self.IdeapadACPIPath + "/conservation_mode", "r")

        # Store as int
        self.BatteryMode = int(self.BatteryFile.read())
        self.BatteryFile.close()

    def LoadBatterySettings(self):

        self.ButtonVar = StringVar(self.BatteryRoot)
        self.BatteryThresholdVar = IntVar(self.BatteryRoot, self.BatteryThresholdPreference)

        if(self.BatteryMode == 1):
            self.ButtonVar.set("Conservation Mode")
        else:
            self.ButtonVar.set("Balanced Mode")

        self.LoadBatteryModes()
        self.LoadBatteryThreshold()
    
    def LoadBatteryModes(self):

        self.BatteryFrame = LabelFrame(self.BatteryRoot, text="Battery Modes", pady=15)
        self.BatteryFrame.grid(column=0, row=0, padx=(5, 0), pady=(0, 30))

        Radiobutton(self.BatteryFrame, variable=self.ButtonVar, text="Conservation Mode", value="Conservation Mode", command=self.BatteryModeSwitch, width=18).pack(padx=(0, 0), pady=(15, 0))
        Radiobutton(self.BatteryFrame, variable=self.ButtonVar, text="Balanced Mode", value="Balanced Mode", command=self.BatteryModeSwitch, width=18).pack(padx=(0, 0), pady=(15, 0))
    	
    
    def LoadBatteryThreshold(self):

        self.BatteryThresholdFrame = LabelFrame(self.BatteryRoot, text="Battery threshold, %", padx=30, pady=25)
        self.BatteryThresholdFrame.grid(row=1, column=0, padx=(0, 0), pady=(0, 85))

        self.BatteryThresholdSlide = Scale(self.BatteryThresholdFrame, from_=self.BatteryChargeMin, to=self.BatteryChargeMax, variable=self.BatteryThresholdVar, orient=HORIZONTAL, command=self.BatterySlider)
        self.BatteryThresholdSlide.pack()
		
        self.BatteryThresholdMin = Label(self.BatteryThresholdFrame, text=f'{int(self.BatteryChargeMin)}')
        self.BatteryThresholdMin.place(x=0, y=45)
        
        self.BatteryThresholdMax = Label(self.BatteryThresholdFrame, text=f'{int(self.BatteryChargeMax)}')
        self.BatteryThresholdMax.place(x=90, y=45)

    def BatteryModeSwitch(self):

        if self.ButtonVar.get() == "Conservation Mode":
            
            self.BatteryMode = 1
            self.BatteryFile = open(self.IdeapadACPIPath + "/conservation_mode", "w")
            self.BatteryFile.write(str(self.BatteryMode))
            self.BatteryFile.close()
            print("Charging Mode: Conservation")
            
        elif self.ButtonVar.get() == "Balanced Mode":
            
            self.BatteryMode = 0
            self.BatteryFile = open(self.IdeapadACPIPath + "/conservation_mode", "w")
            self.BatteryFile.write(str(self.BatteryMode))
            self.BatteryFile.close()
            print("Charging Mode: Balanced")
 			

    def BatterySlider(self, placeholder_arg):

        # placeholder_arg doesn't do anything
        # It's there because TKinter doesn't like it when the function has only the "self" arg
        # When passed to the slider widget

        if self.CurrentBatteryPercentage < int(self.BatteryThresholdSlide.get()) and not self.IsCharging:
            
            self.BatteryMode = 0
            self.BatteryFile = open(self.IdeapadACPIPath + "/conservation_mode", "w")
            self.BatteryFile.write(str(self.BatteryMode))
            self.BatteryFile.close()
            
            self.ButtonVar.set("Balanced Mode")
            self.IsCharging = True
        
        elif self.CurrentBatteryPercentage >= int(self.BatteryThresholdSlide.get()) and self.IsCharging:

            self.BatteryMode = 1
            self.BatteryFile = open(self.IdeapadACPIPath + "/conservation_mode", "w")
            self.BatteryFile.write(str(self.BatteryMode))
            self.BatteryFile.close()
            
            self.ButtonVar.set("Conservation Mode")
            self.IsCharging = False
            print("Battery threshold reached")

    def UpdateBattery(self):
        
        # 30 seconds
        timer_update = 30000

        self.CurrentBatteryPercentage = int(subprocess.run(['cat /sys/class/power_supply/BAT*/capacity'], capture_output=True, text=True, shell=True).stdout)
        self.BatteryRoot.after(timer_update, self.UpdateBattery)
        self.BatteryRoot.after(timer_update, partial(self.BatterySlider, 0))
