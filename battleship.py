import pygame
import random

from pygame.constants import QUIT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Размер клетки
block_size = 30
# Отступ слева
left_margin = 40
# Отступ сверху
upper_margine = 50

# Размер окна
size = (left_margin + 30 * block_size, upper_margine + 15 * block_size)

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Battleship")

# Размер шрифта
font_size = int(block_size // 2)
# Шрифт
font = pygame.font.SysFont('Lucida Console', font_size)

def draw_grid():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in range(11):
        # Игрок
        pygame.draw.line(screen, BLACK, (left_margin, upper_margine + i * block_size), 
                         (left_margin + 10 * block_size, upper_margine + i * block_size), 1)
        pygame.draw.line(screen, BLACK, (left_margin + i * block_size, upper_margine), 
                         (left_margin + i * block_size, upper_margine + 10 * block_size), 1)

        # Компьютер
        pygame.draw.line(screen, BLACK, (left_margin + 15 * block_size, upper_margine + i * block_size), 
                         (left_margin + 25 * block_size, upper_margine + i * block_size), 1)
        pygame.draw.line(screen, BLACK, (left_margin + (i + 15) * block_size, upper_margine), 
                         (left_margin + (i + 15) * block_size, upper_margine + 10 * block_size), 1)
        
        if i < 10:
            num_ver = font.render(str(i + 1), True, BLACK)
            letters_hor = font.render(letters[i], True, BLACK)
            
            num_ver_width = num_ver.get_width()
            num_ver_height = num_ver.get_height()
            letters_hor_width = letters_hor.get_width()
            
            # Вертикальные цифры на первой сетке
            screen.blit(num_ver, (left_margin - (block_size // 2 + num_ver_width // 2), 
                                  upper_margine + i * block_size + (block_size // 2 - num_ver_width // 2)))
            # Горизонтальные буквы на первой сетке
            screen.blit(letters_hor, (left_margin + i * block_size + (block_size // 2 - letters_hor_width // 2), 
                                      upper_margine - (block_size // 2 + num_ver_height // 2)))
            # Вертикальные цифры на второй сетке
            screen.blit(num_ver, (left_margin - (block_size // 2 + num_ver_width // 2) + 15 * block_size, 
                                  upper_margine + i * block_size + (block_size // 2 - num_ver_width // 2)))
            # Горизонтальные буквы на второй сетке
            screen.blit(letters_hor, (left_margin + i * block_size + (block_size // 2 - letters_hor_width // 2) + 15 * block_size, 
                                      upper_margine - (block_size // 2 + num_ver_height // 2)))


def main():
    game_over = False
    screen.fill(WHITE)
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        
        draw_grid()        
        pygame.display.update()        
                
if __name__ == "__main__":                
    main()
    pygame.quit()