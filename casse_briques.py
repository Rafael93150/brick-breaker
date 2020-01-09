from tkinter import*
import time
from tkinter import PhotoImage
import pygame
from pygame.locals import*
import random


#-------------------------FONCTIONS-----------------------------#

def droite (event):
    canvas.move (raquette,a,0)

def gauche (event):
    canvas.move (raquette,b,0)

def destruction():
        fin=1
        fene.destroy()
        pygame.quit()

def lancerBoule(*args):
    global lancer
    if lancer == False :
        lancer = True
        collision()

def lancerPartie(*args):
    global menu
    if menu == True:
        menu = False
        game()

def Menu():
    if menu == True:
        canvas.create_image(0,0,image =Img, anchor = NW)
        fene.after(500,Menu_bis)

def Menu_bis():
    if menu == True:
        canvas.create_image(0,0, image = Img_bis, anchor = NW)
        fene.after(500,Menu)


#-------------------------FENETRE-------------------------------#

fene=Tk()
fene.geometry("600x500+200+50") #creation de la fenetre
fene.title("Casse-briques") #titre de la fenetre

photo = PhotoImage(file="ville.gif")
Img = PhotoImage(file="m.gif")           #définition des différentes images
Img_bis = PhotoImage(file="m_bis.gif")

canvas = Canvas(fene, width=500, height=400, bd=0, bg="black") #création du canvas
canvas.pack(padx=10, pady=10)

#----------------------------SONS-------------------------------#

pygame.init()
son = pygame.mixer.Sound("rebond.wav")
fail = pygame.mixer.Sound("fail.wav")


#--------------------------VARIABLES----------------------------#

v=3 #nombre de vies
score=0 #score
menu = True
lancer = False
Vx=2 #vitesse horizontale de la balle
Vy=2 #vitesse verticale de la balle
br10=br11=br12=br13=br14=br15=br16=br17=br18=br19=1 #briques présentes
br20=br21=br22=br23=br24=br25=br26=br27=br28=br29=1
fin=0 #variable qui passe à 0 une fois qu'on appui sur le bouton "quitter"
Menu()

rand=random.randrange(0,2) #définir aléatoirement la diréction initiale de la balle
if rand==1:
    Vx=-Vx
else:
    Vx=Vx

#---------------------------TOUCHES-----------------------------#

canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<space>', lancerBoule)
canvas.bind_all('<p>', lancerPartie)


#-----------------------------JEU-------------------------------#

def game():
    global raquette,boule,brique11,brique10,brique12,brique13,brique14,brique15
    global brique16,brique17,brique18,brique19,brique27,brique28,brique29,labvit
    global brique20,brique21,brique22,brique23,brique24,brique25,brique26
    global Frame7,Frame1,Frame2,Frame3,Frame4,Frame5,Frame6,labs,labv


    canvas.create_image(0, 0, anchor=NW, image=photo)


#---------------------AFFICHAGE DES VIES------------------------#

    Frame1 = Frame(fene, borderwidth=2, relief=GROOVE) #création de la frame des vies
    Frame1.pack(side=LEFT, padx=20, pady=10)
    Frame2 = Frame(Frame1, bg="#50435d", borderwidth=2, relief=GROOVE) #création de la frame qui contient le texte (nombre de vies)
    Frame2.pack(side=RIGHT, padx=5, pady=5)
    Label(Frame1, text="Nombre de vies").pack(padx=10, pady=10) #création du texte contenue dans la Frame1
    labv=Label(Frame2, text=v) #création du texte contenue dans la Frame 2
    labv.pack()


#---------------------AFFICHAGE DU SCORE------------------------#

    Frame3 = Frame(fene, borderwidth=2, relief=GROOVE)
    Frame3.pack(side=LEFT, padx=20, pady=10)
    Frame4 = Frame(Frame3, bg="#904b6b", borderwidth=2, relief=GROOVE)
    Frame4.pack(side=RIGHT, padx=5, pady=5)
    Label(Frame3, text="Score").pack(padx=10, pady=10)
    labs=Label(Frame4, text=score)
    labs.pack()


#-------------------AFFICHAGE DE LA VITESSE---------------------#

    Frame6 = Frame(fene, borderwidth=2, relief=GROOVE)
    Frame6.pack(side=LEFT, padx=20, pady=10)
    Frame7 = Frame(Frame6, bg="#ec8e9e", borderwidth=2, relief=GROOVE)
    Frame7.pack(side=RIGHT, padx=5, pady=5)
    Label(Frame6, text="Vitesse").pack(padx=10, pady=10)
    labvit=Label(Frame7, text="0")
    labvit.pack()


#------------------------BOUTTON QUITTER-------------------------#

    Frame5 = Frame(fene, bg="red", borderwidth=2, relief=RAISED)
    Frame5.pack(side=LEFT, padx=20, pady=10)
    bouton=Button(Frame5, text="Fermer", command=destruction)
    bouton.pack()


#-------------------------COORDONNEES---------------------------#

    raquette=canvas.create_rectangle(200,380,300,390, fill="#50435d")
    a = 0
    b = 0

    boule=canvas.create_oval(242,363,258,379, fill="tan")

    brique11=canvas.create_rectangle(6,18,102,38, fill="#50435d")
    brique13=canvas.create_rectangle(104,18,200,38, fill="#ec8e9e")
    brique15=canvas.create_rectangle(202,18,298,38, fill="#50435d")
    brique17=canvas.create_rectangle(300,18,396,38, fill="#ec8e9e")
    brique19=canvas.create_rectangle(398,18,494,38, fill="#50435d")

    brique10=canvas.create_rectangle(6,40,102,60, fill="#904b6b")
    brique12=canvas.create_rectangle(104,40,200,60, fill="#50435d")
    brique14=canvas.create_rectangle(202,40,298,60, fill="#904b6b")
    brique16=canvas.create_rectangle(300,40,396,60, fill="#50435d")
    brique18=canvas.create_rectangle(398,40,494,60, fill="#904b6b")

    brique20=canvas.create_rectangle(6,62,102,82, fill="#ec8e9e")
    brique22=canvas.create_rectangle(104,62,200,82, fill="#904b6b")
    brique24=canvas.create_rectangle(202,62,298,82, fill="#ec8e9e")
    brique26=canvas.create_rectangle(300,62,396,82, fill="#904b6b")
    brique28=canvas.create_rectangle(398,62,494,82, fill="#ec8e9e")

    brique21=canvas.create_rectangle(6,84,102,104, fill="#50435d")
    brique23=canvas.create_rectangle(104,84,200,104, fill="#ec8e9e")
    brique25=canvas.create_rectangle(202,84,298,104, fill="#50435d")
    brique27=canvas.create_rectangle(300,84,396,104, fill="#ec8e9e")
    brique29=canvas.create_rectangle(398,84,494,104, fill="#50435d")




"""DEBUT DE LA BOUCLE"""


def collision():
    global lancer,br10,br11,br12,br13,br14,br15,br16,br17,br18,br19,br20,br21,br22,br23,br24,br25,br26,br27,br28,br29,Vx,Vy,labvit,score,v,labs, labv,a, b, raquette, boule

    if menu == False :
        if lancer == True:

            while fin==0:


            #-----------------ACTUALISATION DES COORDONNEES-----------------#

                [x0raq,y0raq,x1raq,y1raq] = canvas.coords(raquette)
                [x0b,y0b,x1b,y1b] = canvas.coords(boule)


            #-----------------------BLOQUER LA BOULE------------------------#

                if canvas.coords(boule)[2]>500:
                        Vx=-Vx
                        Vy=Vy
                if canvas.coords(boule)[0]<5:
                        Vx=-Vx
                        Vy=Vy
                if canvas.coords(boule)[1]<5:
                        Vx=Vx
                        Vy=-Vy
                if canvas.coords(boule)[3]>400:
                        Vx=Vx
                        Vy=-Vy

        #fin de la partie

                        if br10==br11==br12==br13==br14==br15==br16==br17==br18==br19==br20==br21==br22==br23==br24==br25==br26==br27==br28==br29==0:
                            Vx=0
                            Vy=0
                            canvas.create_text(250, 200, text = "WIN", fill = "white",font="Times 50 ")

                        else:
                            if v == 1:
                               Vx = 0
                               Vy = 0
                               canvas.create_text(250, 200, text = "GAME OVER", fill = "white",font="Times 50 ")

                        if v >= 1:
                            v=v-1
                            fail.play()



                        labv.destroy()
                        labv=Label(Frame2, text=v)
                        labv.pack()


                if br10==br11==br12==br13==br14==br15==br16==br17==br18==br19==br20==br21==br22==br23==br24==br25==br26==br27==br28==br29==0:
                            Vx=0
                            Vy=0
                            canvas.create_text(250, 200, text = "WIN", fill = "white",font="Times 30 ")


            #---------------------BLOQUER LA RAQUETTE----------------------#

                if x0raq<=5:
                    b=0
                    a=7
                else:
                    b=-7
                if x1raq>=495:
                    b=-7
                    a=0
                else:
                    a=7


            #----------------INTERACTION BOULE - RAQUETTE------------------#

            #Haut de la raquette
                if x0raq-5<=x0b<=x1raq+5:
                    if (y0raq-y1b<=2):
                        if Vy>0:
                            Vy=-Vy-0.05
                        else:
                            Vy=-Vy+0.05
                        if Vx>0:
                            Vx=Vx+0.05
                        else:
                            Vx=Vx-0.05
                        son.play()
                        labvit.destroy()
                        labvit=Label(Frame7, text=round(abs(Vx),1))
                        labvit.pack()

            #Bas de la raquette
                if x0raq<=x1b<=x1raq:
                    if -3<=y0b-y1raq<=1:
                        Vy=-Vy
                        son.play()

            #Droite de la raquette
                if y0raq-2<=y0b<=y1raq+2:
                    if -3<=x0b-x1raq<=2:
                        Vx=-Vx
                        son.play()

            #Gauche de la raquette
                if y0raq-2<=y1b<=y1raq+2:
                    if -3<=x0raq-x1b<=2:
                        Vx=-Vx
                        son.play()




            #-----------------------SUPPRESSION BRIQUES-------------------------#



                if br10==1: #10
                    [x010,y010,x110,y110] = canvas.coords(brique10)
                    if y010<=y0b<=y110:
                        if(-3<=x0b-x110<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique10,canvas.coords(brique10))
                            br10=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x010-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique10,canvas.coords(brique10))
                            br10=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x010<=x0b<=x110:
                        if (-3<=y0b-y110<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique10,canvas.coords(brique10))
                            br10=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y010-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique10,canvas.coords(brique10))
                            br10=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br11==1: #11
                    [x011,y011,x111,y111] = canvas.coords(brique11)
                    if y011<=y0b<=y111:
                        if(-3<=x0b-x111<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique11,canvas.coords(brique11))
                            br11=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x011-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique11,canvas.coords(brique11))
                            br11=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x011<=x0b<=x111:
                        if (-3<=y0b-y111<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique11,canvas.coords(brique11))
                            br11=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y011-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique11,canvas.coords(brique11))
                            br11=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br12==1: #12
                    [x012,y012,x112,y112] = canvas.coords(brique12)
                    if y012<=y0b<=y112:
                        if(-3<=x0b-x112<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique12,canvas.coords(brique12))
                            br12=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x012-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique12,canvas.coords(brique12))
                            br12=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x012<=x0b<=x112:
                        if (-3<=y0b-y112<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique12,canvas.coords(brique12))
                            br12=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y012-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique12,canvas.coords(brique12))
                            br12=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br13==1: #13
                    [x013,y013,x113,y113] = canvas.coords(brique13)
                    if y013<=y0b<=y113:
                        if(-3<=x0b-x113<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique13,canvas.coords(brique13))
                            br13=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x013-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique13,canvas.coords(brique13))
                            br13=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x013<=x0b<=x113:
                        if (-3<=y0b-y113<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique13,canvas.coords(brique13))
                            br13=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y013-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique13,canvas.coords(brique13))
                            br13=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br14==1: #14
                    [x014,y014,x114,y114] = canvas.coords(brique14)
                    if y014<=y0b<=y114:
                        if(-3<=x0b-x114<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique14,canvas.coords(brique14))
                            br14=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x014-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique14,canvas.coords(brique14))
                            br14=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x014<=x0b<=x114:
                        if (-3<=y0b-y114<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique14,canvas.coords(brique14))
                            br14=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y014-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique14,canvas.coords(brique14))
                            br14=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br15==1: #15
                    [x015,y015,x115,y115] = canvas.coords(brique15)
                    if y015<=y0b<=y115:
                        if(-3<=x0b-x115<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique15,canvas.coords(brique15))
                            br15=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x015-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique15,canvas.coords(brique15))
                            br15=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x015<=x0b<=x115:
                        if (-3<=y0b-y115<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique15,canvas.coords(brique15))
                            br15=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y015-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique15,canvas.coords(brique15))
                            br15=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br16==1: #16
                    [x016,y016,x116,y116] = canvas.coords(brique16)
                    if y016<=y0b<=y116:
                        if(-3<=x0b-x116<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique16,canvas.coords(brique16))
                            br16=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x016-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique16,canvas.coords(brique16))
                            br16=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x016<=x0b<=x116:
                        if (-3<=y0b-y116<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique16,canvas.coords(brique16))
                            br16=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y016-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique16,canvas.coords(brique16))
                            br16=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br17==1: #17
                    [x017,y017,x117,y117] = canvas.coords(brique17)
                    if y017<=y0b<=y117:
                        if(-3<=x0b-x117<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique17,canvas.coords(brique17))
                            br17=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x017-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique17,canvas.coords(brique17))
                            br17=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x017<=x0b<=x117:
                        if (-3<=y0b-y117<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique17,canvas.coords(brique17))
                            br17=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y017-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique17,canvas.coords(brique17))
                            br17=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br18==1: #18
                    [x018,y018,x118,y118] = canvas.coords(brique18)
                    if y018<=y0b<=y118:
                        if(-3<=x0b-x118<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique18,canvas.coords(brique18))
                            br18=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x018-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique18,canvas.coords(brique18))
                            br18=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x018<=x0b<=x118:
                        if (-3<=y0b-y118<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique18,canvas.coords(brique18))
                            br18=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y018-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique18,canvas.coords(brique18))
                            br18=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br19==1: #19
                    [x019,y019,x119,y119] = canvas.coords(brique19)
                    if y019<=y0b<=y119:
                        if(-3<=x0b-x119<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique19,canvas.coords(brique19))
                            br19=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x019-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique19,canvas.coords(brique19))
                            br19=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x019<=x0b<=x119:
                        if (-3<=y0b-y119<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique19,canvas.coords(brique19))
                            br19=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y019-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique19,canvas.coords(brique19))
                            br19=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br20==1: #20
                    [x020,y020,x120,y120] = canvas.coords(brique20)
                    if y020<=y0b<=y120:
                        if(-3<=x0b-x120<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique20,canvas.coords(brique20))
                            br20=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x020-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique20,canvas.coords(brique20))
                            br20=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x020<=x0b<=x120:
                        if (-3<=y0b-y120<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique20,canvas.coords(brique20))
                            br20=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y020-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique20,canvas.coords(brique20))
                            br20=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br21==1: #21
                    [x021,y021,x121,y121] = canvas.coords(brique21)
                    if y021<=y0b<=y121:
                        if(-3<=x0b-x121<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique21,canvas.coords(brique21))
                            br21=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x021-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique21,canvas.coords(brique21))
                            br21=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x021<=x0b<=x121:
                        if (-3<=y0b-y121<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique21,canvas.coords(brique21))
                            br21=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y021-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique21,canvas.coords(brique21))
                            br21=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br22==1: #22
                    [x022,y022,x122,y122] = canvas.coords(brique22)
                    if y022<=y0b<=y122:
                        if(-3<=x0b-x122<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique22,canvas.coords(brique22))
                            br22=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x022-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique22,canvas.coords(brique22))
                            br22=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x022<=x0b<=x122:
                        if (-3<=y0b-y120<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique22,canvas.coords(brique22))
                            br22=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-5<=y022-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique22,canvas.coords(brique22))
                            br22=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br23==1: #23
                    [x023,y023,x123,y123] = canvas.coords(brique23)
                    if y023<=y0b<=y123:
                        if(-3<=x0b-x123<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique23,canvas.coords(brique23))
                            br23=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x023-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique23,canvas.coords(brique23))
                            br23=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x023<=x0b<=x123:
                        if (-3<=y0b-y123<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique23,canvas.coords(brique23))
                            br23=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y023-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique23,canvas.coords(brique23))
                            br23=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br24==1: #24
                    [x024,y024,x124,y124] = canvas.coords(brique24)
                    if y024<=y0b<=y124:
                        if(-3<=x0b-x124<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique24,canvas.coords(brique24))
                            br24=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x024-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique24,canvas.coords(brique24))
                            br24=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x024<=x0b<=x124:
                        if (-3<=y0b-y124<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique24,canvas.coords(brique24))
                            br24=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y024-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique24,canvas.coords(brique24))
                            br24=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br25==1: #25
                    [x025,y025,x125,y125] = canvas.coords(brique25)
                    if y025<=y0b<=y125:
                        if(-3<=x0b-x125<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique25,canvas.coords(brique25))
                            br25=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x025-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique25,canvas.coords(brique25))
                            br25=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x025<=x0b<=x125:
                        if (-3<=y0b-y125<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique25,canvas.coords(brique25))
                            br25=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y025-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique25,canvas.coords(brique25))
                            br25=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br26==1: #26
                    [x026,y026,x126,y126] = canvas.coords(brique26)
                    if y026<=y0b<=y126:
                        if(-3<=x0b-x126<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique26,canvas.coords(brique26))
                            br26=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x026-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique26,canvas.coords(brique26))
                            br26=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x026<=x0b<=x126:
                        if (-3<=y0b-y126<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique26,canvas.coords(brique26))
                            br26=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y026-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique26,canvas.coords(brique26))
                            br26=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br27==1: #27
                    [x027,y027,x127,y127] = canvas.coords(brique27)
                    if y027<=y0b<=y127:
                        if(-3<=x0b-x127<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique27,canvas.coords(brique27))
                            br27=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x027-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique27,canvas.coords(brique27))
                            br27=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x027<=x0b<=x127:
                        if (-3<=y0b-y127<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique27,canvas.coords(brique27))
                            br27=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y027-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique27,canvas.coords(brique27))
                            br27=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br28==1: #28
                    [x028,y028,x128,y128] = canvas.coords(brique28)
                    if y028<=y0b<=y128:
                        if(-3<=x0b-x128<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique28,canvas.coords(brique28))
                            br28=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x028-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique28,canvas.coords(brique28))
                            br28=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x028<=x0b<=x128:
                        if (-3<=y0b-y128<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique28,canvas.coords(brique28))
                            br28=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y028-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique28,canvas.coords(brique28))
                            br28=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                if br29==1: #29
                    [x029,y029,x129,y129] = canvas.coords(brique29)
                    if y029<=y0b<=y129:
                        if(-3<=x0b-x129<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique29,canvas.coords(brique29))
                            br29=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=x029-x1b<=3):
                            Vx=-Vx
                            son.play()
                            canvas.delete(brique29,canvas.coords(brique29))
                            br29=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()

                    if x029<=x0b<=x129:
                        if (-3<=y0b-y129<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique29,canvas.coords(brique29))
                            br29=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()
                        if (-3<=y029-y1b<=3):
                            Vy=-Vy
                            son.play()
                            canvas.delete(brique29,canvas.coords(brique29))
                            br29=0
                            score=score+10
                            labs.destroy()
                            labs=Label(Frame4, text=score)
                            labs.pack()


                canvas.move(boule, Vx,Vy)
                time.sleep(0.01)
                canvas.update()


fene.mainloop()