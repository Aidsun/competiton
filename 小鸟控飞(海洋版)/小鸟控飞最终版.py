import pygame
import random
import sys

# 游戏初始化
pygame.init()
# 屏幕大小
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
#加载字体
font1 = pygame.font.Font("font\猫啃珠圆体.ttf", 36)
font2  = pygame.font.Font("font\演示悠然小楷.ttf",60)
# 加载图片素材
bird_image = pygame.image.load("image\蓝色小鸟.png")
pipe_image = pygame.image.load("image\柱子.png")
background_image = pygame.image.load("image\背景图片.png")
sound_1 = pygame.image.load("image\允许播放.png")
sound_0 = pygame.image.load("image\不允播放.png")
title_image = pygame.image.load("image\标题.png")
start_game = pygame.image.load("image\开始游戏.png")
gameover_image = pygame.image.load("image\游戏结算画面.png")
confirm_image = pygame.image.load("image\确认按钮.png")
exit_image = pygame.image.load("image\退出图标.png")
# 载入游戏图标
icon = pygame.image.load("image\图标.ico")
pygame.display.set_icon(icon)
#加载音效
pygame.mixer.init()
pygame.mixer.music.load("sound\背景音乐.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
gameover_sound = pygame.mixer.Sound("sound\游戏结束音乐.ogg")
gameover_sound.set_volume(0.4)

# 颜色定义
white = (255, 255, 255)
orange = (249, 236, 195)
#创建小鸟类
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y): 
        super().__init__()
        self.image = bird_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 0
    def update(self):
        self.speed += 0.8
        self.rect.y += self.speed
    def jump(self):
        self.speed = -8

# 创建管道类
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, inverted=False):
        super().__init__()
        self.image = pipe_image
        self.rect = self.image.get_rect()
        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y)
        else:
            self.rect.topleft = (x, y)

    def update(self):
        self.rect.x -= 3

# 音乐播放决策
def music_button(sound_key):
    if sound_key==1:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

# 开始界面函数
def start_screen():
    # 设置开始界面屏幕尺寸
    MainScreen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
    # 设置标题
    pygame.display.set_caption("小鸟控飞")
    # 设置屏幕刷新频率
    clock = pygame.time.Clock()
    # 加载背景图片
    background = background_image
    # 加载游戏标题图片
    title_text = title_image
    title_rect = title_text.get_rect()
    title_rect.center = (width // 2, height // 2 - 300)
    # 加载游戏开始按钮
    start_button = start_game
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (width // 2, height // 2 + 100)
    # 加载退出游戏按钮
    exit_image_rect = exit_image.get_rect()
    exit_image_rect.center = (width -50, height-50)
    # 加载音乐播放按钮
    sound_rect = sound_1.get_rect()
    sound_rect.center = (width -150, height-50)
    sound_key = 1  #1代表允许播放，0代表不允许播放
    # 加载小鸟放在屏幕上，以便于游戏过渡
    bird1 = Bird(width // 4, height // 2)

    # 将各种元素放在屏幕上
    MainScreen.blit(background, (0, 0))
    MainScreen.blit(title_text, title_rect)
    MainScreen.blit(start_button, start_button_rect)
    MainScreen.blit(sound_1, sound_rect)
    MainScreen.blit(exit_image, exit_image_rect)
    MainScreen.blit(bird1.image, bird1.rect)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()                    
            if event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos):
                    running = False
                    main()
            if event.type == pygame.MOUSEBUTTONDOWN and sound_rect.collidepoint(event.pos) and event.button==1:
                if sound_key==1:
                    music_button(sound_key)
                    sound_key=0
                    MainScreen.blit(sound_1, sound_rect)
                    pygame.display.flip()
                else:
                    music_button(sound_key)
                    sound_key=1
                    MainScreen.blit(sound_0, sound_rect)
                    pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and exit_image_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        clock.tick(60)


# 主函数
def main():
    MainScreen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("小鸟控飞")
    clock = pygame.time.Clock()

    # 创建小鸟组、管道组、精灵族
    bird_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    # 管道之间的间隔
    pipe_space = 250

    # 实例化小鸟对象
    bird = Bird(width // 4, height // 2)
    bird_group.add(bird)
    all_sprites.add(bird)
    
    # 初始化三对管道，以便进场
    pipe1 = Pipe(width, height//2, False)
    pipe2 = Pipe(width, height//2-200, True)
    pipe3 = Pipe(width+600, height//2, False)
    pipe4 = Pipe(width+600, height//2-180, True)
    pipe5 = Pipe(width+1200, height//2+50, False)
    pipe6 = Pipe(width+1200, height//2-130, True)    
    pipe_group.add(pipe1)
    pipe_group.add(pipe2)
    pipe_group.add(pipe3)
    pipe_group.add(pipe4)
    pipe_group.add(pipe5)
    pipe_group.add(pipe6)
    all_sprites.add(pipe1)
    all_sprites.add(pipe2) 
    all_sprites.add(pipe3) 
    all_sprites.add(pipe4)
    all_sprites.add(pipe5)
    all_sprites.add(pipe5)
    all_sprites.add(pipe6)

    # 背景后移效果
    
    #添加标题，开始按钮等

    # 运行状态
    running = True
    score = 0
    
    # 游戏结束界面函数
    def game_over_screen(score):
        # 加载游戏结束界面的背景图片、得分信息、重新开始按钮等元素
        background = gameover_image
        background_rect=background.get_rect()
        background_rect.center = (width // 2, height // 2)
        score_text = font2.render("分数{:0.0f}".format(score), True, orange)
        score_rect = score_text.get_rect()
        score_rect.center = (width // 2, height // 2 )
        restart_button = confirm_image
        restart_button_rect = restart_button.get_rect()
        restart_button_rect.center = (width // 2, height // 2 + 200)
        gameover_sound.play()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button_rect.collidepoint(event.pos):                        
                        running = False
                        start_screen()
                        

            MainScreen.blit(background, background_rect)
            MainScreen.blit(score_text, score_rect)
            MainScreen.blit(restart_button, restart_button_rect)

            pygame.display.flip()

    # 设置背景图像的初始位置
    bg_x1 = 0
    bg_x2 = background_image.get_width()
    bg_speed = 2
    # 游戏运行主体
    while running:
        # 遍历各种事件
        for event in pygame.event.get():
            # 游戏退出
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            #小鸟跳跃的两种方式
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bird.jump()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
        # 小鸟和管道更新
        bird.update()
        pipe_group.update()
        # 背景移动
        bg_x1 -= bg_speed
        bg_x2 -= bg_speed
        # 当第一张背景移出窗口左侧时，将其放置到第二张背景右侧
        if bg_x1 <= -background_image.get_width():
            bg_x1 = background_image.get_width()

    # 当第二张背景移出窗口左侧时，将其放置到第一张背景右侧
        if bg_x2 <= -background_image.get_width():
            bg_x2 = background_image.get_width()  
        MainScreen.blit(background_image, (bg_x1, 0))
        MainScreen.blit(background_image,(bg_x2, 0))         
        # 小鸟碰撞,掉落,飞出屏幕检测
        hit_pipe = pygame.sprite.spritecollide(bird, pipe_group, False)
        if hit_pipe or bird.rect.bottom >= height:
            running = False
            game_over_screen(score)
        if bird.rect.top <= 0:
            bird.rect.top = 0
            bird.speed = 0
            bird.rect.y = 0
            bird.rect.x = width // 4
            running = False
            game_over_screen(score)
        if bird.rect.bottom >= height:
            bird.rect.bottom = height
            bird.speed = 0
            bird.rect.y = height
            bird.rect.x = width // 4
            running = False
            game_over_screen(score)
    # 删除移出屏幕的管道，同时生成新的管道
        for pipe in pipe_group:
            # 加分功能
            if bird.rect.centerx > pipe.rect.centerx and bird.rect.centerx < pipe.rect.centerx + 100:
                score += 1/66
            if pipe.rect.right < 0:
                pipe.kill()
                if len(pipe_group) < 6:
                    new_pipe = Pipe(width, random.randint(pipe_space, height - pipe_space))
                    new_inverted_pipe = Pipe(width, new_pipe.rect.y - pipe_space, inverted=True)
                    pipe_group.add(new_pipe)
                    pipe_group.add(new_inverted_pipe)
                    all_sprites.add(new_pipe)
                    all_sprites.add(new_inverted_pipe)
        # 渲染小鸟和管道
        all_sprites.draw(MainScreen)
        # 显示分数
        score_text = font1.render("分数{:0.0f}".format(score), True, white)
        score_rect = score_text.get_rect()
        score_rect.center = (width // 2, 50)
        MainScreen.blit(score_text, score_rect)

        # 刷新屏幕
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()  
if __name__ == "__main__":
    start_screen()

