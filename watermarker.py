import getpass
from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


def display_image(image):
    new_photo = ImageTk.PhotoImage(image.resize((480, 270)))
    display_img = canvas.create_image(0, 0, image=new_photo, anchor=NW)
    canvas.configure(image=display_img)


def open_file():
    global img
    global user_photo
    user_photo = Image.open(tkinter.filedialog.askopenfilename()).resize((1920, 1080)).convert(mode="RGBA")
    display_image(user_photo)


def add_watermark():
    global user_photo
    global img
    txt = Image.new("RGBA", (1920, 1080), (255, 255, 255, 0))
    wmk_fnt = ImageFont.truetype("fonts/Ubuntu-Regular.ttf", 200)
    d = ImageDraw.Draw(txt)
    d.text(xy=(50, 50), text=f"{getpass.getuser()}", fill=(0, 0, 0, 160), font=wmk_fnt)
    d.text(xy=(500, 400), text=getpass.getuser(), fill=(0, 0, 0, 160), font=wmk_fnt)
    d.text(xy=(890, 750), text=getpass.getuser(), fill=(0, 0, 0, 160), font=wmk_fnt)
    user_photo = Image.alpha_composite(user_photo, txt)
    display_image(user_photo)


def save_file():
    global user_photo
    user_photo.save(f"{tkinter.filedialog.asksaveasfilename()}.png")


FONT = ("Ubuntu", 10, "normal")

user_photo = None
win = Tk()
win.title("Watermarker")
canvas = Canvas(win, width=480)
no_photo = ImageTk.PhotoImage(image=Image.open("Images/no_image.jpg").resize((480, 270)))
img = canvas.create_image(0, 0, image=no_photo, anchor=NW)
canvas.grid(row=1, column=0, columnspan=3)

add_img = Button(text="Import Image", font=FONT, highlightthickness=0, justify="center", command=open_file)
add_img.grid(row=0, column=0, columnspan=3)
add_wmk_btn = Button(text="Add Watermark", font=FONT, highlightthickness=0, justify="center", command=add_watermark)
add_wmk_btn.grid(row=2, column=0)
save_btn = Button(text="Save As...", font=FONT, highlightthickness=0, justify="center", command=save_file)
save_btn.grid(row=2, column=2)
exit_btn = Button(text="Exit", font=FONT, highlightthickness=0, justify="center", command=exit)
exit_btn.grid(row=3, column=0, columnspan=3)


if __name__ == "__main__":
    win.mainloop()

