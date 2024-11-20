import os
import sys
import langchain
# import langchain_cohere
import cohere.types
os.environ["COHERE_API_KEY"] = "Your API key"

from langchain_cohere import ChatCohere


model = ChatCohere(model="command-r")

print(model)
print(sys.path)


def puzzles(puzzleName):
    if puzzleName == "tallBuilding":
        return """A man who lives in a 30-story building decides to jump out of his window. 
        He survives the fall with no injuries. How did that happen?"""
    elif puzzleName == "hungryLions":
        return """A man is condemned to death. He has to choose from three rooms to accept his punishment. 
        The first room has a firing squad with guns loaded. The second room has a blazing fire. 
        The third room is full of tigers that haven’t eaten for six months. Which room should he choose?"""
    elif puzzleName == "walk10Flights":
        return """A woman lives on the 30th floor and hates taking the stairs. 
        Every day, she takes the elevator down to the lobby floor to go to work. 
        When she comes home from work, she takes the elevator to the 20th floor and walks the rest of the way up, except on days when it rains. 
        Those days, she takes the elevator all the way up. 
        Why does she walk the last 10 flights of stairs if she hates it so much?"""
    elif puzzleName == "screamDead":
        return """A woman opened a door, screamed and was found dead a few minutes later. 
        No gunshots were heard in the area. 
        What happened to her?"""
    elif puzzleName == "The_Missing_Dollar":
        return """Three friends go to a restaurant and decide to split the bill. The waiter tells them the total bill is ₹300. Each friend contributes ₹100, making a total of ₹300.
                After they pay, the waiter realizes he made a mistake — the actual bill was only ₹250. To correct this, he gives ₹50 back to the friends. However, the friends decide to give the waiter ₹20 as a tip and split the remaining ₹30 among themselves, each getting ₹10 back.
                Now, each friend has effectively paid ₹90 (their initial ₹100 minus the ₹10 they got back). Together, they have paid ₹270 (₹90 x 3), and the waiter has ₹20. But ₹270 + ₹20 equals ₹290, not ₹300.
                Where did the missing ₹10 go?"""
    else:
        return """Four men, one of whom was known to have committed a certain crime, 
        made the following statements when questioned by the police:
        1. Archie: Dave did it.
        2. Dave: Tony did it.
        3. Gus: I didn’t do it.
        4. Tony: Dave lied when he said I did it.
        If only one of these four statements is true, who was the guilty man?"""
