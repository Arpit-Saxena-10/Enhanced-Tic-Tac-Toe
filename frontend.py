import pygame

WIDTH, HEIGHT, FPS = 600, 600, 60
BG_COLOR = (28,170,156)
LINE_COLOR, LINE_WIDTH = (23,145,135), 15
# CIRCLE_COLOR, CIRCLE_WIDTH = (239,231,200), 50
# CIRCLE2_COLOR, CIRCLE2_WIDTH = (66,66,66), 50
CIRCLE_COLOR, CIRCLE_WIDTH = (255,255,255), 50
CIRCLE2_COLOR, CIRCLE2_WIDTH = (00,0,0), 50

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Enhanced Tic Tac Toe')
screen.fill(BG_COLOR)

def draw_board():

    n = 3
    for i in range(1,n):   # n-1 horizontal lines
        pygame.draw.line(screen,LINE_COLOR,(0,i*HEIGHT/n),(WIDTH,i*HEIGHT/n),LINE_WIDTH)
    for i in range(1, n):  # n-1 vertical lines
        pygame.draw.line(screen, LINE_COLOR, (i * WIDTH/n,0), (i * WIDTH / n,HEIGHT), LINE_WIDTH)
    pygame.draw.circle(screen,CIRCLE_COLOR,(300,300),50,CIRCLE_WIDTH)
    pygame.draw.circle(screen, CIRCLE2_COLOR, (500, 300), 50, CIRCLE2_WIDTH)
    pygame.display.update()

    pass



def main():
    run = True
    draw_board()
    while run:
        clock = pygame.time.Clock()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

if __name__ == "__main__":
    main()