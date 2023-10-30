import pygame
import random
import sys
import numpy
import time
import itertools

pygame.init()
width,height=pygame.display.Info().current_w,pygame.display.Info().current_h
screen=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
screen.fill((255,255,255))
pygame.display.set_caption("定神方格小游戏")
icon=pygame.image.load("image/图标/小狗.jpg")
pygame.display.set_icon(icon)
pygame.mixer.music.load("sound/背景音乐.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
error_sound=pygame.mixer.Sound("sound/错误提示音.ogg")
clock = pygame.time.Clock()
clock.tick(120)
                    
def five_five():
    width,height=pygame.display.Info().current_w,pygame.display.Info().current_h
    screens=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
    background_image=pygame.image.load("image/背景图片/背景图片.jpg")
    background_image=pygame.transform.scale(background_image,(width,height))
    screens.blit(background_image,(0,0))

    time_start=time.time()
    max_score=100
    max_time=360
    X=[(i*width*0.097)+width*0.25 for i in range(5)]
    Y=[(i*height*0.163) +height*0.09 for i in range(5)]
    map=numpy.array(list(itertools.product(X,Y)))
    list1=[[i] for i in range(25)]    
    random.shuffle(list1)
    pic_count=1
    number=0
    music_on=True
    help_on=False
    while True:

        for event in pygame.event.get():
            while pic_count:
                for i in range(25):
                    screen.blit(pygame.image.load("image/点击前/five_five/pr"+str(*list1[i-1])+".png"),map[i])
                pic_count=0
            menu_image=pygame.image.load("image\图标\返回主页.png")
            menu_rect=menu_image.get_rect()
            menu_rect.x,menu_rect.y=(width*0.946),(height*0.024)
            screens.blit(menu_image,menu_rect)
            sound_button_iamge1=pygame.image.load("image\图标\允许播放.png").convert_alpha()
            sound_button_rect1=sound_button_iamge1.get_rect()
            sound_button_iamge1.set_alpha(255)
            sound_button_rect1.x,sound_button_rect1.y=(width*0.878),(height*0.024)
            screens.blit(sound_button_iamge1,sound_button_rect1)
            sound_button_iamge2=pygame.image.load("image\图标\不允播放.png").convert_alpha()
            sound_button_rect2=sound_button_iamge2.get_rect()
            sound_button_rect2.x,sound_button_rect2.y=(width*0.878),(height*0.024)
            pos=pygame.mouse.get_pos()
            if menu_rect.collidepoint(pos):
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    pygame.mixer.music.unpause()
                    pygame.display.update()
                    return 0
            if sound_button_rect1.collidepoint(pos) or sound_button_rect2.collidepoint(pos):
                
                if event.type==pygame.MOUSEBUTTONDOWN  and event.button==1: 
                
                    music_on=not music_on
                    if music_on:
                        screens.blit(sound_button_iamge1,sound_button_rect1)
                        sound_button_iamge1.set_alpha(255)
                        sound_button_iamge2.set_alpha(0)
                        pygame.mixer.music.unpause()
                        pygame.display.flip()
                    else:
                        screens.blit(sound_button_iamge2,sound_button_rect2)
                        sound_button_iamge1.set_alpha(0)
                        sound_button_iamge2.set_alpha(255)
                        pygame.mixer.music.pause()
                        pygame.display.flip()      
            else:
                if music_on:
                    screens.blit(sound_button_iamge1,sound_button_rect1)
                    pygame.display.flip()
                else:
                    screens.blit(sound_button_iamge2,sound_button_rect2)     
                    pygame.display.flip()   

            for i in range(25):
                if event.type==pygame.MOUSEBUTTONDOWN :
                    if map[i][0]<=event.pos[0]<=map[i][0]+150 and map[i][1]<=event.pos[1]<=map[i][1]+150:
                        if int(*list1[i-1]) == number:
                            screen.blit(pygame.image.load("image/点击后/five_five空白.png"),map[i])
                            number=number+1
                            time_elapsed=time.time()-time_start
                            score=int(max_score*(max_time/time_elapsed))
                            if number==25:
                                error_sound.set_volume(0)
                                time_end=time.time()
                                time_pass=time_end-time_start
                                
                                gamend_image=pygame.image.load("image/跳转按钮/游戏结束图片.png")
                                gamend_rect=gamend_image.get_rect()
                                gamend_rect.x,gamend_rect.y=(width*0.396),(height*0.321)
                                                    
                                font_1=pygame.font.Font("font\猫啃珠圆体.ttf",68)
                                font_1_text=font_1.render("{:.1f}s".format(time_pass),True,(245,65,12))
                                
                                font_2=pygame.font.Font("font\演示悠然小楷.ttf",55)
                                font_2_text=font_2.render("分数：{}".format(score),True,(0,0,0))
                                
                                screens.blit(gamend_image,gamend_rect)
                                screens.blit(font_1_text,((width*0.436),(height*0.412)))
                                screens.blit(font_2_text,((width*0.422),(height*0.49)))
                                while True:   
                                    for event in pygame.event.get():
                                        affirm_image=pygame.image.load("image\跳转按钮\游戏结束点击前.png")
                                        affirm_rect=affirm_image.get_rect()
                                        affirm_rect.x,affirm_rect.y=(width*0.455),(height*0.573)
                                        screens.blit(affirm_image,affirm_rect)
                                        pos=pygame.mouse.get_pos()
                                        if affirm_rect.collidepoint(pos):
                                            affirm_image=pygame.image.load("image\跳转按钮\游戏结束点击后.png")
                                            screens.blit(affirm_image,affirm_rect)
                                            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                                                return 0
                                        pygame.display.flip()

                        else:
                             error_sound.play()
                else:
                    pass
        
            pygame.display.flip()      
   
def six_six():
    width,height=pygame.display.Info().current_w,pygame.display.Info().current_h
    screens=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
    background_image=pygame.image.load("image/背景图片/背景图片.jpg")
    background_image=pygame.transform.scale(background_image,(width,height))
    screens.blit(background_image,(0,0))
    time_start=time.time()
    max_score=100
    max_time=720
    X=[(i*width*0.084)+width*0.23 for i in range(6)]
    Y=[(i*height*0.15) +height*0.07 for i in range(6)]
    map=numpy.array(list(itertools.product(X,Y)))
    list1=[[i] for i in range(36)]    
    random.shuffle(list1)
    pic_count=1
    number=0
    music_on=True
    help_on=False
    while True:

        for event in pygame.event.get():
            while pic_count:
                for i in range(36):
                    screen.blit(pygame.image.load("image/点击前/six_six/pr"+str(*list1[i-1])+".png"),map[i])
                pic_count=0
            menu_image=pygame.image.load("image\图标\返回主页.png")
            menu_rect=menu_image.get_rect()
            menu_rect.x,menu_rect.y=(width*0.946),(height*0.024)
            screens.blit(menu_image,menu_rect)
            sound_button_iamge1=pygame.image.load("image\图标\允许播放.png").convert_alpha()
            sound_button_rect1=sound_button_iamge1.get_rect()
            sound_button_iamge1.set_alpha(255)
            sound_button_rect1.x,sound_button_rect1.y=(width*0.878),(height*0.024)
            screens.blit(sound_button_iamge1,sound_button_rect1)
            sound_button_iamge2=pygame.image.load("image\图标\不允播放.png").convert_alpha()
            sound_button_rect2=sound_button_iamge2.get_rect()
            sound_button_rect2.x,sound_button_rect2.y=(width*0.878),(height*0.024)
            pos=pygame.mouse.get_pos()
            if menu_rect.collidepoint(pos):
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    pygame.mixer.music.unpause()
                    pygame.display.update()
                    return 0
            if sound_button_rect1.collidepoint(pos) or sound_button_rect2.collidepoint(pos):
                
                if event.type==pygame.MOUSEBUTTONDOWN  and event.button==1: 
                
                    music_on=not music_on
                    if music_on:
                        screens.blit(sound_button_iamge1,sound_button_rect1)
                        sound_button_iamge1.set_alpha(255)
                        sound_button_iamge2.set_alpha(0)
                        pygame.mixer.music.unpause()
                        pygame.display.flip()
                    else:
                        screens.blit(sound_button_iamge2,sound_button_rect2)
                        sound_button_iamge1.set_alpha(0)
                        sound_button_iamge2.set_alpha(255)
                        pygame.mixer.music.pause()
                        pygame.display.flip()      
            else:
                if music_on:
                    screens.blit(sound_button_iamge1,sound_button_rect1)
                    pygame.display.flip()
                else:
                    screens.blit(sound_button_iamge2,sound_button_rect2)     
                    pygame.display.flip()   

            for i in range(36):
                if event.type==pygame.MOUSEBUTTONDOWN :
                    if map[i][0]<=event.pos[0]<=map[i][0]+130 and map[i][1]<=event.pos[1]<=map[i][1]+130:
                        if int(*list1[i-1]) == number:
                            screen.blit(pygame.image.load("image/点击后/six_six空白.png"),map[i])
                            number=number+1
                            time_elapsed=time.time()-time_start
                            score=int(max_score*(max_time/time_elapsed))
                            if number==36:
                                error_sound.set_volume(0)
                                time_end=time.time()
                                time_pass=time_end-time_start
                                
                                gamend_image=pygame.image.load("image/跳转按钮/游戏结束图片.png")
                                gamend_rect=gamend_image.get_rect()
                                gamend_rect.x,gamend_rect.y=(width*0.396),(height*0.321)
                                                    
                                font_1=pygame.font.Font("font\猫啃珠圆体.ttf",68)
                                font_1_text=font_1.render("{:.1f}s".format(time_pass),True,(245,65,12))
                                
                                font_2=pygame.font.Font("font\演示悠然小楷.ttf",55)
                                font_2_text=font_2.render("分数：{}".format(score),True,(0,0,0))
                                
                                screens.blit(gamend_image,gamend_rect)
                                screens.blit(font_1_text,((width*0.436),(height*0.412)))
                                screens.blit(font_2_text,((width*0.422),(height*0.49)))
                                while True:   
                                    for event in pygame.event.get():
                                        affirm_image=pygame.image.load("image\跳转按钮\游戏结束点击前.png")
                                        affirm_rect=affirm_image.get_rect()
                                        affirm_rect.x,affirm_rect.y=(width*0.455),(height*0.573)
                                        screens.blit(affirm_image,affirm_rect)
                                        pos=pygame.mouse.get_pos()
                                        if affirm_rect.collidepoint(pos):
                                            affirm_image=pygame.image.load("image\跳转按钮\游戏结束点击后.png")
                                            screens.blit(affirm_image,affirm_rect)
                                            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                                                return 0
                                        pygame.display.flip()

                        else:
                             error_sound.play()
                else:
                    pass
        
            pygame.display.flip()     
def seven_seven():
    width,height=pygame.display.Info().current_w,pygame.display.Info().current_h
    screens=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
    background_image=pygame.image.load("image/背景图片/背景图片.jpg")
    background_image=pygame.transform.scale(background_image,(width,height))
    screens.blit(background_image,(0,0))
    time_start=time.time()
    max_score=100
    max_time=1080
    X=[(i*width*0.071)+width*0.23 for i in range(7)]
    Y=[(i*height*0.126) +height*0.048 for i in range(7)]
    map=numpy.array(list(itertools.product(X,Y)))
    list1=[[i] for i in range(49)]    
    random.shuffle(list1)
    pic_count=1
    number=0
    music_on=True
    help_on=False
    while True:
        for event in pygame.event.get():
            while pic_count:
                for i in range(49):
                    screen.blit(pygame.image.load("image/点击前/seven_seven/pr"+str(*list1[i-1])+".png"),map[i])
                pic_count=0
            menu_image=pygame.image.load("image\图标\返回主页.png")
            menu_rect=menu_image.get_rect()
            menu_rect.x,menu_rect.y=(width*0.946),(height*0.024)
            screens.blit(menu_image,menu_rect)
            sound_button_iamge1=pygame.image.load("image\图标\允许播放.png").convert_alpha()
            sound_button_rect1=sound_button_iamge1.get_rect()
            sound_button_iamge1.set_alpha(255)
            sound_button_rect1.x,sound_button_rect1.y=(width*0.878),(height*0.024)
            screens.blit(sound_button_iamge1,sound_button_rect1)
            sound_button_iamge2=pygame.image.load("image\图标\不允播放.png").convert_alpha()
            sound_button_rect2=sound_button_iamge2.get_rect()
            sound_button_rect2.x,sound_button_rect2.y=(width*0.878),(height*0.024)
            pos=pygame.mouse.get_pos()
            if menu_rect.collidepoint(pos):
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    pygame.mixer.music.unpause()
                    pygame.display.update()
                    return 0
            if sound_button_rect1.collidepoint(pos) or sound_button_rect2.collidepoint(pos):
                
                if event.type==pygame.MOUSEBUTTONDOWN  and event.button==1: 
                
                    music_on=not music_on
                    if music_on:
                        screens.blit(sound_button_iamge1,sound_button_rect1)
                        sound_button_iamge1.set_alpha(255)
                        sound_button_iamge2.set_alpha(0)
                        pygame.mixer.music.unpause()
                        pygame.display.flip()
                    else:
                        screens.blit(sound_button_iamge2,sound_button_rect2)
                        sound_button_iamge1.set_alpha(0)
                        sound_button_iamge2.set_alpha(255)
                        pygame.mixer.music.pause()
                        pygame.display.flip()      
            else:
                if music_on:
                    screens.blit(sound_button_iamge1,sound_button_rect1)
                    pygame.display.flip()
                else:
                    screens.blit(sound_button_iamge2,sound_button_rect2)     
                    pygame.display.flip()   
            for i in range(49):
                if event.type==pygame.MOUSEBUTTONDOWN :
                    if map[i][0]<=event.pos[0]<=map[i][0]+110 and map[i][1]<=event.pos[1]<=map[i][1]+110:
                        if int(*list1[i-1]) == number:
                            screen.blit(pygame.image.load("image/点击后/seven_seven空白.png"),map[i])
                            number=number+1
                            time_elapsed=time.time()-time_start
                            score=int(max_score*(max_time/time_elapsed))
                            if number==49:
                                error_sound.set_volume(0)
                                time_end=time.time()
                                time_pass=time_end-time_start
                                
                                gamend_image=pygame.image.load("image/跳转按钮/游戏结束图片.png")
                                gamend_rect=gamend_image.get_rect()
                                gamend_rect.x,gamend_rect.y=(width*0.396),(height*0.321)
                                                    
                                font_1=pygame.font.Font("font\猫啃珠圆体.ttf",68)
                                font_1_text=font_1.render("{:.1f}s".format(time_pass),True,(245,65,12))
                                
                                font_2=pygame.font.Font("font\演示悠然小楷.ttf",55)
                                font_2_text=font_2.render("分数：{}".format(score),True,(0,0,0))
                                
                                screens.blit(gamend_image,gamend_rect)
                                screens.blit(font_1_text,((width*0.436),(height*0.412)))
                                screens.blit(font_2_text,((width*0.422),(height*0.49)))
                                while True:   
                                    for event in pygame.event.get():
                                        affirm_image=pygame.image.load("image\跳转按钮\游戏结束点击前.png")
                                        affirm_rect=affirm_image.get_rect()
                                        affirm_rect.x,affirm_rect.y=(width*0.455),(height*0.573)
                                        screens.blit(affirm_image,affirm_rect)
                                        pos=pygame.mouse.get_pos()
                                        if affirm_rect.collidepoint(pos):
                                            affirm_image=pygame.image.load("image\跳转按钮\游戏结束点击后.png")
                                            screens.blit(affirm_image,affirm_rect)
                                            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                                                return 0
                                        pygame.display.flip()

                        else:
                             error_sound.play()
                else:
                    pass
        
            pygame.display.flip()     
def eight_eight():
    width,height=pygame.display.Info().current_w,pygame.display.Info().current_h
    screens=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
    background_image=pygame.image.load("image/背景图片/背景图片.jpg")
    background_image=pygame.transform.scale(background_image,(width,height))
    screens.blit(background_image,(0,0))
    time_start=time.time()
    max_score=100
    max_time=14460
    X=[(i*width*0.06)+width*0.25 for i in range(8)]
    Y=[(i*height*0.109) +height*0.07 for i in range(8)]
    map=numpy.array(list(itertools.product(X,Y)))
    list1=[[i] for i in range(64)]    
    random.shuffle(list1)
    pic_count=1
    number=0
    music_on=True
    help_on=False
    while True:

        for event in pygame.event.get():
            while pic_count:
                for i in range(64):
                    screen.blit(pygame.image.load("image/点击前/eight_eight/pr"+str(*list1[i-1])+".png"),map[i])
                pic_count=0
            menu_image=pygame.image.load("image\图标\返回主页.png")
            menu_rect=menu_image.get_rect()
            menu_rect.x,menu_rect.y=(width*0.946),(height*0.024)
            screens.blit(menu_image,menu_rect)
            sound_button_iamge1=pygame.image.load("image\图标\允许播放.png").convert_alpha()
            sound_button_rect1=sound_button_iamge1.get_rect()
            sound_button_iamge1.set_alpha(255)
            sound_button_rect1.x,sound_button_rect1.y=(width*0.878),(height*0.024)
            screens.blit(sound_button_iamge1,sound_button_rect1)         
            sound_button_iamge2=pygame.image.load("image\图标\不允播放.png").convert_alpha()
            sound_button_rect2=sound_button_iamge2.get_rect()
            sound_button_rect2.x,sound_button_rect2.y=(width*0.878),(height*0.024)
            pos=pygame.mouse.get_pos()
            if menu_rect.collidepoint(pos):
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    pygame.mixer.music.unpause()
                    pygame.display.update()
                    return 0
            if sound_button_rect1.collidepoint(pos) or sound_button_rect2.collidepoint(pos):
                
                if event.type==pygame.MOUSEBUTTONDOWN  and event.button==1: 
                
                    music_on=not music_on
                    if music_on:
                        screens.blit(sound_button_iamge1,sound_button_rect1)
                        sound_button_iamge1.set_alpha(255)
                        sound_button_iamge2.set_alpha(0)
                        pygame.mixer.music.unpause()
                        pygame.display.flip()
                    else:
                        screens.blit(sound_button_iamge2,sound_button_rect2)
                        sound_button_iamge1.set_alpha(0)
                        sound_button_iamge2.set_alpha(255)
                        pygame.mixer.music.pause()
                        pygame.display.flip()      
            else:
                if music_on:
                    screens.blit(sound_button_iamge1,sound_button_rect1)
                    pygame.display.flip()
                else:
                    screens.blit(sound_button_iamge2,sound_button_rect2)     
                    pygame.display.flip()   

            for i in range(64):
                if event.type==pygame.MOUSEBUTTONDOWN :
                    if map[i][0]<=event.pos[0]<=map[i][0]+100 and map[i][1]<=event.pos[1]<=map[i][1]+100:
                        if int(*list1[i-1]) == number:
                            screen.blit(pygame.image.load("image/点击后/eight_eight空白.png"),map[i])
                            number=number+1
                            time_elapsed=time.time()-time_start
                            score=int(max_score*(max_time/time_elapsed))
                            if number==64:
                                error_sound.set_volume(0)
                                time_end=time.time()
                                time_pass=time_end-time_start
                                
                                gamend_image=pygame.image.load("image/跳转按钮/游戏结束图片.png")
                                gamend_rect=gamend_image.get_rect()
                                gamend_rect.x,gamend_rect.y=(width*0.396),(height*0.321)
                                                    
                                font_1=pygame.font.Font("font\猫啃珠圆体.ttf",68)
                                font_1_text=font_1.render("{:.1f}s".format(time_pass),True,(245,65,12))
                                
                                font_2=pygame.font.Font("font\演示悠然小楷.ttf",55)
                                font_2_text=font_2.render("分数：{}".format(score),True,(0,0,0))
                                
                                screens.blit(gamend_image,gamend_rect)
                                screens.blit(font_1_text,((width*0.436),(height*0.412)))
                                screens.blit(font_2_text,((width*0.422),(height*0.49)))
                                while True:   
                                    for event in pygame.event.get():
                                        affirm_image=pygame.image.load("image\跳转按钮\游戏结束点击前.png")
                                        affirm_rect=affirm_image.get_rect()
                                        affirm_rect.x,affirm_rect.y=(width*0.455),(height*0.573)
                                        screens.blit(affirm_image,affirm_rect)
                                        pos=pygame.mouse.get_pos()
                                        if affirm_rect.collidepoint(pos):
                                            affirm_image=pygame.image.load("image\跳转按钮\游戏结束点击后.png")
                                            screens.blit(affirm_image,affirm_rect)
                                            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                                                return 0
                                        pygame.display.flip()

                        else:
                             error_sound.play()
                else:
                    pass
        
            pygame.display.flip()     
while True:
    screen_bgimage=pygame.image.load("image/背景图片/背景图片.jpg")
    screen_bgimage=pygame.transform.scale(screen_bgimage,(width,height))
    screen.blit(screen_bgimage,(0,0))
    power_image=pygame.image.load("image/背景图片/版权所有.png")
    power_rect=power_image.get_rect()
    power_rect.x,power_rect.y=(width*0.245),(height*0.927)
    screen.blit(power_image,power_rect)
    power_image=pygame.image.load("image/背景图片/游戏名称.png")
    power_rect=power_image.get_rect()
    power_rect.x,power_rect.y=(width*0.355),(height*0.057)
    screen.blit(power_image,power_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        quit_image=pygame.image.load("image/跳转按钮/退出按钮(点击前).png")
        quit_rect=quit_image.get_rect()
        quit_rect.x,quit_rect.y=(width*0.459),(height*0.785)
        screen.blit(quit_image,quit_rect)            
        five_image=pygame.image.load("image/跳转按钮/5x5难度点击前.png")
        five_rect=five_image.get_rect()
        five_rect.x,five_rect.y=(width*0.32),(height*0.350)
        screen.blit(five_image,five_rect)      
        six_image=pygame.image.load("image/跳转按钮/6x6难度点击前.png")
        six_rect=six_image.get_rect()
        six_rect.x,six_rect.y=(width*0.54),(height*0.350)
        screen.blit(six_image,six_rect)
        seven_image=pygame.image.load("image/跳转按钮/7x7难度点击前.png")
        seven_rect=seven_image.get_rect()
        seven_rect.x,seven_rect.y=(width*0.32),(height*0.55)
        screen.blit(seven_image,seven_rect)        
        eight_image=pygame.image.load("image/跳转按钮/8x8难度点击前.png")
        eight_rect=eight_image.get_rect()
        eight_rect.x,eight_rect.y=(width*0.54),(height*0.55)
        screen.blit(eight_image,eight_rect)            
        pos=pygame.mouse.get_pos()
        if quit_rect.collidepoint(pos) :
            quit_image=pygame.image.load("image/跳转按钮/退出按钮(点击后).png")
            screen.blit(quit_image,quit_rect)
            if event.type==pygame.MOUSEBUTTONDOWN  and event.button==1:
                pygame.quit()
                sys.exit()
        if five_rect.collidepoint(pos):
            five_image=pygame.image.load("image/跳转按钮/5x5难度点击后.png")
            screen.blit(five_image,five_rect)   
            if event.type==pygame.MOUSEBUTTONDOWN  and event.button==1:
                    five_five()
        if six_rect.collidepoint(pos):
            six_image=pygame.image.load("image/跳转按钮/6x6难度点击后.png")
            screen.blit(six_image,six_rect)   
            if event.type==pygame.MOUSEBUTTONDOWN  and event.button==1:
                    six_six()
        if seven_rect.collidepoint(pos):
            seven_image=pygame.image.load("image/跳转按钮/7x7难度点击后.png")
            screen.blit(seven_image,seven_rect)   
            if event.type==pygame.MOUSEBUTTONDOWN  and event.button==1:
                    seven_seven()
        if eight_rect.collidepoint(pos):
            eight_image=pygame.image.load("image/跳转按钮/8x8难度点击后.png")
            screen.blit(eight_image,eight_rect)   
            if event.type==pygame.MOUSEBUTTONDOWN  and event.button==1:
                    eight_eight()
                
        pygame.display.flip()             