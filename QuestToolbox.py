import tkinter
import customtkinter
import platform
import discord_rpc
import time
from ppadb.client import Client as AdbClient
import os

def readyCallback(current_user):
    print('Our user: {}'.format(current_user))

def disconnectedCallback(codeno, codemsg):
    print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
        codeno, codemsg
    ))

def errorCallback(errno, errmsg):
    print('An error occurred! Error {}: {}'.format(
        errno, errmsg
    ))

def ADB():
    

        # Note: 'event_name': callback
    callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
    discord_rpc.initialize('928736720864821358', callbacks=callbacks, log=True)
    start = time.time()
    print(start)
    discord_rpc.update_connection()
    discord_rpc.run_callbacks()
    discord_rpc.update_presence(
            **{
                'details': 'Main Menu',
                'start_timestamp': start,
                'large_image_key': 'toolboxlogo'
            }
    )
    discord_rpc.update_connection()
    discord_rpc.run_callbacks()
    

root_tk = customtkinter.CTk()  # create the customTk window
root_tk.geometry("1280x720")
root_tk.title("QuestToolbox")
customtkinter.set_appearance_mode("System")



os_name = platform.system()

os.system("cd _file_/platform-tools-windows/platform-tools/")
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
#
# adb shell setprop debug.oculus.capture.width 1080
# adb shell setprop debug.oculus.capture.height 1920
# adb shell setprop debug.oculus.capture.bitrate 10000000
# adb shell setprop debug.oculus.foveation.level 0
# adb shell setprop debug.oculus.capture.fps 60