import random, pygame, os, sys, font
from turtle import back, position
from re import T
import secrets
from winreg import QueryReflectionKey
from buttonclass import Button
from font import orangeKid, pcSenior
pygame.init()

#mainFont = pygame.font.Font(orangeKid, 100)
SCREEN = pygame.display.set_mode((1250, 938))

class card:
    def __init__(self, pos, image, card, name, rank, typec, hp):
        # allows for instantiation of an object of the card class
        # right, left, front card, back card
        self.x = pos[0]
        self.y = pos[1]

        self.imageL = image[0]
        self.imageR = image[1]
        self.rectL = self.imageL.get_rect(center=(self.x, self.y))
        self.rectR = self.imageR.get_rect(center=(self.x, self.y))

        self.cardF = card[0]
        self.cardB = card[1]
        self.rectF = self.cardF.get_rect(center=(self.x, self.y))
        self.rectB = self.cardB.get_rect(center=(self.x, self.y))

        self.name = name
        self.rank = rank
        self.typec = typec
        self.hp = hp



    def back(self, screen): # shows back of card
        screen.blit(self.cardB, self.rectB) # display image and rect on screen

    def front(self, screen): # show front of card
        screen.blit(self.cardF, self.rectF)
  
    def checkInput(self, position): # checks if input is within the bounds of the image e.g. the mouse
        if position[0] in range(self.rectF.left, self.rectF.right) and position[1] in range(self.rectF.top, self.rectF.bottom):
            print("click") # checking if image pressed
            return True
        return False

    def reveal(self, screen):
        screen.blit(self.imageL, self.rectL)
        
    # change the coordinates of the original object
    def add(self, user, p):
        user.x = self.x - p[0]
        user.y = self.y - p[1]

    # allows for change in attributes B)
    #def changeCoords(self, pos):
        #self.x = pos[0]
        #self.y = pos[1]
        #return(self.x, self.y)

    def bA(self, user):

        # ensures each round the total attack value is random and ensures the chance for critical attacks are random
        if user.rank == "IV":
            baseAttk = random.randint(17, 20)
            critRate = random.randint(22, 25)
            randRate = random.randint(0, 100)
            tRate = 100
            # set a tuple of the values to return so they can be used in other functions
            return baseAttk, critRate, randRate, tRate

        elif user.rank == "III":
            baseAttk = random.randint(12, 15)
            critRate = random.randint(17, 20)
            randRate = random.randint(0, 75)
            tRate = 100
            return baseAttk, critRate, randRate, tRate

        elif user.rank == "II":
            baseAttk = random.randint(7, 10)
            critRate = random.randint(12, 15)
            randRate = random.randint(0, 50)
            tRate = 100
            return baseAttk, critRate, randRate, tRate

        elif user.rank == "I":
            baseAttk = random.randint(2, 5)
            critRate = random.randint(7, 10)
            randRate = random.randint(0, 25)
            tRate = 100
            return baseAttk, critRate, randRate, tRate

    # testing health
    def alive(self, user):
        flag = True
        if user.hp > 0:
            return flag

        else:

            flag = False
            print(user.name, " has fainted!")

            if user in hand:
                hand.remove(user)
                print("user")

                k = 0
                while k != len(hand):
                    print(hand[k].name)
                    k = k + 1

            else:
                comHand.remove(user)
                print("computer")

                k = 0
                while k != len(comHand):
                    print(comHand[k].name)
                    k = k + 1

            return flag

    def attack(self, user, opponent):
        # function for attacking opponents, parameters are for the player's card (user) which would be attacking, and the opponent's card which is selected to be attacked

        # this section is for the type advantages, e.g. hearts deals more damage to spades, similar to how in pokemon, a fire type deals more damage to a grass type
        if user.typec == "Hearts" and opponent.typec == "Spades":
            # set the return values to variable names
            result = user.bA(user)
            baseAttk = result[0]
            critRate = result[1]
            randRate = result[2]
            tRate = result[3]

            if randRate > (tRate * 0.8):
                # if the random chance is greater than 80% of total random value then the attack is a critical attack, i.e. deals more damage

                userA = round(baseAttk * 2 * (critRate / 10))
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("Critical hit!")
                print("It's super effective!")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            else:

                userA = baseAttk * 2
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("It's super effective!")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            # testing each base value that it is within range, random each turn and that the results align with these values, e.g. a critical hit
            print("base attack: ", baseAttk)
            print("total: ", userA)
            print("crit ", critRate)
            print("random: ", randRate)

        elif user.typec == "Spades" and opponent.typec == "Diamonds":

            result = user.bA(user)
            baseAttk = result[0]
            critRate = result[1]
            randRate = result[2]
            tRate = result[3]

            if randRate > (tRate * 0.8):

                userA = round(baseAttk * 2 * (critRate / 10))
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("Critical hit!")
                print("It's super effective!")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            else:

                userA = baseAttk * 2

                opponent.hp = opponent.hp - userA
                print(user.name, " dealt ", userA, " damage!")
                print("It's super effective!")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            # testing
            print("base attack: ", baseAttk)
            print("total: ", userA)
            print("crit ", critRate)
            print("random: ", randRate)

        elif user.typec == "Diamonds" and opponent.typec == "Clovers":

            result = user.bA(user)
            baseAttk = result[0]
            critRate = result[1]
            randRate = result[2]
            tRate = result[3]

            if randRate > (tRate * 0.8):

                userA = round(baseAttk * 2 * (critRate / 10))
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("Critical hit!")
                print("It's super effective!")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            else:

                userA = baseAttk * 2
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("It's super effective!")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            # testing
            print("base attack: ", baseAttk)
            print("total: ", userA)
            print("crit ", critRate)
            print("random: ", randRate)

        elif user.typec == "Clovers" and opponent.typec == "Hearts":

            result = user.bA(user)
            baseAttk = result[0]
            critRate = result[1]
            randRate = result[2]
            tRate = result[3]

            if randRate > (tRate * 0.8):

                userA = round(baseAttk * 2 * (critRate / 10))
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("Critical hit!")
                print("It's super effective!")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            else:

                userA = baseAttk * 2
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("It's super effective!")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            # testing
            print("base attack: ", baseAttk)
            print("total: ", userA)
            print("crit ", critRate)
            print("random: ", randRate)

        # this is for the disadvantages, i.e. they will deal less damage to a certain type, e.g. hearts deal less damage to clovers while clovers will deal more damage to hearts
        elif user.typec == "Hearts" and opponent.typec == "Clovers":

            result = user.bA(user)
            baseAttk = result[0]
            critRate = result[1]
            randRate = result[2]
            tRate = result[3]

            if randRate > (tRate * 0.8):

                userA = round((baseAttk * (critRate / 10) / 1.5))
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("Critical hit!")
                print("It's not very effective...")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            else:

                userA = round(baseAttk / 1.5)
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("It's not very effective...")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            # testing
            print("base attack: ", baseAttk)
            print("total: ", userA)
            print("crit ", critRate)
            print("random: ", randRate)

        elif user.typec == "Spades" and opponent.typec == "Hearts":

            result = user.bA(user)
            baseAttk = result[0]
            critRate = result[1]
            randRate = result[2]
            tRate = result[3]

            if randRate > (tRate * 0.8):

                userA = round((baseAttk * (critRate / 10) / 1.5))
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("Critical hit!")
                print("It's not very effective...")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            else:

                userA = round(baseAttk / 1.5)
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("It's not very effective...")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            #testing
            print("base attack: ", baseAttk)
            print("total: ", userA)
            print("crit ", critRate)
            print("random: ", randRate)

        elif user.typec == "Diamonds" and opponent.typec == "Spades":

            result = user.bA(user)
            baseAttk = result[0]
            critRate = result[1]
            randRate = result[2]
            tRate = result[3]

            if randRate > (tRate * 0.8):

                userA = round((baseAttk * (critRate / 10) / 1.5))
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("Critical hit!")
                print("It's not very effective...")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            else:

                userA = round(baseAttk / 1.5)
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("It's not very effective...")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            #testing
            print("base attack: ", baseAttk)
            print("total: ", userA)
            print("crit ", critRate)
            print("random: ", randRate)

        elif user.typec == "Clovers" and opponent.typec == "Diamonds":

            result = user.bA(user)
            baseAttk = result[0]
            critRate = result[1]
            randRate = result[2]
            tRate = result[3]

            if randRate > (randRate * 0.8):

                userA = round((baseAttk * (critRate / 10) / 1.5))
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("Critical hit!")
                print("It's not very effective...")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            else:

                userA = round(baseAttk / 1.5)
                opponent.hp = opponent.hp - userA

                print(user.name, " dealt ", userA, " damage!")
                print("It's not very effective...")
                print(opponent.name, " is on ", opponent.hp, "HP!")

            #testing
            print("base attack: ", baseAttk)
            print("total: ", userA)
            print("crit ", critRate)
            print("random: ", randRate)

        else:

            result = user.bA(user)
            baseAttk = result[0]
            critRate = result[1]
            randRate = result[2]
            tRate = result[3]

            if randRate > (randRate * 0.8):

                userA = round((baseAttk * (critRate / 10) / 1.5))
                opponent.hp = opponent.hp - userA
                print(user.name, " dealt ", userA, " damage.")
                print("Critical hit!")
                print(opponent.name, " is on ", opponent.hp, "HP")

            else:
                userA = round(baseAttk / 1.5)
                opponent.hp = opponent.hp - userA
                print(user.name, " dealt ", baseAttk, " damage.")
                print(opponent.name, " is on ", opponent.hp, "HP")

            #testing
            print("base attack: ", baseAttk)
            print("total: ", userA)
            print("crit ", critRate)
            print("random: ", randRate)


#==========================================testing the class methods==========================================

# This section is for the instantiation of each individual card and all their relevant attributes

#-----------------------------------------------opening images-----------------------------------------------
# back of cards images
backCard = pygame.image.load(os.path.join(os.path.dirname(__file__), 'individualelements', 'backcard.png')).convert_alpha()
BACKCARD = pygame.transform.scale(backCard, (352, 505))

# hearts
QFRONTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', 'qepsi', 'Qfront1.png')).convert_alpha()
QLEFTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', '0qepsi', 'Lqepsi1.png')).convert_alpha()
QRIGHTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', '0qepsi','Rqepsi1.png')).convert_alpha()

QFRONTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', 'qepsi', 'Qfront2.png')).convert_alpha()
QLEFTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', '0qepsi','Lqepsi2.png')).convert_alpha()
QRIGHTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', '0qepsi','Rqepsi2.png')).convert_alpha()

QFRONTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', 'qepsi', 'Qfront3.png')).convert_alpha()
QLEFTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', '0qepsi','Lqepsi3.png')).convert_alpha()
QRIGHTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', '0qepsi','Rqepsi3.png')).convert_alpha()

QFRONTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', 'qepsi', 'Qfront4.png')).convert_alpha()
QLEFTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', '0qepsi','Lqepsi4.png')).convert_alpha()
QRIGHTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init', '0qepsi','Rqepsi4.png')).convert_alpha()

#------------------------------------------------------------------------------------------------------------------------------------

# spades
mFrontI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango', 'Mfront1.png')).convert_alpha()
mLeftI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango','1-mango-L.png')).convert_alpha()
mRightI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango','1-mango-R.png')).convert_alpha()

mFrontII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango', 'Mfront2.png')).convert_alpha()
mLeftII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango','2-mango-L.png')).convert_alpha()
mRightII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango','2-mango-R.png')).convert_alpha()

mFrontIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango', 'Mfront3.png')).convert_alpha()
mLeftIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango','3-mango-L.png')).convert_alpha()
mRightIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango','3-mango-R.png')).convert_alpha()

mFrontIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango', 'Mfront4.png')).convert_alpha()
mLeftIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango','4-mango-L.png')).convert_alpha()
mRightIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango','4-mango-R.png')).convert_alpha()

#------------------------------------------------------------------------------------------------------------------------------------

# diamonds
rFrontI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river', 'Rfront1.png')).convert_alpha()
rLeftI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river','1-river-L.png')).convert_alpha()
rRightI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river','1-river-R.png')).convert_alpha()

rFrontII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river', 'Rfront2.png')).convert_alpha()
rLeftII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river','2-river-L.png')).convert_alpha()
rRightII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river','2-river-R.png')).convert_alpha()

rFrontIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river', 'Rfront3.png')).convert_alpha()
rLeftIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river','3-river-L.png')).convert_alpha()
rRightIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river','3-river-R.png')).convert_alpha()

rFrontIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river', 'Rfront4.png')).convert_alpha()
rLeftIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river','4-river-L.png')).convert_alpha()
rRightIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river','4-river-R.png')).convert_alpha()

#------------------------------------------------------------------------------------------------------------------------------------

# clovers
cFrontI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry', 'Cfront1.png')).convert_alpha()
cLeftI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry','1-cherry-L.png')).convert_alpha()
cRightI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry','1-cherry-R.png')).convert_alpha()

cFrontII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry', 'Cfront2.png')).convert_alpha()
cLeftII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry','2-cherry-L.png')).convert_alpha()
cRightII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry','2-cherry-R.png')).convert_alpha()

cFrontIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry', 'Cfront3.png')).convert_alpha()
cLeftIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry','3-cherry-L.png')).convert_alpha()
cRightIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry','3-cherry-R.png')).convert_alpha()

cFrontIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry', 'Cfront4.png')).convert_alpha()
cLeftIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry','4-cherry-L.png')).convert_alpha()
cRightIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry','4-cherry-R.png')).convert_alpha()


#----------------------------------------card instantiation---------------------------------------

# right facing, left facing, front card, back card
# self.imageL = image[0], self.imageR = image[1], self.cardF = card[0], self.cardB = card[1], self.name = name, self.rank = rank, self.typec = typec, self.hp = hp

#Hearts
QEPSI_IV = card(pos=(200, 200), image=(QLEFTIV, QRIGHTIV), card=(QRIGHTIV, BACKCARD), name="Qepsi IV", rank="IV", typec="Hearts", hp=225)
QEPSI_III = card(pos=(200, 200), image=(QLEFTIII, QRIGHTIII), card=(QFRONTIII, BACKCARD), name="Qepsi III", rank="III", typec="Hearts", hp=175)
QEPSI_II = card(pos=(200, 200), image=(QLEFTII, QRIGHTII), card=(QFRONTII, BACKCARD), name="Qepsi II", rank="II", typec="Hearts", hp=125)
QEPSI_I = card(pos=(625, 469), image=(QLEFTI, QRIGHTI), card=(QFRONTI, BACKCARD), name="Qepsi I", rank="I", typec="Hearts", hp= 75)

#Spades
mangoIV = card(pos=(200, 200), image=(mLeftI, mRightI), card=(mFrontI, BACKCARD), name="Mango IV", rank="IV", typec="Spades", hp=225)
mangoIII = card(pos=(200, 200), image=(mLeftII, mRightII), card=(mFrontII, BACKCARD), name="Mango III", rank="III", typec="Spades", hp=175)
mangoII = card(pos=(200, 200), image=(mLeftIII, mRightIII), card=(mFrontIII, BACKCARD), name="Mango II", rank="II", typec="Spades", hp=125)
mangoI = card(pos=(200, 200), image=(mLeftIV, mRightIV), card=(mFrontIV, BACKCARD), name="Mango I", rank="I", typec="Spades", hp=75)

#Diamonds
riverIV = card(pos=(200, 200), image=(rLeftI, rRightI), card=(rFrontI, BACKCARD), name="River IV", rank="IV", typec="Diamonds", hp=225)
riverIII = card(pos=(200, 200), image=(rLeftII, rRightII), card=(rFrontII, BACKCARD), name="River III", rank="III", typec="Diamonds", hp=175)
riverII = card(pos=(200, 200), image=(rLeftIII, rRightIII), card=(rFrontIII, BACKCARD), name="River II", rank="II", typec="Diamonds", hp=125)
riverI = card(pos=(200, 200), image=(rLeftIV, rRightIV), card=(rFrontIV, BACKCARD), name="River I", rank="I", typec="Diamonds", hp=75)

#Clovers
cherryIV = card(pos=(200, 200), image=(cLeftI, cRightI), card=(cFrontI, BACKCARD), name="Cherry IV", rank="IV", typec="Clovers", hp=225)
cherryIII = card(pos=(200, 200), image=(cLeftII, cRightII), card=(cFrontII, BACKCARD), name="Cherry III", rank="III", typec="Clovers", hp=175)
cherryII = card(pos=(200, 200), image=(cLeftIII, cRightIII), card=(cFrontIII, BACKCARD), name="Cherry II", rank="II", typec="Clovers", hp=125)
cherryI = card(pos=(200, 200), image=(cLeftIV, cRightIV), card=(cFrontIV, BACKCARD), name="Cherry I", rank="I", typec="Clovers", hp=75)

# This is where all the cards are "stored" and this ensures that both the user and computer do not get duplicate cards, as it deletes chosen ones as it goes along.
#deck = [qepsiI, qepsiII, qepsiIII, qepsiIV, mangoI, mangoII, mangoIII, mangoIV, riverI, riverII, riverIII, riverIV, cherryI, cherryII, cherryIII, cherryIV]

hand = []  #user's cards
comHand = []  # opponent's hand

#===================================================testing==================================================

pygame.display.set_caption("image test")
SCREEN = pygame.display.set_mode((1250, 938))

def getFont(size):
    # show relevant font 
    return pygame.font.Font(pcSenior, size)

def revealFrontCard():
    while True:
        
        SCREEN.fill("#0f0f0fff")

        # change coordinates and location of object
        QEPSI_I.add(user=QEPSI_I, p=(300, 0))

        # load object image onto screen
        QEPSI_I.front(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

def revealSprite():
    while True:

        SCREEN.fill("#0f0f0fff")

        # depict character image and name
        QEPSI_I.reveal(SCREEN)
        CHARA_TEXT = getFont(50).render(QEPSI_I.name, True, "White")
        CHARA_TEXTRECT = CHARA_TEXT.get_rect(center=(627, 150))
        SCREEN.blit(CHARA_TEXT, CHARA_TEXTRECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QEPSI_I.checkInput(position=pygame.mouse.get_pos()):
                    revealFrontCard()

        pygame.display.update()
 

def cardBack():
    while True:

        SCREEN.fill("black")
        QEPSI_I.back(screen=SCREEN)        
        REVEAL_TEXT = getFont(50).render("Click to reveal card!", True, "#c71e1e")
        REVEAL_TEXTRECT = REVEAL_TEXT.get_rect(center=(627, 150))
        SCREEN.blit(REVEAL_TEXT, REVEAL_TEXTRECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QEPSI_I.checkInput(position=pygame.mouse.get_pos()):
 
                    revealSprite()
                
        pygame.display.update()

cardBack()
