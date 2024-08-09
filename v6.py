import pygame
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

# Load and set the custom icon
logo = pygame.image.load('logo.png')
pygame.display.set_icon(logo)

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

def enter_player_names():
    """
    Display the screen for entering player names and handle input.
    Default names are used if no input is given.
    """
    input_box_speaker = pygame.Rect(150, 150, 140, 32)
    input_box_thinker = pygame.Rect(150, 200, 140, 32)

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')

    active_speaker = False
    active_thinker = False

    text_speaker = ''
    text_thinker = ''

    color_speaker = color_inactive
    color_thinker = color_inactive

    while True:
        screen.fill(BACKGROUND_COLOR)
        display_message("Enter Player Names", (SCREEN_WIDTH//2 - 100, 100))
        display_message("Speaker:", (50, 155))
        display_message("Thinker:", (50, 205))

        pygame.draw.rect(screen, color_speaker, input_box_speaker, 2)
        pygame.draw.rect(screen, color_thinker, input_box_thinker, 2)

        text_surface_speaker = font.render(text_speaker, True, TEXT_COLOR)
        text_surface_thinker = font.render(text_thinker, True, TEXT_COLOR)

        screen.blit(text_surface_speaker, (input_box_speaker.x+5, input_box_speaker.y+5))
        screen.blit(text_surface_thinker, (input_box_thinker.x+5, input_box_thinker.y+5))

        input_box_speaker.w = max(100, text_surface_speaker.get_width()+10)
        input_box_thinker.w = max(100, text_surface_thinker.get_width()+10)

        # Submit button
        submit_button = pygame.Rect(250, 300, 100, 32)
        pygame.draw.rect(screen, color_inactive, submit_button)
        display_message("Submit", (submit_button.x+10, submit_button.y+5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_speaker.collidepoint(event.pos):
                    active_speaker = not active_speaker
                else:
                    active_speaker = False
                if input_box_thinker.collidepoint(event.pos):
                    active_thinker = not active_thinker
                else:
                    active_thinker = False

                # Check for submit button click
                if submit_button.collidepoint(event.pos):
                    return text_speaker if text_speaker else "Ram", text_thinker if text_thinker else "Shyam"

                # Change the color of the input boxes based on active status
                color_speaker = color_active if active_speaker else color_inactive
                color_thinker = color_active if active_thinker else color_inactive

            if event.type == pygame.KEYDOWN:
                if active_speaker:
                    if event.key == pygame.K_RETURN:
                        active_speaker = False
                    elif event.key == pygame.K_BACKSPACE:
                        text_speaker = text_speaker[:-1]
                    else:
                        text_speaker += event.unicode

                if active_thinker:
                    if event.key == pygame.K_RETURN:
                        active_thinker = False
                    elif event.key == pygame.K_BACKSPACE:
                        text_thinker = text_thinker[:-1]
                    else:
                        text_thinker += event.unicode

def main():
    # Initialize scores and player roles
    speaker_score = 0
    thinker_score = 0
    rounds = 5
    current_round = 1

    # Get player names
    speaker, thinker = enter_player_names()

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
