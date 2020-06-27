import pygame
from pygame.locals import *
import sys

def play_tank():
    pygame.init()  #任何Pygame程序均需要执行此句执行模块初始化

    window_size = (width, height) = (600, 400) #设置窗口大小
    speed = [1, 1] #移动量，值越大，速度越快
    color_black = (255, 255, 255) #RGB白色背景色
    screen = pygame.display.set_mode(window_size) #窗口模式

    pygame.display.set_caption('Freedom Move Tank') #窗口标题
    tank_image = pygame.image.load('D:\\PycharmProjects\\PythonOne\\src\\pygame\\tankU.bmp')

    tank_rect = tank_image.get_rect() #图片区域形状

    #无线循环，直到窗口关闭事件触发
    while True:
        for event in pygame.event.get():  # 处理事件

            # 接收到窗口关闭事件
            if event.type == QUIT:
                pygame.quit()  # 退出
                sys.exit()

        tank_rect = tank_rect.move(speed)

        if (tank_rect.left < 0) or (tank_rect.right > width): #水平方向
            speed[0] =- speed[0]

        if (tank_rect.top < 0) or (tank_rect.bottom > height): #垂直方向
            speed[1] =- speed[1]

        screen.fill(color_black) #填充背景
        screen.blit(tank_image, tank_rect) #窗口surface指定区域tank_rect上绘制坦克

        # 将surface对象绘制在屏幕上
        pygame.display.update()

if __name__ == "__main__":
    play_tank()