import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, screen_settings, screen, ship, bullets):
    '''Keydown event action'''
    if event.key == pygame.K_RIGHT:
        # Ship move to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(screen_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    '''keyup event action'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(screen_settings, screen, ship, bullets):
    '''Respond to keyboard and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(screen_settings, screen, ship, bullets):
    '''space key down ==> new bullets if limit not reached'''
    if len(bullets) < screen_settings.bullets_allowed:
        new_bullet = Bullet(screen_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(screen_settings, screen, ship, aliens, bullets):
    '''update postion of bullets'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(screen_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(screen_settings, screen, ship, aliens, bullets):
    '''Action after bullet hitting alien'''
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # Destroy existing bullets, and create new fleet.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def check_fleet_edges(screen_settings, aliens):
    '''Action if alien reaches an edge'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(screen_settings, aliens)
            break

def change_fleet_direction(screen_settings, aliens):
    '''change the fleet's direction'''
    for alien in aliens.sprites():
        alien.rect.y += screen_settings.fleet_drop_speed
    screen_settings.fleet_direction *= -1

def ship_hit(screen_settings, stats, screen, ship, aliens, bullets):
    '''hit by alien'''
    if stats.ship_left > 0:
        stat.ship_left = -1
    else:
        stats.game_active = False
    # clear the list: aliens and bullets
    aliens.empty()
    bullets.empy()

    # new fleet and center the ship
    create_fleet(screen_settings, screen, ship, aliens)
    ship.center_ship()

    # sleep 0.5
    sleep(0.5)

def check_aliens_bottom(screen_settings, stats, screen, ship, aliens, bullets):
    '''check if reaching the bottom'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            shit_hit(screen_settings, stats, screen, aliens, bullets)
            break

def update_aliens(screen_settings, stats, screen, ship, aliens, bullets):
    '''update the positions of all aliens in the fleet'''
    check_fleet_edges(screen_settings, aliens)
    aliens.update()
    # look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(screen_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(screen_settings, stats, screen, ship, aliens, bullets)

def get_number_aliens_x(screen_settings, alien_width):
    '''calculate the nubmer of alien that fit per row'''
    available_space_x = screen_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(screen_settings, ship_height, alien_height):
    '''Determine the number of rows of aliens'''
    available_space_y = (screen_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(screen_settings, screen, aliens, alien_number, row_number):
    '''Create an alien and place it in the row.'''
    alien = Alien(screen_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(screen_settings, screen, ship, aliens):
    '''create a fleet of aliens'''
    alien = Alien(screen_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(screen_settings, alien.rect.width)
    number_rows = get_number_rows(screen_settings, ship.rect.height,
        alien.rect.height)

    # create the fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(screen_settings, screen, aliens, alien_number, row_number)

def update_screen(screen_settings, screen, ship, aliens, bullets):
    '''Update the images on the screen and refresh the images'''
    # Redraw the screen during each loop
    screen.fill(screen_settings.bg_color)

    # redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #aliens.blitme()
    aliens.draw(screen)
    pygame.display.flip()
