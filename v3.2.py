import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FONT_SIZE = 30
BACKGROUND_COLOR = (0,0,0)
THINKER_COLOR = (135,153,255)
SPEAKER_COLOR = (255,135,135)
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
    Prompts the player to make a choice by pressing a number key (1, 2, 3).
    """
    choice = None
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    choice = int(event.unicode) - 1
    return choice

def main():
    # Initialize scores
    speaker_score = 0
    thinker_score = 0
    rounds = 7
    current_round = 1

    while current_round <= rounds:
        screen.fill(BACKGROUND_COLOR)
        display_message(f"Round {current_round}/{rounds}", (20, 20))
        display_message(f"Speaker Score: {speaker_score}", (20, 60))
        display_message(f"Thinker Score: {thinker_score}", (20, 100))
        pygame.display.flip()

        # Speaker says "Aroygya..."
        time.sleep(2)  # Wait 2 seconds before showing choices
        screen.fill(BACKGROUND_COLOR)
        display_message("Speaker says: Aroygya...", (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50))
        pygame.display.flip()
        time.sleep(5)

        # Thinker's choice
        screen.fill(THINKER_COLOR)
        display_message("Thinker, choose your option (1, 2, or 3):", (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
        pygame.display.flip()
        thinker_choice = get_choice("Thinker")

        # Clear the screen before showing speaker's turn
        screen.fill(SPEAKER_COLOR)
        display_message("Speaker, choose your option (1, 2, or 3):", (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
        pygame.display.flip()
        speaker_choice = get_choice("Speaker")

        # Show speaker's chosen phrase
        screen.fill(SPEAKER_COLOR)
        display_message(f"Speaker chose: {CHOICES[speaker_choice]}", (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
        pygame.display.flip()
        time.sleep(3)

        # Determine winner
        if thinker_choice == speaker_choice:
            thinker_score += 1
            result_message = "Thinker wins this round!"
        else:
            speaker_score += 1
            result_message = "Speaker wins this round!"

        # Display result
        screen.fill(BACKGROUND_COLOR)
        display_message(result_message, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
        pygame.display.flip()
        time.sleep(3)

        current_round += 1

    # End of game
    winner = "Thinker" if thinker_score > speaker_score else "Speaker"
    screen.fill(BACKGROUND_COLOR)
    display_message(f"Game Over! {winner} wins!", (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
    pygame.display.flip()
    time.sleep(5)

    pygame.quit()

if __name__ == "__main__":
    main()
