print("Hello I'm AI Bot. What's your name? :")
name = input()
print(f"Nice to meet you, {name}!")
print("How are you feeling today? (good/bad) : ")
mood = input().lower()

if mood == "good":
    print("I am glad to hear that")
elif mood == "bad":
    print("I'm sorry to hear that. Hope to get things better soon!")
else:
    print(" I see sometimes feelings are put into words")    




print("It was nice chatting with you {name}. Goodbye!")

