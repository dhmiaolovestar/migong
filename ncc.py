import time, sensor, image
from image import SEARCH_EX, SEARCH_DS

# Reset sensor
sensor.reset()

# Set sensor settings
sensor.set_contrast(1)
sensor.set_gainceiling(16)
# Max resolution for template matching with SEARCH_EX is QQVGA
sensor.set_framesize(sensor.QQVGA)
# You can set windowing to reduce the search image.
#sensor.set_windowing(((640-80)//2, (480-60)//2, 80, 60))
sensor.set_pixformat(sensor.GRAYSCALE)

# Load template.
# Template should be a small (eg. 32x32 pixels) grayscale image.
tem1 = image.Image("/sd/3.jpg")
tem1 = tem1.to_grayscale()
#加载模板图片
tem2 = image.Image("/sd/4.jpg")
tem2 = tem2.to_grayscale()
tem3 = image.Image("/sd/5.jpg")
tem3 = tem3.to_grayscale()
tem4 = image.Image("/sd/6.jpg")
tem4 = tem4.to_grayscale()
clock = time.clock()

# Run template matching
while (True):
    clock.tick()
    img = sensor.snapshot()
    r1 = img.find_template(tem1, 0.70, step=4, search=SEARCH_EX)
    #find_template(template, threshold, [roi, step, search]),threshold中
    #的0.7是相似度阈值,roi是进行匹配的区域（左上顶点为（10，0），长80宽60的矩形），
    #注意roi的大小要比模板图片大，比frambuffer小。
    #把匹配到的图像标记出来
    if r1:
        img.draw_rectangle(r1)
        print(1)
    r2 = img.find_template(tem2, 0.65, step=4, search=SEARCH_EX)
    if r2:
        img.draw_rectangle(r2)
        print(2)
    r3 = img.find_template(tem3, 0.84, step=4, search=SEARCH_EX)
    if r3:
        img.draw_rectangle(r3)
        print(3)
    r4 = img.find_template(tem4, 0.65, step=4, search=SEARCH_EX)
    if r4:
        img.draw_rectangle(r4)
        print(4)


