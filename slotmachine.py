import tkinter as tk
import random
from tkinter import PhotoImage
from PIL import Image, ImageTk

window = tk.Tk()

window.title("Slot Machine Game")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.resizable(False, False)
window["bg"] = "cadetblue3"

canvas = tk.Canvas(window, width=screen_width,
                   height=600, background='cadetblue3')
canvas.pack()

canvas.create_rectangle(236, 236, 1284, 584, outline='gray21', width=15)
canvas.create_rectangle(246, 246, 1274, 574,
                        fill='cadetblue2', outline='indianred2', width=15)
canvas.create_rectangle(586, 156, 934, 236, outline='gray21', width=15)
canvas.create_rectangle(596, 166, 924, 236,
                        fill='white', outline='indianred2', width=15)

canvas.create_rectangle(236, 236, 1284, 584, outline='gray21', width=15)
canvas.create_rectangle(646, 296, 874, 524, outline='gray21', width=30)
canvas.create_rectangle(996, 296, 1224, 524, outline='gray21', width=30)
canvas.create_rectangle(296, 296, 524, 524, outline='indianred2', width=15)
canvas.create_rectangle(646, 296, 874, 524, outline='indianred2', width=15)
canvas.create_rectangle(996, 296, 1224, 524, outline='indianred2', width=15)


jack_image = ImageTk.PhotoImage(Image.open("imge/JACKPOT.png"))
symbol_images = [
    "imge/symbol/seveno.png",
    "imge/symbol/cherry.png",
    "imge/symbol/lemon.png",
    #   "imge/symbol/orange.png",
    #   "imge/symbol/plum.png",
    #    "imge/symbol/bell.png",
    #    "imge/symbol/banana.png",
    #    "imge/symbol/watermelon.png"
]

symbol_images_tk = [ImageTk.PhotoImage(
    Image.open(image)) for image in symbol_images]

label1 = tk.Label(window, image=random.choice(
    symbol_images_tk), borderwidth=10, relief="sunken")
label2 = tk.Label(window, image=random.choice(
    symbol_images_tk), borderwidth=10, relief="sunken")
label3 = tk.Label(window, image=random.choice(
    symbol_images_tk), borderwidth=10, relief="sunken")

label1.place(x=300, y=300)
label2.place(x=650, y=300)
label3.place(x=1000, y=300)


def show_jackpot():
    global jackpot_label, button
    jackpot = ImageTk.PhotoImage(Image.open("imge/jackpot.png"))
    jackpot_label = tk.Label(window, image=jackpot,
                             borderwidth=10, relief="sunken")
    jackpot_label.place(x=500, y=650)
    button = tk.Button(window, text="Okay", command=hide_jackpot)
    button.place(x=500, y=950)


def hide_jackpot():
    jackpot_label.destroy()
    button.destroy()


def spin_machine():
    current_img = [label1.cget("image"), label2.cget(
        "image"), label3.cget("image")]
    if all(image == symbol_images_tk[0] for image in current_img):
        show_jackpot()
    else:
        label1.configure(image=random.choice(symbol_images_tk))
        label2.configure(image=random.choice(symbol_images_tk))
        label3.configure(image=random.choice(symbol_images_tk))


window.bind('<space>', lambda event: spin_machine())


window.mainloop()
