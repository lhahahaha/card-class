# card-class
class for instantiation of card objects

current issue: Lots of repetition in the attack method, probably could be shortened
FOR LINES ON THE ATTACK METHOD: read Lines 108 - 404

-------------------------------------------------------------------------------
Run down of the different sections of my code
1. initialisation of card attributes:
    
    i. image (tuple input of left and right facing character images)
    
    ii. card (tuple of front and back of card)
    
    iii. name
    
    iv. rank
    
    v. typec ('type' is already a command)
    
    vi. HP 
    
2. creation of methods to allow for interation and battle sequence
    i. coords (allows for coordinates/location of images of object to be manipulated and changed when necessary)

    ii. back (blit the back of the card to the screen)
    
    iii. front (blit the front of the card)
    
    iv. checkInput (check if mouse clicks on object)
    
    v. reveal (blit the character image)
    
    vi. bA (assigns the values of different stats to different ranks)
    
        a. base attack value = range of basic damage that can be dealt
        
        b. crit value = if a critical hit, range of damage that can be dealt
        
        c. randomised rate = range for critical hits (e.g. lower ranked cards having a higher chance of a crit hit so their range is smaller)
        
        d. total random rate = value used for attack method
        
    vii. alive (flag to stop attacking when opponent/user has less than 0 HP)
    
    viii. attack (method to attack opponent and affect opponent HP)
    
3. loading of images rank and type
    i. ranks = I, II, III, IV
    ii. type = hearts, spades, diamonds, clovers
    iii. also loads the front and back of the cards 
    
4. Instantiation of the cards per rank and type

5. testing screen
    i. checking the images load and methods 
    
