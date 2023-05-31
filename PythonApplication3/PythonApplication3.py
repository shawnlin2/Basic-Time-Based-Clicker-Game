
import pygame, random as r, csv
pygame.init()

'Variables'
WIDTH , HEIGHT = 600 , 600
running = True
game = True
end = False
radius = 25
score = 0
s = []
circle_x , circle_y = r.randint(radius , WIDTH- radius), r.randint(radius , HEIGHT- radius)
color = (r.randint(20 , 255),r.randint(20 , 255), r.randint(20 , 255)) 
FONT = pygame.font.SysFont("Times New Roman" , 20)

'Screen'
scr = pygame.display.set_mode((WIDTH , HEIGHT))

'Functions'
def display(s):
    global text
    s = s 
    scr.fill((0 , 0, 0))
    
    if end == True:
        text = FONT.render("Top Scores: " , 1, (255, 255 , 255))
        t1 = FONT.render('1. {}'.format(s[0]) , 1, (255, 255 , 255))
        t2 = FONT.render('2. {}'.format(s[1]) , 1, (255, 255 , 255))
        t3 = FONT.render('3. {}'.format(s[2]) , 1, (255, 255 , 255))
        t4 = FONT.render('4. {}'.format(s[3]) , 1, (255, 255 , 255))
        t5 = FONT.render('5. {}'.format(s[4]) , 1, (255, 255 , 255))
        t6 = FONT.render('Click Anywhere To Play Again' , 1, (255, 255 , 255))
        scr.blit(text , (240, 180))
        scr.blit(t1 , (240 , 200))
        scr.blit(t2 , (240 , 220))
        scr.blit(t3 , (240 , 240))
        scr.blit(t4 , (240 , 260))
        scr.blit(t5 , (240 , 280))
        scr.blit(t6 , (240 , 350))
    else:
        text = FONT.render("Score: {}".format(score) , 1, (255, 255 , 255))
        pygame.draw.circle(scr , color , (circle_x , circle_y), radius)
        scr.blit(text , (0 , 0))
    pygame.display.update()

def collision(x , y):
    global circle_x , circle_y , color, score, text
    print('a')
    dist = ((x - circle_x) ** 2 + (circle_y - y)** 2)** 0.5
    if dist < 20 and end == False:
        circle_x , circle_y = r.randint(radius , WIDTH), r.randint(radius , HEIGHT)
        color = (r.randint(0 , 255),r.randint(0 , 255), r.randint(0 , 255))
        score += 1
        text = FONT.render("Score: {}".format(score) , 1, (255, 255 , 255))
    
def end_screen():
    s = []
    
    with open('scoreboard.csv') as csvfile:
        scores = csv.reader(csvfile)
        print(scores)
        for num in scores:
            print(num)
            for i in num:
                n = int(i)
                print(n)
                s.append(n)
                print(s)

        csvfile.close
    
    s.sort(reverse = True)
    if score > s[-1]:
        s[-1] = score
    s.sort(reverse = True)
    with open('scoreboard.csv', 'w', newline='') as csvfile:
        changeS = csv.writer(csvfile)
        for i in range(len(s)):
            print(s[i])
            changeS.writerow([s[i]])
        csvfile.close
    
    return s


"Game"
time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            print('a')
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if end == False:
            x , y = pygame.mouse.get_pos()
            collision(x , y)
        else:
            end = False
            time = 0
            score = 0
            circle_x , circle_y = r.randint(radius , WIDTH- radius), r.randint(radius , HEIGHT- radius)
            color = (r.randint(20 , 255),r.randint(20 , 255), r.randint(20 , 255)) 
    if round(time)/100 > 1200 and end == False:
        end = True
        s = end_screen()
        
    time += 1 
    display(s)

pygame.quit()

