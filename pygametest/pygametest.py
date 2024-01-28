from time import sleep
import pygame
import random
from tkinter import *
import sys,math
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
'''
推荐设置                         
setting = {
    "屏幕宽度":800,
    "屏幕高度":600,
    "导弹生成间隔秒数":1,
    "云生成间隔秒数":1,
    "导弹最小速度":10,
    "导弹最大速度":20,
    "云速度":5
}
新手设置
setting = {
    "屏幕宽度":800,
    "屏幕高度":600,
    "导弹生成间隔秒数":1,
    "云生成间隔秒数":1,
    "导弹最小速度":1,
    "导弹最大速度":10,
    "云速度":5
}
老手设置
setting = {
    "屏幕宽度":800,
    "屏幕高度":600,
    "导弹生成间隔秒数":1,
    "云生成间隔秒数":1,
    "导弹最小速度":20,
    "导弹最大速度":30,
    "云速度":5
}
'''
def tkmain(assembly,window):
    for i in assembly:
        assembly[i].pack()
    window.mainloop()



def startgame(setting):
    class Cloud(pygame.sprite.Sprite):
        def __init__(self):
            super(Cloud, self).__init__()
            self.surf = pygame.image.load("cloud.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(setting["屏幕宽度"] + 20, setting["屏幕宽度"] + 100),
                    random.randint(0, setting["屏幕高度"]),
                )
            )
        def update(self):
            self.rect.move_ip(-setting["云速度"], 0)
            if self.rect.right < 0:
                self.kill()
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.image.load("missile.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(setting["屏幕宽度"] + 20, setting["屏幕宽度"] + 100),
                    random.randint(0, setting["屏幕高度"]),
                )
            )
            self.speed = random.randint(setting["导弹最小速度"], setting["导弹最大速度"])
        def update(self):
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                self.kill()
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.surf = pygame.image.load("jet.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
        def update(self, pressed_keys):
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -10)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 10)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-10, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(10, 0)
    pygame.init()
    screen = pygame.display.set_mode((setting["屏幕宽度"], setting["屏幕高度"]))
    ADDENEMY = pygame.USEREVENT + 1
    ADDCLOUD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCLOUD, setting["云生成间隔秒数"]*1000)
    pygame.time.set_timer(ADDENEMY, math.ceil(setting["导弹生成间隔秒数"])*1000)
    player = Player()
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDCLOUD:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        clouds.update()
        screen.fill((135, 206, 250))
        enemies.update()
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        screen.blit(player.surf, player.rect)
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False


        pygame.display.flip()
        clock.tick(30)
    sys.exit()
    return
def start():

    if v.get() == 1:
        setting = {
            "屏幕宽度":800,
            "屏幕高度":600,
            "导弹生成间隔秒数":1,
            "云生成间隔秒数":1,
            "导弹最小速度":1,
            "导弹最大速度":1,
            "云速度":5
        }
    elif v.get == 2:
        setting = {
            "屏幕宽度":800,
            "屏幕高度":600,
            "导弹生成间隔秒数":1,
            "云生成间隔秒数":1,
            "导弹最小速度":10,
            "导弹最大速度":20,
            "云速度":5
        }
    elif v.get() == 3:
        setting = {
            "屏幕宽度":800,
            "屏幕高度":600,
            "导弹生成间隔秒数":0.1,
            "云生成间隔秒数":1,
            "导弹最小速度":40,
            "导弹最大速度":50,
            "云速度":5
        }
    else:
        setting = {
            "屏幕宽度":int(assembly["entry1"].get()),
            "屏幕高度":int(assembly["entry2"].get()),
            "导弹生成间隔秒数":int(assembly["entry3"].get()),
            "云生成间隔秒数":int(assembly["entry4"].get()),
            "导弹最小速度":int(assembly["entry5"].get()),
            "导弹最大速度":int(assembly["entry6"].get()),
            "云速度":int(assembly["entry7"].get())
        }
    startgame(setting)
window = Tk()
v = IntVar()
v.set(4)
assembly={}
assembly["lable1"] = Label(window,text="屏幕宽度")
assembly["entry1"] = Entry(window)
assembly["lable2"] = Label(window,text="屏幕高度")
assembly["entry2"] = Entry(window)
assembly["lable3"] = Label(window,text="导弹生成间隔秒数")
assembly["entry3"] = Entry(window)
assembly["lable4"] = Label(window,text="云生成间隔秒数")
assembly["entry4"] = Entry(window)
assembly["lable5"] = Label(window,text="导弹最小速度")
assembly["entry5"] = Entry(window)
assembly["lable6"] = Label(window,text="导弹最大速度")
assembly["entry6"] = Entry(window)
assembly["lable7"] = Label(window,text="云速度")
assembly["entry7"] = Entry(window)
assembly["dx1"] = Radiobutton(window,text="我是新手",variable=v,value=1)
assembly["dx2"] = Radiobutton(window,text="我是正常人",variable=v,value=2)
assembly["dx3"] = Radiobutton(window,text="我是老手",variable=v,value=3)
assembly["dx4"] = Radiobutton(window,text="自定义",variable=v,value=4)
assembly["button1"] = Button(window,text="开始游戏",command=start)
tkmain(assembly,window)

