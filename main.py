from Panel import Panel
import os

if __name__ == "__main__":

    if os.geteuid() != 0:
        exit("You need root privileges to run this app!")

    panel = Panel()

    panel.Load()

    panel.MainLoop()

    panel.OnClose()
