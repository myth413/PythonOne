import pygame
from pygame.locals import *
import sys

def hello_world():
    pygame.init()  #任何Pygame程序均需要执行此句执行模块初始化

    #设置窗口的模式，（680， 480）表示窗口宽高
    #此函数返回surface对象，本程序不使用，故未保存到对象变量中
    pygame.display.set_mode((680, 480))

    #设置窗口标题
    pygame.display.set_caption('Hello World!')

    #无线循环，直到窗口关闭事件触发
    while True:
        for event in pygame.event.get(): #处理事件

            #接收到窗口关闭事件
            if event.type == QUIT:
                pygame.quit()  #退出
                sys.exit()
        #将surface对象绘制在屏幕上
        pygame.display.update()

if __name__ == "__main__":
    hello_world()