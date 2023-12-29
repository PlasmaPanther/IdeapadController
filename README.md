# IdeapadController
Simple GUI app that I made for my ideapad laptop to control some of it's features.

# Dependencies
* python3-tk

Install with:
```
sudo apt install python3-tk
```
# How to run
Make sure you have `virtualvenv` installed on your system.

* Download the source code and unzip
* Or
* Clone the repository
  ```
  git clone https://github.com/PlasmaPanther/IdeapadController.git
  ```
* Enter the folder
  ```
  cd IdeapadController
  ```
* Create a virtual enviorment with:
  ```
  virtualenv venv
  ```
* Activate the virtual enviorment with:
  ```
  source venv/bin/activate
  ```
* Run the app with sudo privileges:
  ```
  sudo python3 main.py
  ```
When you are done using the app make sure to deactivate the virtual enviorment with the `deactivate` command.

# TODO
* Add acpi_call command for rapid charge for models that support it.
* Add acpi_call command for cooling modes for models that support it.

# What works
* Switching between `conservation_mode` and `balanced_mode`
* Battery charge thresholds (will not discharge if set to a lower level, you need to unplug the laptop).
* Turning on/off the trackpad.
* Turning on/off the FnLock.

# Sidenote
I have tried this on my Lenovo Ideapad Gaming 3 - 15IHU6 and haven't tested this on other ideapad laptops but im certain it should work on your machine as long as you have the `ideapad_laptop` kernel module loaded. 

You can check if it's loaded with `lsmod | grep ideapad_laptop` command.
