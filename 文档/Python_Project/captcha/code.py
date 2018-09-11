from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import os
import errno
import tkinter as tk

target_dir = '/home/jzy'
window = tk.Tk()
window.title("captcha")
window.geometry('300x300')


def random_letter():
    # 生成一个随机字母
    letter = random.choice(string.ascii_uppercase)
    # print(letter)
    return letter


# 生成随即颜色
def random_color():
    color = (random.randint(0, 255),
             random.randint(0, 255),
             random.randint(0, 255))
    return color


def generate_captcha(num):
    if num > 1:
        # Check for target directory
        try:
            os.makedirs(target_dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    for img_num in range(num):
        # Generate canvas for captcha
        canvas_width = 240
        canvas_height = 60
        canvas = Image.new('RGB', (canvas_width, canvas_height), '#fff')
        # 选择字体
        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 45)
        draw = ImageDraw.Draw(canvas)
        # Generate random 4 digit captcha with random color
        for i in range(4):
            text_pox = 60 * i + random.randint(5, 15)
            text_poy = random.randint(2, 10)
            draw.text((text_pox, text_poy), random_letter(),
                      fill=random_color(), font=font)
        # Generate noise in canvas background
        for _ in range(random.randint(1500, 3000)):
            draw.point((random.randint(0, canvas_width),
                        random.randint(0, canvas_height)), fill=random_color())
        # Blur the text
        canvas = canvas.filter(ImageFilter.BLUR)
        if num > 1:
            canvas.save(target_dir + '/' + str(img_num) + '.jpg', 'jpeg')
        else:
            canvas.save(target_dir + '/' + '1.jpg', 'jpeg')


def main():
    btn = tk.Button(window,
                    text='刷新',
                    width=30,
                    height=2,
                    command=generate_captcha(1))
    btn.pack()


if __name__ == '__main__':
    main()
    window.mainloop
