#Choose You Own Adventure Game, for Danny
import time

def fireManGame():
    print("""Today is your first day on Fire Crew 317, welcome to the crew!\n..And guess what!  Do you hear that?  That's the alarm bell,
time to respond to your first call!
    A man called to say he smells gas in his house, we need to go check it out, do we...
    (a), speed to the house with our sirens on?
    (b), drive the speed limit with no sirens?""")
    choiceOne = input()
    if choiceOne == 'a':      
        print("""You turn on your sirens and speed to the house, getting there quickly but also safely
        You see the man and his family standing outside on the curb, they tell you when they woke up, the whole house smelled like gas
        Do you...
                (a), rush in the house to identify the source of the gas?
                (b), find the main gas line and shut it off before going inside?""")
        choiceTwo = input()
        if choiceTwo == 'a':
              print('You rush in the house, only to hear the fire chief scream at you that you forgot to turn the gas off!')
        elif choiceTwo == 'b':
              print('You find the main gas line, and shut if off before going inside.')
        
    elif choiceOne == 'b':              
          print("""You leave the station without your sirens on, and get stuck in traffic on a busy road!
Nobody moves out of the way because they don't know there is an emergency!
Unfortunately, you didn't make it in time, the house is now full of gas and will have to be fumigated for the next 24 hours until the family can go back inside.
Game over.""")
         
       

def policeManGame():
    print("""Welcome to Police Precint 37, time for you to head out on your first shift.
    We need help in a couple areas today, would you like to...
    (a), Investigate a robbery?
    (b), Set up a speed trap?""")
    choiceOne = input()
    if choiceOne == 'a':      
        print("""Robbery it is!
        A call just came in about a gas station being robbed, you drive there quickly to secure the scene and begin investigating.
        When you arrive, you see the front door is busted out, and glass is all over the ground.
        As you approach, you see someone run out the back door in a hurry.
        Do you...
                (a), run through the front door to catch up to him?
                (b), run around the side of the gas station and try to cut him off?""")
        choiceTwo = input()
        if choiceTwo == 'a':
              print('You sprint towards the front door, but slip on the broken glass!')
        elif choiceTwo == 'b':
              print('You sprint around the side of the gas station, just in time to see the person jumping over a fence behind the building.')
        
    elif choiceOne == 'b':
        print("""Speed trap it is!""")
          #print('You leave the station without your sirens on, and get stuck in traffic on a busy road!  Nobody moves out of the way because they don\'t know there is \
#an emergency!\nUnfortunately, you didn\'t make it in time, the house is now full of gas and will have to be fumigated for the next 24 hours until the family can go back inside.\nGame over.')

#def bucketTruckGame():

#def ambulanceGame():

#def doctorGame():

#def pilotGame():

#def dannyGame():
        
fireManGame()
policeManGame

          
