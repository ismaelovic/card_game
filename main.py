from generator import generate_cards, generate_with_gemini 
from games import get_game_data
import os

# Suppress gPRC logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

def display_menu():
    """Displays the game selection menu."""
    print("\nSelect a game to generate cards for:")
    print("1. Encrypted")
    print("2. Reverse Trivia")
    print("3. Logic")
    print("4. Mime it")
    print("5. You laugh you lose")
    print("0. Exit")

def display_card(card, game_name):
    """Displays a single card in the terminal with reveal functionality."""
    if game_name == "Encrypted":
        print("Encrypted Phrase:", card['encrypted_phrase'])
        reveal = input("Reveal Phrase? (y/n): ")
        if reveal.lower() == 'y':
            print("Original Phrase:", card['phrase'])
    elif game_name == "Reverse It":
        print("Original Word:", card['word'])
        reveal = input("Reveal Reversed Word? (y/n): ")
        if reveal.lower() == 'y':
            print("Reversed Word:", card['reversed'])
    elif game_name == "Rhyme Time":
        print("Word 1:", card['word1'])
        reveal = input("Reveal Rhyme? (y/n): ")
        if reveal.lower() == 'y':
            print("Rhyme:", card['word2'])

def main():
    while True:
        # Display the game selection menu
        display_menu()
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                break  # Exit the program

            game_data = get_game_data(choice)
            if game_data:
                examples, game_name, game_description = game_data
                while True:
                    try:
                        num_cards_to_generate = int(input("How many cards to generate?"))
                        if 1 <= num_cards_to_generate <= 20:
                            break
                        elif num_cards_to_generate > 20:
                            print("Whoa there, card shark! Generating that many cards might cause the LLM to have an existential crisis (and probably take a while). Let's aim for 20 or fewer, shall we?")
                        else:
                            print("Please enter a number between 1 and 20.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                generated_cards = generate_cards(
                    num_cards_to_generate, examples, game_name, game_description, generate_with_gemini
                )

                if generated_cards:
                    print(f"\n{game_name} Cards:")
                    for card in generated_cards:
                        display_card(card, game_name)
                        print("-" * 20 + "\n")  # Separator between cards
                else:
                    print("Could not generate cards. Please check your prompt or LLM connection")
            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")
    
if __name__ == "__main__":
    main()