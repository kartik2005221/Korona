import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FONT_SIZE = 32
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
CHOICES = ["aroygya setu", "aroygya vati", "aroygya nothing"]

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Korona Game')
font = pygame.font.Font(None, FONT_SIZE)

# Game variables
speaker_score = 0
thinker_score = 0
rounds = 5
current_round = 1

def display_message(message, position):
    text = font.render(message, True, TEXT_COLOR)
    screen.blit(text, position)

def main():
    global speaker_score, thinker_score, current_round
    running = True

    while running and current_round <= rounds:
        screen.fill(BACKGROUND_COLOR)

        # Display scores and round
        display_message(f"Round {current_round}/{rounds}", (20, 20))
        display_message(f"Speaker Score: {speaker_score}", (20, 60))
        display_message(f"Thinker Score: {thinker_score}", (20, 100))

        # Speaker's turn
        speaker_choice = random.choice(CHOICES)
        display_message("Speaker says: Aroygya...", (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50))
        pygame.display.flip()
        time.sleep(5)  # 3-second thinking time

        # Thinker's choice
        thinker_choice = random.choice(CHOICES)

        # Reveal speaker's choice
        display_message(f"Speaker chose: {speaker_choice}", (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2))
        pygame.display.flip()
        time.sleep(2)

        # Determine winner
        if thinker_choice == speaker_choice:
            thinker_score += 1
            current_round += 1
        else:
            speaker_score += 1
            current_round += 1

        # Check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        time.sleep(2)  # Pause before next round

    # End of game
    screen.fill(BACKGROUND_COLOR)
    winner = "Thinker" if thinker_score > speaker_score else "Speaker"
    display_message(f"Game Over! {winner} wins!", (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2))
    pygame.display.flip()
    time.sleep(5)

    pygame.quit()

if __name__ == "__main__":
    main()
