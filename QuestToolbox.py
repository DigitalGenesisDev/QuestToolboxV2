import tkinter
import customtkinter  # <- import the CustomTkinter module
import platform

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("1280x720")
root_tk.title("QuestToolbox")

os_name = platform.system()

def button_function():
    print(os_name)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function, text="Print OS Name")
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()