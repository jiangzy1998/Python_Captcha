import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
import random
import string
import os
import errno
# import asyncio

name = 0
right_code = 'ABCD'

target_dir = '/home/jzy'
window = tk.Tk()
window.title('captcha')
window.geometry('300x300')

im = Image.open('/home/jzy/' + str(name+1) + '.jpg')
img = ImageTk.PhotoImage(im)
imLable = tk.Label(window, image=img)
imLable.pack()

# async def test(value):
#     show_jpg()
#     r = await asyncio.sleep(3)
#     print('input %s' % value)


def random_letter():
    # 生成一个随机字母
    letter = random.choice(string.ascii_uppercase)
    print('letter:', letter)
    global right_code
    right_code = right_code + letter
    print('right_code:', right_code)
    return letter


# 生成随即颜色
def random_color():
    color = (random.randint(0, 255),
             random.randint(0, 255),
             random.randint(0, 255))
    return color


def print_code():
    letter = random.choice(string.ascii_uppercase)
    print(letter)
    # return letter


def generate_captcha():
    print("generate_captcha")
    num = 1
    global right_code
    right_code = ''
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
            global name
            name += 1
            canvas.save(target_dir + '/' + str(name) + '.jpg', 'jpeg')


def show_img():
    global imLable, im, img
    generate_captcha()
    im = Image.open('/home/jzy/' + str(name) + '.jpg')
    print(name)
    img = ImageTk.PhotoImage(im)
    imLable.configure(image=img)
    # img = ImageTk.PhotoImage(im)
    # imLable.configure(image=img)
    # imLable.pack()


def check_input():
    global e
    var = e.get()
    print('e:', var)
    if var == right_code:
        print("OK")
    else:
        print("ERROR")


# loop = asyncio.get_event_loop()
# c = test(u'xxx')
# loop.run_until_complete(c)
# loop.close()
btn1 = tk.Button(window,
                 text='刷新',
                 width=30,
                 height=2,
                 command=show_img)
btn1.pack()

e = tk.Entry(window)
e.pack()

btn2 = tk.Button(window,
                 text='确定',
                 width=30,
                 height=2,
                 command=check_input)
btn2.pack()

if __name__ == '__main__':
    generate_captcha()
    print("main_generate_captcha")
    show_img()
    print("main_show_img")
    window.mainloop()
