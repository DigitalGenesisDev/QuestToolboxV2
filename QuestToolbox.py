from ntpath import realpath
import pyinstaller
import tkinter
import customtkinter
import platform
import time
from ppadb.client import Client as AdbClient
import os

    
root_tk = customtkinter.CTk()  # create the customTk window
root_tk.geometry("1280x720")
root_tk.title("QuestToolbox")
customtkinter.set_appearance_mode("System")


def ADB():()
os_name = platform.system()
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
##os.chdir("/platform-tools-windows/platform-tools")
os.system("adb start-server")


# button functions
def print_OSName():
    print(os_name)

def test_command1():
    print("test button 1")

def test_command2():
    print("test button 2")

def adbtest():
    client = AdbClient(host="127.0.0.1", port=5037)
    print(client.version())
    

# buttons
OSName_button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=print_OSName, text="Check OS")
OSName_button.place(relx=0.07, rely=0.05, anchor=tkinter.CENTER)

test_button1 = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=test_command1, text="test button 1", width=225, height=100)
test_button1.place(relx=0.2, rely=0.27, anchor=tkinter.CENTER)

test_button2 = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=test_command2, text="test button 2", width=225, height=100)
test_button2.place(relx=0.42, rely=0.27, anchor=tkinter.CENTER)

adbtest_button1 = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=adbtest, text="ADB Test", width=225, height=100)
adbtest_button1.place(relx=0.42, rely=0.27, anchor=tkinter.CENTER)

root_tk.mainloop()

# Changes Recording Res and FPS to 1920x1080 60fps
# Testing test
# adb shell setprop debug.oculus.capture.width 1080
# adb shell setprop debug.oculus.capture.height 1920
# adb shell setprop debug.oculus.capture.bitrate 10000000
# adb shell setprop debug.oculus.foveation.level 0
# adb shell setprop debug.oculus.capture.fps 60