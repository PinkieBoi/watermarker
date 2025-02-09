from tkinter import *
from PIL import ImageTk, Image


def open_file():
    file = "/home/pinkieboi/Pictures/bgs/wallpaper1.png"
    new_file= Image.open(file).resize((480, 270))
    (img_width, img_height) = new_file.size
    new_photo = ImageTk.PhotoImage(new_file, size=(img_width, img_height))
    new_img = canvas.create_image(0, 0, image=new_photo, anchor=NW)
    canvas.configure(image=new_img)


def add_watermark():
    pass


def save_file():
    pass


def exit_no_save():
    pass


FONT = ("Ubuntu", 10, "normal")

win = Tk()
win.title("Watermarker")
canvas = Canvas(win, width=480)
no_photo = ImageTk.PhotoImage(image=Image.open("Images/no_image.jpg").resize((480, 270)))
img= canvas.create_image(0, 0, image=no_photo, anchor=NW)

# Display image to be watermarked
# new_file = open_file()

# Allow user to add image
add_img = Button(text="Import Image", font=FONT, highlightthickness=0, justify="center", command=open_file)
# Button to add watermark
add_wmk_btn = Button(text="Add Watermark", font=FONT, highlightthickness=0, justify="center", command=add_watermark)
# Button to save watermarked copy of photo
save_btn = Button(text="Save As...", font=FONT, highlightthickness=0, justify="center", command=save_file)
# Button to exit without saving
exit_btn = Button(text="Exit", font=FONT, highlightthickness=0, justify="center", command=exit_no_save)

# Create input box to name watermarked photo before saving

# Place items on canvas
add_img.grid(row=0, column=0, columnspan=3)
canvas.grid(row=1, column=0, columnspan=3)
add_wmk_btn.grid(row=2, column=0)
save_btn.grid(row=2, column=2)
exit_btn.grid(row=3, column=0, columnspan=3)

win.mainloop()
