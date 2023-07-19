import sensor, image, time
from image import SEARCH_EX, SEARCH_DS

# 颜色跟踪阈值(L Min, L Max, A Min, A Max, B Min, B Max)
thresholds = [(10, 90, 15, 127, -50, 50), # generic_red_thresholds
              (10, 90, -10, -128, -50, 25), # generic_green_thresholds
              (10, 90, 50, -50, -128, -10), # generic_blue_thresholds
              (10, 90, 50, -50, 25, 127)]#yellow
# 不要超过16个颜色阈值

thr1 = [(10, 90, 15, 127, -50, 50), (10, 90, -10, -128, -50, 25)]
thr2 = [(10, 90, 15, 127, -50, 50),(10, 90, 50, -50, 25, 127)]
thr3 = [(10, 90, 50, -50, -128, -10), (10, 90, 50, -50, 25, 127)]
thr4 = [(10, 90, -10, -128, -50, 25),(10, 90, 50, -50, -128, -10)]

thrb=[(10, 90, 50, -50, -128, -10)]
thrr=[(10, 90, 8, 127, -50, 50)]

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()

tem1 = image.Image("/sd/3.jpg")
tem1 = tem1.to_grayscale()
#加载模板图片
tem2 = image.Image("/sd/4.jpg")
tem2 = tem2.to_grayscale()
tem3 = image.Image("/sd/5.jpg")
tem3 = tem3.to_grayscale()
tem4 = image.Image("/sd/6.jpg")
tem4 = tem4.to_grayscale()

while(True):
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs(thrr, pixels_threshold=700, area_threshold=700,merge=True):
        img1 = img.to_grayscale()
        r1 = img1.find_template(tem1, 0.73, step=4, search=SEARCH_EX)
        if r1:
            img.draw_rectangle(r1, color=0)
            print(1) #打印模板名字
        r4 = img1.find_template(tem4, 0.76, step=4, search=SEARCH_EX)
        if r4:
            img.draw_rectangle(r4, color=0)
            print(4) #打印模板名字

    for blob in img.find_blobs(thrb, pixels_threshold=700, area_threshold=700,merge=True):
        img2 = img.to_grayscale()
        r2 = img2.find_template(tem2, 0.55, step=4, search=SEARCH_EX)
        if r2:
            img.draw_rectangle(r2, color=0)
            print(2) #打印模板名字
        r3 = img2.find_template(tem3, 0.77, step=4, search=SEARCH_EX)
        if r3:
            img.draw_rectangle(r3, color=0)
            print(3) #打印模板名字



