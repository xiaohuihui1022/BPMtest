import pygame
import sys
from pygame.locals import *

# 初始化pygame，让程序正常运行。
pygame.init()
# 运用set_mode函数来创建一个大小为500×500像素大小的窗口，变量名为screen。
screen = pygame.display.set_mode([500, 500])
# 设置标题
pygame.display.set_caption('灰灰自制BPM测试机')


def draw(content):
    pygame.font.init()
    # pygame.font.Font（字体，大小）
    font = pygame.font.Font(r"C:\windows\Fonts\msyhbd.ttf", 32)
    text_sf = font.render(content, False, pygame.Color(255, 255, 255), pygame.Color(0, 0, 0))
    return text_sf
    # font.render参数意义：.render（内容，是否抗锯齿，字体颜色，字体背景颜色）


def timer(times):
    tick = pygame.time.Clock()
    press = 0
    while True:
        tick.tick(60)   # 锁帧60
        for event2 in pygame.event.get():
            if event2.type == pygame.KEYDOWN:
                if event2.key == K_x:
                    press += 1
        # time.sleep(1)
        times -= 1
        screen.blit(draw("时间还剩:" + str(times) + "tick(60tick为一秒)           "), (1, 1))
        screen.blit(draw("狂按X就对了"), (1, 50))
        pygame.display.update()
        # print(times)
        if times == 0:
            return press


screen.blit(draw("按下“k”键开始测试"), (1, 1))

while True:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # 判断是否按下按键
            if event.key == K_k:
                # screen.blit(draw("您有5秒的时间测试！"), (1, 1))
                # time.sleep(3000)
                returnPress = timer(300)
                screen.blit(draw("测试完成! 结果为：" + str(returnPress / 5 * 15) + "BPM"), (1, 1))
                screen.blit(draw("CPS结果为：" + str(returnPress / 5) + "CPS"), (1, 50))
                screen.blit(draw("按'q'键退出"), (1, 100))
            if event.key == K_q:
                sys.exit()
