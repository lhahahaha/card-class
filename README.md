# card-class
class for instantiation of card objects

current issue: cannot change the location of the images, the (x, y) coordinates are fixed to the __init__ method and when the object is instantiated; the values cannot be changed

Run down of the different sections of my code
1. initialisation of card attributes:
    i. pos (tuple input of x and y coordinates)
    ii. image (tuple input of left and right facing character images)
    iii. card (tuple of front and back of card)
    iv. name
    v. rank
    vi. typec ('type' is already a command)
    vii. HP 
    
2. creation of methods to allow for interation and battle sequence
    i. back (blit the back of the card to the screen)
    ii. front (blit the front of the card)
    iii. checkInput (check if mouse clicks on object)
    iv. reveal (blit the character image)
    v. add (meant to allow for the original init set (x, y) coordinates to be changed - doesn't work)
    vi. changeCoords (same intent as above, but also does not work)
    vii. bA (assigns the values of different stats to different ranks)
        a. base attack value = range of basic damage that can be dealt
        b. crit value = if a critical hit, range of damage that can be dealt
        c. randomised rate = range for critical hits (e.g. lower ranked cards having a higher chance of a crit hit so their range is smaller)
        d. total random rate = value used for attack method
    viii. alive (flag to stop attacking when opponent/user has less than 0 HP)
    ix. attack (method to attack opponent and affect opponent HP)
    
3. loading of images rank and type
    i. ranks = I, II, III, IV
    ii. type = hearts, spades, diamonds, clovers
    iii. also loads the front and back of the cards 
    
4. Instantiation of the cards per rank and type

5. testing screen
    i. checking the images load and methods 
    
