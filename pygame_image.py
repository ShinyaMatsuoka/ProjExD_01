import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") #練習1：背景画像の読み込み
    bg_imgb = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs =[kk_img, pg.transform.rotozoom(kk_img, 2, 1.0),
              pg.transform.rotozoom(kk_img, 4, 1.0), 
              pg.transform.rotozoom(kk_img, 6, 1.0),
              pg.transform.rotozoom(kk_img, 8, 1.0), 
              pg.transform.rotozoom(kk_img, 10, 1.0),
              pg.transform.rotozoom(kk_img, 8, 1.0),
              pg.transform.rotozoom(kk_img, 6, 1.0), 
              pg.transform.rotozoom(kk_img, 4, 1.0),
              pg.transform.rotozoom(kk_img, 2, 1.0),]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        print(x)
        screen.blit(bg_img, [-x, 0]) #練習4：背景画像の表示
        screen.blit(bg_imgb, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(kk_imgs[tmr%10], [300, 200])
        pg.display.update()
        tmr += 1
        clock.tick(300)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()