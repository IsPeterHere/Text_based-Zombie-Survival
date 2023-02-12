import Terminal_py
from time import sleep
import Running_process as sg

def update():

    if len(iall.ALLP) > 0:
        tx.text = "|".join(iall.ALLP)

        if iall.ip == True:
            iall.ALLP = []
            Name.text = "Name:"+str(iall.name)

            Health.text = "Health:"+str(int(iall.health * (1 + (iall.statHEALTH / 10))))+"%"
            if iall.daysTILLsafety != None:
                days.text = "            You hvae "+str(iall.daysTILLsafety)+" days until safety"

                Attack.text = "Attack:" + str(iall.attack + iall.statATTACK)
                Defence.text = "Defence:" + str(iall.defence + iall.statDEFENCE)
                Food.text = "Food(Days):" + str(iall.food)
                Weapon.text = str(iall.activeWEP)
                Armor.text = str(iall.activeDEF)

                WeaponA.text = "Active weapon:"
                ArmorA.text = "Active armor:"

                if iall.dog == 1:
                    DogName.text ="Dog Name:" + str(iall.dogNAME)
                    DogHealth.text = "Dog Health:" + str(iall.dogHEALTH)

            iall.ip = False
    
    
T = Terminal_py.Terminal()
tx = T.text_box(10,20,10,90,left = "|",right = "|",top = "_")

Name = T.text_box(7,7,10,23,left = "[",right = "]")
Health = T.text_box(7,7,24,37,left = "[",right = "]")
days = T.text_box(7,7,38,90,left = "",right = "")

Attack = T.text_box(12,12,94,115,left = "",right = "")
Defence = T.text_box(13,13,94,115,left = "",right = "")
Food = T.text_box(14,14,94,115,left = "",right = "")

WeaponA = T.text_box(16,16,94,110,left = "",right = "")
ArmorA = T.text_box(19,19,94,110,left = "",right = "")
Weapon = T.text_box(17,17,94,110,left = "",right = "")
Armor = T.text_box(20,20,94,110,left = "",right = "")

DogName = T.text_box(22,22,94,115,left = "",right = "")
DogHealth = T.text_box(23,23,94,115,left = "",right = "")


iall = sg.ALL()
T.calling = update
iall.start()




        


