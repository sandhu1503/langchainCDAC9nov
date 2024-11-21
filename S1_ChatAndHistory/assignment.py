import os
import random
import sys
import langchain
# import langchain_cohere
import cohere.types
os.environ["COHERE_API_KEY"] = "Your API key"
from langchain_cohere import ChatCohere

model = ChatCohere(model="command-r")

print(model)
print(sys.path)


def actor_picker():
    actors = [
    "Shah Rukh Khan",
    "Priyanka Chopra",
    "Amitabh Bachchan",
    "Deepika Padukone",
    "Irrfan Khan",
    "Hrithik Roshan",
    "Katrina Kaif",
    "Nawazuddin Siddiqui",
    "Alia Bhatt",
    "Salman Khan"
    ]
    random_index = random.randint(0, len(actors) - 1)
    return actors[random_index]

def location_picker():
    locations = [
    "Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata", 
    "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Lucknow"
    ]

    random_index = random.randint(0, len(locations) - 1)
    return locations[random_index]

def theme_picker():
    themes = [
        "Adventure", "Romance", "Mystery", "Fantasy", "Sci-fi",
        "Horror", "Historical", "Comedy", "Drama", "Thriller"
    ]
    random_index = random.randint(0, len(themes) - 1)
    return themes[random_index]
