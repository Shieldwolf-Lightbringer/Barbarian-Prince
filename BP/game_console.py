import pygame
import os

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
        self.scroll_offset = 0

    def render_area(self, surface=None):
        self.console_area_height = int((self.screen.get_height() * self.height_ratio) - 40)
        self.console_area = pygame.Surface((self.screen.get_width() - 40, self.console_area_height))
        self.console_area.fill((220, 215, 175))
        if surface:
            surface.blit(self.console_area, (20, self.screen.get_height() - self.console_area_height - 20))
        else:
            self.screen.blit(self.console_area, (20, self.screen.get_height() - self.console_area_height - 20))

    def render_text(self, surface=None):
        self.max_displayed_lines = 5 #int(console_area_height // self.font.get_linesize())
        start_index = max(0, len(self.console_lines) - self.max_displayed_lines - self.scroll_offset)
        visible_lines = self.console_lines[start_index:start_index + self.max_displayed_lines]

        y_position = 0

        for line, requires_input in visible_lines:
            text_surface = self.font.render(line, True, ("black"))
            self.console_area.blit(text_surface, (20, y_position))
            y_position += self.font.get_linesize()

            if requires_input:
            # Render an indicator that more input is needed for this message
                input_required_surface = self.font.render("What is your choice? " + self.input_buffer, True, (255, 0, 0))
                self.console_area.blit(input_required_surface, (20, y_position))
                y_position +=  self.font.get_linesize()

        # Render input buffer
        input_surface = self.font.render(">>> " + self.input_buffer, True, (80, 80, 80))
        self.console_area.blit(input_surface, (20, y_position))
        #console_area.blit(input_surface, (20, console_area_height - self.font.get_linesize()))

        # Render cursor blink
        self.cursor_blink_timer += pygame.time.get_ticks()
        if self.cursor_blink_timer // 500 % 2 == 0:
            cursor_pos = 20 + self.font.size(">>> " + self.input_buffer)[0]
            pygame.draw.line(self.console_area, (80, 80, 80), (cursor_pos, y_position),
                             (cursor_pos, y_position + self.font.get_linesize()), 2)
        else:
            cursor_pos = 20 + self.font.size(">>> " + self.input_buffer)[0]
            pygame.draw.line(self.console_area, (220, 215, 175), (cursor_pos, y_position),
                             (cursor_pos, y_position + self.font.get_linesize()), 2)

        if surface:
            surface.blit(self.console_area, (20, self.screen.get_height() - self.console_area_height - 20))
        else:    
            self.screen.blit(self.console_area, (20, self.screen.get_height() - self.console_area_height - 20))
            


    def add_line(self, text, requires_input=False):
        if text not in self.displayed_messages:
            self.log_message(text)
            self.displayed_messages.add(text)
            self.console_lines.append((text, requires_input))


    def handle_input(self, event):
        if event.type == pygame.TEXTINPUT:
            self.input_buffer += event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                command_result = self.execute_command()
                if command_result is not None:
                    return command_result
            elif event.key == pygame.K_BACKSPACE:
                self.input_buffer = self.input_buffer[:-1]
            elif event.key == pygame.K_UP:
                self.scroll_down()
            elif event.key == pygame.K_DOWN:
                self.scroll_up()

    
    def handle_player_response(self):
        for event in pygame.event.get():
            if event.type == pygame.TEXTINPUT:
                self.input_buffer += event.text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.input_buffer


    def execute_command(self):
        command = self.input_buffer.strip().lower()
        if command:
            self.clear_console()
            self.add_line(">>> " + command)  # Echo the command back to the console
            return command


    def display_message(self, message, requires_input=False):
        self.wrap_text(message, requires_input)


    def clear_console(self):
        self.console_lines = []
        self.input_buffer = ""
        self.displayed_messages = set()
        self.scroll_offset = 0


    def scroll_up(self):
        self.scroll_offset = max(0, self.scroll_offset - 1)


    def scroll_down(self):
        max_displayed_lines = 6 #int((self.screen.get_height() * self.height_ratio - 40) / self.font.get_linesize())
        max_scroll_offset = max(0, len(self.console_lines) - max_displayed_lines)
        self.scroll_offset = min(max_scroll_offset, self.scroll_offset + 1)


    def wrap_text(self, text, requires_input=False):
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            test_width, _ = self.font.size(test_line)

            if test_width <= (self.screen.get_width() * 0.9):
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "

        lines.append(current_line)
        
        for line in lines:
            self.add_line(line, requires_input)


    def create_log(self):
        with open('game_log.txt', 'a') as log_file:
            pass
        with open('game_log.txt', 'w') as log_file:
            log_file.write('Welcome to a new game.' + '\n')


    def log_message(self, message):
        with open('game_log.txt', 'a') as log_file:
            log_file.write(message + '\n')