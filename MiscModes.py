from tkinter import *
from functools import partial

class MiscellaneousModes:
    def __init__(self, root):

        self.MiscRoot = root

        self.IdeapadACPIPath = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00"
       
        self.Touchpad = open(self.IdeapadACPIPath + "/touchpad", "r")
        self.TouchpadMode = int(self.Touchpad.read())
        self.Touchpad.close()

        self.FnLock = open(self.IdeapadACPIPath + "/fn_lock", "r")
        self.FnLockMode = int(self.FnLock.read())
        self.FnLock.close()

        self.CheckBoxDict = {"Enable FnLock" : self.FnLockMode, "Enable Touchpad" : self.TouchpadMode}

    def LoadMiscModes(self):

        print("Loading Function Modes...")

        self.FunctionFrame = LabelFrame(self.MiscRoot, text="Misc", padx=10, pady=15)
        self.FunctionFrame.grid(column=1, row=0, padx=(5, 0), pady=(0, 30))
        
        for checkboxes in self.CheckBoxDict:

            self.CheckBoxDict[checkboxes] = IntVar(self.MiscRoot, self.CheckBoxDict.get(checkboxes))

            Checkbutton(self.FunctionFrame, text=checkboxes, variable=self.CheckBoxDict[checkboxes], command=partial(self.MiscSwitch, checkboxes), width=16).pack(padx=(0, 40), pady=(0, 15))

        print("Completed initializing misc modes")
    
    def MiscSwitch(self, index):

        if index == "Enable Touchpad" and self.CheckBoxDict[index].get() == 1:
           self.Touchpad = open(self.IdeapadACPIPath + "/touchpad", "w")
           self.Touchpad.write(str(self.CheckBoxDict[index].get()))
           self.Touchpad.close()
           print("Touchpad on")
        elif  index == "Enable Touchpad" and not self.CheckBoxDict[index].get() == 1:
           self.Touchpad = open(self.IdeapadACPIPath + "/touchpad", "w")
           self.Touchpad.write(str(self.CheckBoxDict[index].get()))
           self.Touchpad.close()
           print("Touchpad off")

        if index == "Enable FnLock" and self.CheckBoxDict[index].get() == 1:
           self.Touchpad = open(self.IdeapadACPIPath + "/fn_lock", "w")
           self.Touchpad.write(str(self.CheckBoxDict[index].get()))
           self.Touchpad.close()
           print("Fn locked")
        elif  index == "Enable FnLock" and not self.CheckBoxDict[index].get() == 1:
           self.Touchpad = open(self.IdeapadACPIPath + "/fn_lock", "w")
           self.Touchpad.write(str(self.CheckBoxDict[index].get()))
           self.Touchpad.close()
           print("Fn unlocked")
