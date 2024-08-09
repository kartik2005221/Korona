import random
import time

# Constants
CHOICES = ["aroygya setu", "aroygya vati", "aroygya nothing"]

def get_choice_input(player):
    print(f"{player}, choose your option:")
    for i, choice in enumerate(CHOICES, 1):
        print(f"{i}. {choice}")
    choice = input("Enter the number of your choice: ")
    return int(choice) - 1

def main():
    # Initialize scores
    speaker_score = 0
    thinker_score = 0
    rounds = 5
    current_round = 1

    # Start the game loop
    while current_round <= rounds:
        print(f"\nRound {current_round}/{rounds}")
        
        # Speaker's turn to say "Aroygya..."
        print("\nSpeaker says: Aroygya...")
        
        # Delay for 5 seconds to simulate thinking time
        time.sleep(5)

        # Thinker's choice
        thinker_choice = get_choice_input("Thinker")
        
        # Speaker's choice
        speaker_choice = get_choice_input("Speaker")
        
        # Show speaker's chosen phrase
        print(f"\nSpeaker chose: {CHOICES[speaker_choice]}")
        
        # Determine winner
        if thinker_choice == speaker_choice:
            print("Thinker wins this round!")
            thinker_score += 1
        else:
            print("Speaker wins this round!")
            speaker_score += 1

        # Update round
        current_round += 1

        # Display scores
        print(f"\nScores -> Speaker: {speaker_score}, Thinker: {thinker_score}")

    # End of game
    winner = "Thinker" if thinker_score > speaker_score else "Speaker"
    print(f"\nGame Over! {winner} wins!")

if __name__ == "__main__":
    main()
