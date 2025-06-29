from pygame import * 
from Spriteclass2 import Player

''' colors '''
background = (200, 255, 255)

'''var'''
width = 600
height = 500


window = display.set_mode( (width, height) )


clock = time.Clock()

rocket1 = Player(player_image='rocket.png', 
                 player_x=20, player_y=200,
                 player_speed=4, width=50, height=150)

rocket2 = Player(player_image='rocket.png', 
                 player_x=525, player_y=200,
                 player_speed=4, width=50, height=150)

ball_spd = 1

ball = Player(player_image='ball.png', 
                 player_x=200, player_y=200,
                 player_speed=ball_spd, width=50, height=50)


font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSES!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSES!', True, (180, 0, 0))

global finish
run = True
finish = True
ball_speed_x = 5
ball_speed_y = 5

while run :

    if finish == True:

        window.fill(background)

        rocket1.reset(window=window)
        rocket1.update_left()

        rocket2.reset(window=window)
        rocket2.update_right()

        ball.reset(window=window)

        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if ball.rect.y > 500-45 or ball.rect.y < -50:
            ball_speed_y *= -1           
             
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            ball_speed_x *= -1
            ball_spd += 5

        # home works
        ## losing condition
        if ball.rect.x >600:
            finish = False
            window.blit(lose2,(200,200))
        if ball.rect.x < 0-50:  
            finish = False
            window.blit(lose1,(200,200))

        ## reset game play
        key_pressed = key.get_pressed()
        if key_pressed[K_r] and finish == False:
            ball.player_x = 200
            ball.player_y = 200
            rocket1.player_x = 20     
            rocket1.player_y = 200  
            rocket2.player_x = 525
            rocket2.player_y = 200   
            finish = True 

    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(60)