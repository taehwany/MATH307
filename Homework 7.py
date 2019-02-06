import random as rn
import pandas as pd
theTrials = 0
newDeck = []
aCount = 0
bCount = 0
bothABCount = 0
totalAnswer = 0
# Number of trials
while theTrials < 5000:
    eachSuit = 0
    eachNumber = 2
    chooseCards = 0 
    chooseAce = 0
    chooseSeven = 0
    secondValue = 0
    deck = []
    firstValue = []
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
# If the chosen card was a seven...
        if issaChoice == 7:
            chooseSeven = chooseSeven + 1
# If the chosen card was an ace...
        if issaChoice == "A":
            chooseAce = chooseAce + 1
# Remove the card when it is chosen from the deck
        deck.remove(issaChoice)
        chooseCards = 1 + chooseCards
# Make into list
# Ace and seven count
    firstValue = [chooseAce, chooseSeven]
# Point value
    secondValue = ((3*(chooseAce**2))+((2**chooseSeven)))
# List of counts and point value
    randomVariable = [firstValue, secondValue]
# Append list into a bigger list
    newDeck.append(randomVariable)
# The DATAFRAME
    allEvents = pd.DataFrame(newDeck, columns = ['Aces, Sevens', '3m^2 + 2^n'])
# Counts all the point values together    
    totalAnswer = secondValue + totalAnswer
    theTrials = theTrials + 1
# Print the DATAFRAME
print (allEvents)
# Print the total point value
print ("All the point values equate to:", totalAnswer)
expectValue = 0
# Total point value divided by number of trials
expectValue = (totalAnswer)/(theTrials + 1)
# Print the expected value
print ("The expected value is:", expectValue)
print ("After multiple 5,000 trials, it seems as though the expected value is around 10.5-10.7. We can conclude that that appromiately 10.6 is our expected value.")