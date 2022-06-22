import tkinter as tk
import read_HW_V2
import psutil
import wmi

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()
window.geometry("300x500")
greeting = tk.Label(text="adgsdfh")
greeting.pack()

# label = tk.Label(
#     text="chuj",
#     foreground ="white",  # Set the text color to white
#     background ="orange",  # Set the background color to black
#     width = 10,
#     height = 10
# )
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# button.pack()
# label.pack()
frame_a = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
frame_b = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)

# label_a = tk.Label(master=frame_a, text=read_HW_V2.current_cpu())
labels = []
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):

    label = tk.Label(master = frame_a, text=(f"Core {i}: {percentage}%"))
    label.pack()
    labels.append(label)

svmem = psutil.virtual_memory()
label_b = tk.Label(master=frame_b, text=f"Used: {read_HW_V2.get_size(svmem.used)}")
label_b.pack()

t = wmi.WMI(namespace=)


frame_a.pack()
frame_b.pack()

window.mainloop()


