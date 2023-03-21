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
        if len(bullets) < ai_settings.bullets_allowed:
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
    available_space_x = ai_settings.screen_width -2 * alien_width
    number_aliens_x = int(available_space_x/(2 * alien_width))
    return number_aliens_x
 
def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows we can fit on the screen"""
    available_space_y = (ai_settings.screen_height - 
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
                    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)    

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""    
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
        
    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)
                
def update_bullets(aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    bullets.update()
    
    # Get rid of old bullets
    for bullet in bullets.copy():
        bullets.remove(bullet)       
    
    # Check if bullets hit aliens and remove alien if so.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Redraw the screen during each pass through the loop."""
    screen.fill(ai_settings.bg_color)
    
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def check_fleet_edges(ai_settings, aliens):
    """Respond to aliens reaching edge by changing direction."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
            
def change_fleet_direction(ai_settings, aliens):
    """Finish the direction change and drop aliens."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    """Check for edge collisions and change direction before updating aliens."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    

    