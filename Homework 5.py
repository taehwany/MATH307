import random as rn
import pandas as pd
theTrials = 0
newDeck = []
aCount = 0
bCount = 0
bothABCount = 0
# Number of trials
while theTrials < 1000:
    eachSuit = 0
    eachNumber = 2
    chooseCards = 0 
    chooseFace = 0
    chooseSeven = 0
    deck = []
# The Deck 
# Does the while loop 4 times to create four suits of 13 cards
    while eachSuit < 4:
        deck.insert(0 ,'J')
        deck.insert(0 ,'Q')
        deck.insert(0 ,'K')
        deck.insert(0 ,'A')
        while eachNumber < 11:
            deck.insert(0, eachNumber)
            eachNumber = eachNumber + 1
        eachSuit = eachSuit + 1
        eachNumber = 2
# The Hand
    while chooseCards < 17: 
# The chosen card
        issaChoice = rn.choice(deck)
# If the chosen card was seven...
        if issaChoice == 7:
            chooseSeven = chooseSeven + 1
# If the chosen card was a face card...
        if issaChoice == str(issaChoice):
            chooseFace = chooseFace + 1
        deck.remove(issaChoice)
        chooseCards = 1 + chooseCards
# If the hand has more than 5 face cards...
    if chooseFace > 5:
        aCount = aCount + 1
# If the hand has less than 2 sevens...
    if chooseSeven < 2:
        bCount = bCount + 1
# If the hand has more than 5 face cards and has less than 2 sevens...
    if (chooseFace > 5 and chooseSeven < 2): 
        bothABCount = bothABCount + 1
    randomVariable = [chooseFace,chooseSeven]
    newDeck.append(randomVariable)
# All the events
    allEvents = pd.DataFrame(newDeck, columns = ['X', 'Y'])
    theTrials = theTrials + 1
print (allEvents)
print ("Event A: " )
eventA = aCount/1000
print (eventA)
print ("Event B: " )
eventB = bCount/1000
print (eventB)
print ("Event A and B: " )
print (bothABCount/1000)
print ("Event A x Event B: ")
print (eventA * eventB)
print ("To find independence, P(A ∩ B) = P(A) x P(B). It seems as though it's close but does not equate. Therefore, we can conclude that they are dependent.")
