from tkinter import *




def initialisation (self):
    self.geometry("800x500")
    self.minsize(900,600)
    self.maxsize(900,600)
    self.iconbitmap("assets/games_logo.ico")
    self.config(background = '#608DCC')

def principale(master):

    frame = Frame(master,bg = "#608DCC")   

    #Personnaliser cette fenêtre 
    window.title("MULTI GAMES")
    

    #Ajout du titre Bienvenue
    label_title = Label(frame, text="Bienvenue sur MULTI GAMES", font = ("Arial",45), bg= "#608DCC",fg= "white")
    label_title.pack(pady=20)

    

    #Ajout du sous-titre Tag Name
    label_subtitle = Label(frame, text="By ILAN990", font = ("Arial",25), bg= "#608DCC",fg= "white")
    label_subtitle.pack()

    #Création d'un bouton vers le menu
    connexion_button = Button(frame, text= 'JOUER', font = ("Arial",40), bg= "white",fg= "#608DCC",command=lambda: change_frame('menu'))
    connexion_button.place(x = 340 , y= 460)
    


    return frame
    
def menu (master):

    #Personnaliser cette fenêtre 
    window.title("MULTI GAMES - MENU")
    frame = Frame(master,bg= "#608DCC")
    frame.rowconfigure(7,minsize=50)
    frame.columnconfigure(2,minsize=50)
    
    t_menu_jeux = [    "pendu"    ,"prochainement","prochainement",
                   "prochainement","prochainement","prochainement",
                   "prochainement","prochainement","prochainement",
                   "prochainement","prochainement","prochainement"]
    
    change_box = [     "pendu"    ,"pendu","prochainement",
                   "prochainement","prochainement","prochainement",
                   "prochainement","prochainement","prochainement",
                   "prochainement","prochainement","prochainement"]

    #Ajout d'un bouton retour
    label_retour = Button(frame,text = "RETOUR",bg= "red",fg= "white",height = 2, width = 20,command=lambda: change_frame('principale'))
    label_retour.grid(row=0,column=0,pady=10)
    
    #Ajouter du Titre Menu
    label_title = Label(frame, text="MENU", font = ("Arial",45), bg= "#608DCC",fg= "black")
    label_title.grid(row=1,column=1,pady=30,padx=30)
    
   
    for j in range(3):
        for v in range(4):
             #Ajout d'un bouton PENDU

             label_retour= Button(frame,text = t_menu_jeux[3* j + v],bg= "#647B9A",fg= "white",height = 4, width = 35,command=lambda: change_frame(change_box[(3 * j) + v]))
             label_retour.grid(row=4+v,column=0+j,pady=10,padx=20)
             print(change_box[3 * j + v])
    
    return frame


#############################################          PENDU          ################################################################## 
def pendu(master):
    #Personnaliser cette fenêtre 
    window.title("MULTI GAMES - PENDU")
    frame = Frame(master,bg= "#608DCC")

    #Ajout d'un bouton retour
    label_retour = Button(frame,text = "RETOUR",bg= "red",fg= "white",height = 2, width = 20,command=lambda: change_frame('menu'))
    label_retour.place(x=20,y=20)

    lettres = Frame(frame)
    lettres.grid(row=1, column=1)
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(2):
        for j in range(10):
            btn = Button(lettres,text=ALPHA[10 * i + j],bg= "#608DCC",relief=FLAT,font='times 30')
            btn.grid(row=i, column=j)

    for j in range(6):
        btn = Button(frame, text=ALPHA[20 + j],bg= "#608DCC", relief=FLAT, font='times 30')
        btn.grid(row=2, column=j + 2)

    return frame   




########################################################################################################################################

def prochainement(master):
    #Personnaliser cette fenêtre 
    window.title("MULTI GAMES - Prochainement...")
    frame = Frame(master,bg= "#608DCC")

    #Ajout d'un bouton retour
    label_retour = Button(frame,text = "RETOUR",bg= "red",fg= "white",height = 2, width = 20,command=lambda: change_frame('menu'))
    label_retour.place(x=20,y=20)

    #Ajouter du Titre Menu
    label_title = Label(frame, text="Un peu de patience !", font = ("Arial",45), bg= "#608DCC",fg= "black")
    label_title.place(x=320,y=200)

    #Ajouter du Titre Menu
    label_title = Label(frame, text="Peut-être dans la prochaine ", font = ("Arial",45), bg= "#608DCC",fg= "black")
    label_title.place(x=160,y=300)
    #Ajouter du Titre Menu
    label_title = Label(frame, text="mise à jour...", font = ("Arial",45), bg= "#608DCC",fg= "black")
    label_title.place(x=160,y=400)

    return frame

def change_frame(frame_name):
    """ Change la frame actuelle de notre application par une nouvelle frame.
    Cette nouvelle frame est crée par une fonction.
    frame_name est la clé d'un dictionaire contenant les fonctions créant des frames.
    """
    children = window.winfo_children()
    frame = children[0] # Notre app n'a qu'un seul widget enfant, la frame qu'on a créé.
    frame.destroy()
    frame_function = usine_de_frames[frame_name]
    new_frame = frame_function(window)
    new_frame.pack(side = BOTTOM,fill= BOTH,expand=1)

window = Tk ()
initialisation(window)
usine_de_frames = {'menu': menu, 'principale': principale,'pendu':pendu,'prochainement':prochainement}
frame = principale(window)
frame.pack(side = BOTTOM,fill= BOTH,expand=1)    
window.mainloop()