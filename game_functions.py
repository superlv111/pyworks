import pygame
import sys
import json

from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep
from ship import Ship
from button import Button
from scoreboard import ScoreBoard

def fire_bullet(ship,screen,bullets,ai_settings):
    """开火"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(screen,ai_settings,ship)
        bullets.add(new_bullet)

def check_keydown_events(event,ship,screen,ai_settings,bullets,stats,aliens,
    scoreboard):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    # 创建子弹
    elif event.key == pygame.K_SPACE:
        if stats.game_active:
            fire_bullet(ship,screen,bullets,ai_settings)
    # 添加开始和关闭游戏的方式
    elif event.key == pygame.K_ESCAPE:
        with open('highscore.txt','w') as f_obj:
            f_obj.write(str(stats.high_score))
        sys.exit()
    elif event.key == pygame.K_RETURN:
        if not stats.game_active:
            start_game(stats,aliens,bullets,ship,screen,ai_settings,scoreboard)

def check_keyup_events(event,ship):
    """响应松开按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False

def check_events(play_button,stats,ai_settings,aliens,bullets,ship,screen,
    scoreboard):
    """监视鼠标键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('highscore.txt','w') as f_obj:
                f_obj.write(str(stats.high_score))
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,screen,ai_settings,bullets,
                stats,aliens,scoreboard)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button,stats,mouse_x,mouse_y,
                ai_settings,aliens,bullets,ship,screen,scoreboard)

def check_play_button(play_button,stats,mouse_x,mouse_y,ai_settings,
    aliens,bullets,ship,screen,scoreboard):
    """检查是否点击开始按钮"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        start_game(stats,aliens,bullets,ship,screen,ai_settings,scoreboard)

def start_game(stats,aliens,bullets,ship,screen,ai_settings,scoreboard):
    "开始游戏"
    # 鼠标非活动
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True
    scoreboard.prep_score()
    scoreboard.prep_high_score()
    scoreboard.prep_level()
    scoreboard.prep_left_ships()
    # 重置游戏状态
    aliens.empty()
    bullets.empty()
    create_fleet(aliens,screen,ai_settings,ship)
    ship.center_ship()
    ai_settings.initialize_dynamic_settings()


def update_screen(ship,screen,ai_settings,bullets,aliens,stats,play_button,
    scoreboard):
    """更新屏幕"""
    # 重绘背景色
    screen.fill(ai_settings.bg_color)
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    # for alien in aliens.sprites():
    #     alien.blitme()
    aliens.draw(screen)
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示记分牌
    scoreboard.draw_scoreboard()
    # 如果游戏非活动，创建play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 绘制最新的屏幕
    pygame.display.flip()


def update_bullets(bullets,aliens,ai_settings,ship,screen,stats,scoreboard):
    """更新子弹位置，删除多余子弹"""
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullets_aliens_collisions(aliens,bullets,ai_settings,ship,screen,
        stats,scoreboard)

def check_bullets_aliens_collisions(aliens,bullets,ai_settings,ship,screen,
    stats,scoreboard):
    # 检测碰撞并删除元素
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    # 计分
    if collisions:
        stats.score += (ai_settings.alien_points*
            len(list(collisions.values())[0]))
        scoreboard.prep_score()
        check_high_score(stats,scoreboard)
    # 检查外星人是否被完全消灭
    if len(aliens) == 0:
        stats.level += 1
        scoreboard.prep_level()
        bullets.empty()
        create_fleet(aliens,screen,ai_settings,ship)
        ship.center_ship
        ai_settings.increase_game_pace()

def check_high_score(stats,scoreboard):
    """检查是否产生了最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()

def create_fleet(aliens,screen,ai_settings,ship):
    """创建一群外星人"""
    alien = Alien(ai_settings,screen)
    number_of_aliens_x = get_number_of_aliens_x(ai_settings,alien.rect.width)
    number_of_rows = get_number_of_rows(ai_settings,alien.rect.height,
        ship.rect.height)

    for row in range(number_of_rows):
        for number in range(number_of_aliens_x):
            create_alien(ai_settings,screen,aliens,number,row)

def get_number_of_aliens_x(ai_settings,alien_width):
    """计算每行几个"""
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_of_aliens_x = int(available_space_x / (2*alien_width))
    return number_of_aliens_x

def get_number_of_rows(ai_settings,alien_height,ship_height):
    """计算可排多少行"""
    available_space_y = (ai_settings.screen_height
        - 3*alien_height - ship_height)
    number_of_rows = int(available_space_y / (2*alien_height))
    return number_of_rows

def create_alien(ai_settings,screen,aliens,number,row):
    """生成并排列外星人"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2*alien_width*number
    alien.y = alien_height + 2*alien_height*row
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)
    

def update_aliens(ai_settings,aliens,ship,bullets,screen,stats,scoreboard):
    """更新外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats,ai_settings,aliens,bullets,ship,screen,scoreboard) 
    check_aliens_bottom(screen,aliens,stats,ai_settings,bullets,
        ship,scoreboard)
    # 使鼠标重新可见
    if not stats.game_active:
        pygame.mouse.set_visible(True)

def check_fleet_edges(ai_settings,aliens):
    """外星人到边缘时采取的措施"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings,aliens)
            break
        
def change_fleet_direction(ai_settings,aliens):
    """触边转向"""
    ai_settings.fleet_direction *= -1
    for alien in aliens.sprites():
        alien.y += ai_settings.fleet_drop_speed
        alien.rect.y = alien.y

def ship_hit(stats,ai_settings,aliens,bullets,ship,screen,scoreboard):
    """飞船和外星人碰撞"""
    if stats.ship_left > 1:
        # 飞船数减一
        stats.ship_left -= 1
        scoreboard.prep_left_ships()
        # 清空子弹和外星人
        aliens.empty()
        bullets.empty()
        # 创建新的外星人和飞船
        create_fleet(aliens,screen,ai_settings,ship)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(screen,aliens,stats,ai_settings,bullets,ship,
    scoreboard):
    """检查敌人是否到达底边"""
    # 以和外星人相撞的方式处理
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom > screen_rect.bottom:
            ship_hit(stats,ai_settings,aliens,bullets,ship,screen,scoreboard)
            break