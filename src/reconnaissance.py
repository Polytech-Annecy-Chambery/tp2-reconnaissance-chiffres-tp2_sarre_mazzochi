from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    img1 = image.binarisation(S)
    img2 = img1.localisation()
    sim = 0
    chiffre=-1
      
    for i in range (len(liste_modeles)):
        img3=img2.resize(liste_modeles[i].H,liste_modeles[i].W)
        if img3.similitude(liste_modeles[i])>sim:
            sim = img3.similitude(liste_modeles[i])
            chiffre=i
            print("pour" ,i, "=", sim)
    return chiffre
            
