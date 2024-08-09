import pygame
import time
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FONT_SIZE = 40
BACKGROUND_COLOR = (0, 0, 0)  # Pure black
TEXT_COLOR = (255, 255, 255)
SPEAKER_COLOR = (0, 128, 255)
THINKER_COLOR = (255, 128, 0)
CHOICES = ["aroygya setu", "aroygya vati", "aroygya nothing"]
ICON_PATH = "logo.png"  # Path to the window icon
BEEP_SOUND_PATH = "beep.mp3"  # Path to the beep sound file

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Aroygya (by AiR)')
font = pygame.font.Font(None, FONT_SIZE)

# Load icon and beep sound
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)
beep_sound = pygame.mixer.Sound(BEEP_SOUND_PATH)

def display_message(message, position, color=TEXT_COLOR):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)

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
                sys.exit()  # Use sys.exit() to handle quitting the program
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
    rounds = 7
    current_round = 1
    speaker = "Ram"
    thinker = "Shyam"

    while current_round <= rounds:
        screen.fill(BACKGROUND_COLOR)
        display_message(f"Round {current_round}/{rounds}", (SCREEN_WIDTH//2, 50))
        display_message(f"{speaker} (Speaker) Score: {speaker_score}", (SCREEN_WIDTH//2, 150), SPEAKER_COLOR)
        display_message(f"{thinker} (Thinker) Score: {thinker_score}", (SCREEN_WIDTH//2, 200), THINKER_COLOR)
        pygame.display.flip()

        # Speaker says "Aroygya..."
        time.sleep(2)  # Wait 2 seconds before showing choices
        beep_sound.play()  # Play beep sound
        screen.fill(BACKGROUND_COLOR)
        display_message(f"{speaker} says: Aroygya...", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50), SPEAKER_COLOR)
        pygame.display.flip()
        time.sleep(5)

        # Thinker's choice
        screen.fill(BACKGROUND_COLOR)
        display_message(f"{thinker}, choose your option (1, 2, or 3):", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), THINKER_COLOR)
        pygame.display.flip()
        thinker_choice = get_choice(thinker)

        # Clear the screen before showing speaker's turn
        screen.fill(BACKGROUND_COLOR)
        display_message(f"{speaker}, choose your option (1, 2, or 3):", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), SPEAKER_COLOR)
        pygame.display.flip()
        speaker_choice = get_choice(speaker)

        # Show speaker's chosen phrase
        screen.fill(BACKGROUND_COLOR)
        display_message(f"{speaker} chose: {CHOICES[speaker_choice]}", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), SPEAKER_COLOR)
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
        display_message(result_message, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), TEXT_COLOR)
        pygame.display.flip()
        time.sleep(3)

        current_round += 1

    # End of game
    winner = speaker if speaker_score > thinker_score else thinker
    screen.fill(BACKGROUND_COLOR)
    display_message(f"Game Over! {winner} wins!", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), TEXT_COLOR)
    pygame.display.flip()
    time.sleep(5)

    pygame.quit()

if __name__ == "__main__":
    main()
