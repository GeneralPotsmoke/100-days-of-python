from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog

def add_watermark(image_path, watermark_text):
    image = Image.open(image_path)
    width, height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 36)
    text_width, text_height = draw.textsize(watermark_text, font)
    position = (width - text_width - 10, height - text_height - 10)
    draw.text(position, watermark_text, (255, 255, 255), font=font)
    image.show()

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        add_watermark(file_path, "Sample Watermark")

root = tk.Tk()
root.title("Watermark Adder")
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()
root.mainloop()
