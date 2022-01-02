import tkinter
import customtkinter
import platform

root_tk = tkinter.Tk()  # create the Tk window
root_tk.geometry("1280x720")
root_tk.title("QuestToolbox")

os_name = platform.system()

def print_OSName():
    print(os_name)

def test_command():
    print("test button 1")

OSName_button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=print_OSName, text="Print OS Name")
OSName_button.place(relx=0.07, rely=0.05, anchor=tkinter.CENTER)

test1_button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=test_command, text="test button", width=225, height=100)
test1_button.place(relx=0.2, rely=0.25, anchor=tkinter.CENTER)

root_tk.mainloop()

# Changes Recording Res and FPS to 1920x1080 60fps
#
# adb shell setprop debug.oculus.capture.width 1080
# adb shell setprop debug.oculus.capture.height 1920
# adb shell setprop debug.oculus.capture.bitrate 10000000
# adb shell setprop debug.oculus.foveation.level 0
# adb shell setprop debug.oculus.capture.fps 60