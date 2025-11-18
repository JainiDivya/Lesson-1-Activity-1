import colorama

from colorama import Fore, Style
from textblob import TextBlob

# Initializee coloroma for colored output
colorama.init()

# Emoji's for the start of program
print(f"{Fore.CYAN} Welcome to sentiment spy ! {Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA} Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent" #Fall back if user doesn't provide a name

# store conversation in a list of tuples: (text, polarity, sentiment_type)
conversation_history = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name} !")
print(f" Type a sentence I will analyze your sentences with TextBlob and shown you the sentiment. ")
print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN},"
      f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    
    if not user_input:
        print(f"{Fore.RED}Please enter some valid text or command.{Style.RESET_ALL}")
        continue

    if user_input.lower() == 'exit':
        print(f"{Fore.BLUE}exciting sentiment spy. Farewell, Agent {user_name}! {Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN} All conversation hostory cleared! {Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History: {Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):

                #Choose color and e,moji based on sentiment
                if sentiment_type == "Positive":
                    color = Fore.GREEN

                elif sentiment_type == "Negative":
                    color = Fore.RED

                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(f"{idx}. {color}{emoji} {text}"
                      f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")

        continue
    # Analyze Statement
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😀"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😥"
    else:
        sentiment_type = "Neytral"
        color = Fore.YELLOW
        emoji = "😐"

    #Store in history
    conversation_history.append((user_input, polarity, sentiment_type))  

    # Print result with color, emojis, and polarity
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
          f" (polarity: {polarity: 2f}){Style.RESET_ALL}")
                      










