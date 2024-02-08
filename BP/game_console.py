import pygame
import sys

class Console:
    def __init__(self, screen, font, width_ratio, height_ratio):
        self.screen = screen
        self.font = font
        self.width_ratio = width_ratio
        self.height_ratio = height_ratio

        self.console_lines = []
        self.input_buffer = ""
        self.cursor_blink_timer = 0

        self.displayed_messages = set()

    def render(self):
        console_area_height = int((self.screen.get_height() * self.height_ratio) - 40)
        console_area = pygame.Surface((self.screen.get_width() - 40, console_area_height))
        console_area.fill((220, 215, 175))

        y_position = 0
        for line, requires_input in self.console_lines:
            text_surface = self.font.render(line, True, ("black"))
            console_area.blit(text_surface, (20, y_position))
            y_position += self.font.get_linesize()

            if requires_input:
            # Render an indicator that more input is needed for this message
                input_required_surface = self.font.render("<Press any key to continue>", True, (255, 0, 0))
                console_area.blit(input_required_surface, (20, y_position))
                y_position +=  self.font.get_linesize()
                break  # Only render the input indicator for the first message that requires input


        # Render input buffer
        input_surface = self.font.render(">>> " + self.input_buffer, True, (80, 80, 80))
        console_area.blit(input_surface, (20, y_position))

        # Render cursor blink
        self.cursor_blink_timer += pygame.time.get_ticks()
        if self.cursor_blink_timer // 500 % 2 == 0:
            cursor_pos = 20 + self.font.size(">>> " + self.input_buffer)[0]
            pygame.draw.line(console_area, (80, 80, 80), (cursor_pos, y_position),
                             (cursor_pos, y_position + self.font.get_linesize()), 2)
        else:
            cursor_pos = 20 + self.font.size(">>> " + self.input_buffer)[0]
            pygame.draw.line(console_area, (220, 215, 175), (cursor_pos, y_position),
                             (cursor_pos, y_position + self.font.get_linesize()), 2)
            
        self.screen.blit(console_area, (20, self.screen.get_height() - console_area_height - 20))

    def add_line(self, text, requires_input=False):
        if text not in self.displayed_messages:
            self.displayed_messages.add(text)
            self.console_lines.append((text, requires_input))
            max_lines = int(self.screen.get_height() * self.height_ratio / self.font.get_linesize())
            if len(self.console_lines) > max_lines:
                self.console_lines.pop(0)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.execute_command()
            elif event.key == pygame.K_BACKSPACE:
                self.input_buffer = self.input_buffer[:-1]
            else:
                self.input_buffer += event.unicode

    def execute_command(self):
        command = self.input_buffer.strip()
        if command:
            self.add_line(">>> " + command)  # Echo the command back to the console
            # TODO: Add logic to handle commands based on your game's requirements
            self.input_buffer = ""  # Clear the input buffer

    def display_message(self, message, requires_input=False):
        self.add_line(message, requires_input)

    def clear_console(self):
        self.console_lines = []
        self.displayed_messages = set()
        
