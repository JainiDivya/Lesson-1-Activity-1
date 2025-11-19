import re, random
from colorama import Fore, init

# # Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# # Destination & joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# # Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
     return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)

def recommend():
     print(f"{Fore.CYAN}Chatbot: Beaches, Mountains or Cities?")
     preference= input(f"{Fore.YELLOW}You: ").lower()
     preference= normalize_input(preference)

     if preference in destinations:
          suggestion= random.choice(destinations[preference])
          print(f"{Fore.CYAN}Chatbot: How about {suggestion}")
          answer= input("Do you like it? [Y/N]").lower()

          if answer== "yes":
               print(f"{Fore.GREEN}Chatbot: Awesome! Enjoy {suggestion}!")
          elif answer== "no":
               print(f"{Fore.RED}Chatbot: I'll give you another suggestion.")  
               recommend()
          else:
               print(f"{Fore.RED}Chatbot: How about another suggestion.")
               recommend()
     else:
          print(f"{Fore.YELLOW}Chatbot: I don't think I have that type of destination...")

          show_help()             

# Offer packing tips based on user’s destination and duration
def packing_tips():
     print(f"{Fore.CYAN}Chatbot: Where to?")
     location= normalize_input(input(f"{Fore.YELLOW}You: "))
     print(f"{Fore.CYAN}Chatbot: How many days")
     days= int(input(f"{Fore.YELLOW}You: "))

     print(f"{Fore.GREEN}Chatbot: Packing tips for {days} days in {location}: ")
     print(f"{Fore.GREEN}-Pack versatile clothes")
     print(f"{Fore.GREEN}-Bring chatgers/adapters")
     print(f"{Fore.GREEN}-Check the weather forecast")

# Tell a random joke
def tell_joke():
     print(f"{Fore.YELLOW}Travelbot: {random.choice(jokes)}")     

#Show weather forecast
def tell_weather():
     place= input((f"{Fore.YELLOW}Chatbot: Which city are you going to from the one's I have suggested?"))
     place= normalize_input(place)

     if place in destinations["beaches"]:
          print(f"{Fore.GREEN}Chatbot: The temperature while be hot at day and cool at night.")
     elif place in destinations["cities"]:
          print(f"{Fore.GREEN}Chatbot: Temperature will be slightly hot and humid due to pollution and crowd.")
     elif place in destinations["mountains"]:
          print(f"{Fore.GREEN}Chatbot: This place has a very cold-cool temperature with snow all around.")
     else:
          print(f"{Fore.RED}Chatbot: I don't think I have that place in my catalogue...")          
          
#Describe places of travel
def travel_desc():
     place= input((f"{Fore.YELLOW}Chatbot: Which city are you going to from the one's I have suggested?"))

     if place in destinations["beaches"]:
          print(f"{Fore.GREEN}Chatbot: The scenery is calming and peaceful with the sandy shore outlooking unto the blue sea and the sun shining upon the glistening ground.")
     elif place in destinations["cities"]:
          print(f"{Fore.GREEN}Chatbot: This bustling city while feel like an adventure. Skyscrapers in one place and citizens on another, the city is confusing yet beautiful.")
     elif place in destinations["mountains"]:
          print(f"{Fore.GREEN}Chatbot: The coldness of the mountain is in stark contrast to the spicy adventure that awaits you. The treacherous yet beautiful landscape of the mountain is sure to bring some fun to your life.")
     else:
          print(f"{Fore.RED}Chatbot: I don't think I have that place in my catalogue...") 


# Display help menu
def show_help():
     print(f"{Fore.CYAN}\nChatbot: I can")
     print(f"{Fore.GREEN}- Suggest travel reccomendations(say 'recommened')")
     print(f"{Fore.GREEN}- Offer packing tips(say 'packing')")
     print(f"{Fore.GREEN}- Tell a joke(say 'joke')")
     print(f"{Fore.GREEN}- Give the weather forecast for a place(say 'weather')")
     print(f"{Fore.GREEN}- Describe places to go to(say describe)")
# Main chat loop
def chat():
     print(f"{Fore.YELLOW}Chatbot: Hello! I am your personal travel chatbot.")
     name= input(f"{Fore.YELLOW}Chatbot: Your name? ")
     print(f"{Fore.GREEN}Nice to meet you, {name}!")

     show_help()

     while True:
          user_input= input(f"{Fore.YELLOW}{name}: ")
          user_input= normalize_input(user_input)

          if "recommened" in user_input or "suggest" in user_input:
               recommend()
          elif "pack" in user_input or "packing" in user_input:
               packing_tips()
          elif "joke" in user_input or "funny" in user_input:
               tell_joke()
          elif "weather" in user_input or "climate" in user_input:
               tell_weather()
          elif "describe" in user_input or "tell" in user_input or "place" in user_input:
               travel_desc()     
          elif "help" in user_input:
               show_help()
          elif "exit" in user_input or "bye" in user_input:
               print(f"{Fore.GREEN}Chatbot: Safe travels! Goodbye!")
               break
          else:
               print(f"{Fore.YELLOW}Could you rephrase?")                   

# Run the chatbot
if __name__ == "__main__":
    chat()