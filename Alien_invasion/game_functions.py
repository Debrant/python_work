import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()
  
    
def check_keyup_events(event, ship):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
 
 
def check_events(ai_settings, screen, ship, bullets):
    """Respond to kepsersses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)    
def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width -2*alien_width
    number_aliens_x = int(available_space_x/(2 * alien_width))
    return number_aliens_x
                    
def create_alien(ai_settings, screen, aliens, alien_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)    

def create_fleet(ai_settings, screen, aliens, alien_number):
    """Create a full fleet of aliens."""    
    number_aliens = get_number_aliens_x(ai_settings, alien.rect.width)
    # Create the first row of aliens.
    for alien_number in range(number_aliens_x):
        # Create an alien and place it in the row.
        create_alien(ai_settings, screen, aliens, alien_number)
        
    
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Redraw the screen during each pass through the loop."""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        aliens.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()
