import random, pygame, os, sys, font
from font import orangeKid, pcSenior
pygame.init()

SCREEN = pygame.display.set_mode((1250, 938))

class card:
    def __init__(self, image, card, name, rank, typec, hp):
        # allows for instantiation of an object of the card class
        self.imageL = image[0]
        self.imageR = image[1]

        self.cardF = card[0]
        self.cardB = card[1]

        self.name = name
        self.rank = rank
        self.typec = typec
        self.hp = hp

    def coords(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.rectL = self.imageL.get_rect(center=(self.x, self.y))
        self.rectR = self.imageR.get_rect(center=(self.x, self.y))
        self.rectF = self.cardF.get_rect(center=(self.x, self.y))
        self.rectB = self.cardB.get_rect(center=(self.x, self.y))

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
MFRONTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango', 'Mfront1.png')).convert_alpha()
MLEFTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0mango','Lmango1.png')).convert_alpha()
MRIGHTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0mango','Rmango1.png')).convert_alpha()

MFRONTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango', 'Mfront2.png')).convert_alpha()
MLEFTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0mango','Lmango2.png')).convert_alpha()
MRIGHTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0mango','Rmango2.png')).convert_alpha()

MFRONTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango', 'Mfront3.png')).convert_alpha()
MLEFTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0mango','Lmango3.png')).convert_alpha()
MRIGHTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0mango','Rmango3.png')).convert_alpha()

MFRONTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','mango', 'Mfront4.png')).convert_alpha()
MLEFTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0mango','Lmango4.png')).convert_alpha()
MRIGHTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0mango','Rmango4.png')).convert_alpha()

#------------------------------------------------------------------------------------------------------------------------------------

# diamonds
RFRONTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river', 'Rfront1.png')).convert_alpha()
RLEFTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0river','Lriver1.png')).convert_alpha()
RRIGHTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0river','Rriver1.png')).convert_alpha()

RFRONTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river', 'Rfront2.png')).convert_alpha()
RLEFTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0river','Lriver2.png')).convert_alpha()
RRIGHTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0river','Rriver2.png')).convert_alpha()

RFRONTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river', 'Rfront3.png')).convert_alpha()
RLEFTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0river','Lriver3.png')).convert_alpha()
RRIGHTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0river','Rriver3.png')).convert_alpha()
  
RFRONTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','river', 'Rfront4.png')).convert_alpha()
RLEFTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0river','Lriver4.png')).convert_alpha()
RRIGHTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0river','Rriver4.png')).convert_alpha()

#------------------------------------------------------------------------------------------------------------------------------------

# clovers
CFRONTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry', 'Cfront1.png')).convert_alpha()
CLEFTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0cherry','Lcherry1.png')).convert_alpha()
CRIGHTI = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0cherry','Rcherry1.png')).convert_alpha()

CFRONTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry', 'Cfront2.png')).convert_alpha()
CLEFTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0cherry','Lcherry2.png')).convert_alpha()
CRIGHTII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0cherry','Rcherry2.png')).convert_alpha()

CFRONTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry', 'Cfront3.png')).convert_alpha()
CLEFTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0cherry','Lcherry3.png')).convert_alpha()
CRIGHTIII = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0cherry','Rcherry3.png')).convert_alpha()

CFRONTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','cherry', 'Cfront4.png')).convert_alpha()
CLEFTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0cherry','Lcherry4.png')).convert_alpha()
CRIGHTIV = pygame.image.load(os.path.join(os.path.dirname(__file__), 'characters init','0cherry','Rcherry4.png')).convert_alpha()

#----------------------------------------card instantiation---------------------------------------

# right facing, left facing, front card, back card
# self.imageL = image[0], self.imageR = image[1], self.cardF = card[0], self.cardB = card[1], self.name = name, self.rank = rank, self.typec = typec, self.hp = hp

#Hearts
QEPSI_IV = card(image=(QLEFTIV, QRIGHTIV), card=(QRIGHTIV, BACKCARD), name="Qepsi IV", rank="IV", typec="Hearts", hp=225)
QEPSI_III = card(image=(QLEFTIII, QRIGHTIII), card=(QFRONTIII, BACKCARD), name="Qepsi III", rank="III", typec="Hearts", hp=175)
QEPSI_II = card(image=(QLEFTII, QRIGHTII), card=(QFRONTII, BACKCARD), name="Qepsi II", rank="II", typec="Hearts", hp=125)
QEPSI_I = card(image=(QLEFTI, QRIGHTI), card=(QFRONTI, BACKCARD), name="Qepsi I", rank="I", typec="Hearts", hp= 75)

#Spades
MANGOIV = card(image=(MLEFTI, MRIGHTI), card=(MFRONTI, BACKCARD), name="Mango IV", rank="IV", typec="Spades", hp=225)
MANGOIII = card(image=(MLEFTII, MRIGHTII), card=(MFRONTII, BACKCARD), name="Mango III", rank="III", typec="Spades", hp=175)
MANGOII = card(image=(MLEFTIII, MRIGHTIII), card=(MFRONTIII, BACKCARD), name="Mango II", rank="II", typec="Spades", hp=125)
MANGOI = card(image=(MLEFTIV, MRIGHTIV), card=(MFRONTIV, BACKCARD), name="Mango I", rank="I", typec="Spades", hp=75)

#Diamonds
RIVERIV = card(image=(RLEFTI, RRIGHTI), card=(RFRONTI, BACKCARD), name="River IV", rank="IV", typec="Diamonds", hp=225)
RIVERIII = card(image=(RLEFTII, RRIGHTII), card=(RFRONTII, BACKCARD), name="River III", rank="III", typec="Diamonds", hp=175)
RIVERII = card(image=(RLEFTIII, RRIGHTIII), card=(RFRONTIII, BACKCARD), name="River II", rank="II", typec="Diamonds", hp=125)
RIVERI = card(image=(RLEFTIV, RRIGHTIV), card=(RFRONTIV, BACKCARD), name="River I", rank="I", typec="Diamonds", hp=75)

#Clovers
CHERRYIV = card(image=(CLEFTI, CRIGHTI), card=(CFRONTI, BACKCARD), name="Cherry IV", rank="IV", typec="Clovers", hp=225)
CHERRYIII = card(image=(CLEFTII, CRIGHTII), card=(CFRONTII, BACKCARD), name="Cherry III", rank="III", typec="Clovers", hp=175)
CHERRYII = card(image=(CLEFTIII, CRIGHTIII), card=(CFRONTIII, BACKCARD), name="Cherry II", rank="II", typec="Clovers", hp=125)
CHERRYI = card(image=(CLEFTIV, CRIGHTIV), card=(CFRONTIV, BACKCARD), name="Cherry I", rank="I", typec="Clovers", hp=75)

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
        QEPSI_I.coords(pos=(300, 469))

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
        QEPSI_I.coords(pos=(625, 469))

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
        QEPSI_I.coords(pos=(625, 469))
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
