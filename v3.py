import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
FONT_SIZE = 30
BACKGROUND_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
CHOICES = ["aroygya setu", "aroygya vati", "aroygya nothing"]

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Korona Game')
font = pygame.font.Font(None, FONT_SIZE)

def display_message(message, position):
    text = font.render(message, True, TEXT_COLOR)
    screen.blit(text, position)

def get_choice(player):
    """
    Prompts the player to make a choice by pressing a number key (1, 2, 3)
    from either the main keyboard or the numpad.
    """
    choice = None
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # Check for both number row and numpad keys
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    choice = 0
                elif event.key in [pygame.K_2, pygame.K_KP2]:
                    choice = 1
                elif event.key in [pygame.K_3, pygame.K_KP3]:
                    choice = 2
    return choice

def main():
    # Initialize scores and player roles
    speaker_score = 0
    thinker_score = 0
    rounds = 5
    current_round = 1
    speaker = "Ram"
    thinker = "Shyam"

    while current_round <= rounds:
        screen.fill(BACKGROUND_COLOR)
        display_message(f"Round {current_round}/{rounds}", (20, 20))
        display_message(f"{speaker} (Speaker) Score: {speaker_score}", (20, 60))
        display_message(f"{thinker} (Thinker) Score: {thinker_score}", (20, 100))
        pygame.display.flip()

        # Speaker says "Aroygya..."
        time.sleep(2)  # Wait 2 seconds before showing choices
        screen.fill(BACKGROUND_COLOR)
        display_message(f"{speaker} says: Aroygya...", (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50))
        pygame.display.flip()
        time.sleep(5)

        # Thinker's choice
        screen.fill(BACKGROUND_COLOR)
        display_message(f"{thinker}, choose your option (1, 2, or 3):", (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
        pygame.display.flip()
        thinker_choice = get_choice(thinker)

        # Clear the screen before showing speaker's turn
        screen.fill(BACKGROUND_COLOR)
        display_message(f"{speaker}, choose your option (1, 2, or 3):", (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
        pygame.display.flip()
        speaker_choice = get_choice(speaker)

        # Show speaker's chosen phrase
        screen.fill(BACKGROUND_COLOR)
        display_message(f"{speaker} chose: {CHOICES[speaker_choice]}", (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
        pygame.display.flip()
        time.sleep(3)

        # Determine winner
        if thinker_choice == speaker_choice:
            thinker_score += 1
            result_message = f"{thinker} wins this round!"
            # Swap roles
            speaker, thinker = thinker, speaker
        else:
            speaker_score += 1
            result_message = f"{speaker} wins this round!"

        # Display result
        screen.fill(BACKGROUND_COLOR)
        display_message(result_message, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
        pygame.display.flip()
        time.sleep(3)

        current_round += 1

    # End of game
    winner = speaker if speaker_score > thinker_score else thinker
    screen.fill(BACKGROUND_COLOR)
    display_message(f"Game Over! {winner} wins!", (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
    pygame.display.flip()
    time.sleep(5)

    pygame.quit()

if __name__ == "__main__":
    main()
