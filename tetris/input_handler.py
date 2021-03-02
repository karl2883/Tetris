import pygame


def check_input(move_left_timeout, move_right_timeout, keys, current_piece):
    fall_ready = False
    if keys[pygame.K_LEFT] and move_left_timeout < 1:
        if move_left_timeout == 0 or move_left_timeout == -1:
            current_piece.move_left()
        move_left_timeout += 1
        if move_left_timeout == 0:
            move_left_timeout = -2
    elif keys[pygame.K_LEFT] and move_left_timeout > 0:
        move_left_timeout += 1
        if move_left_timeout > 10:
            move_left_timeout = -2
    else:
        move_left_timeout = 0
    if keys[pygame.K_RIGHT] and move_right_timeout < 1:
        if move_right_timeout == 0 or move_right_timeout == -1:
            current_piece.move_right()
        move_right_timeout += 1
        if move_right_timeout == 0:
            move_right_timeout = -2
    elif keys[pygame.K_RIGHT] and move_right_timeout > 0:
        move_right_timeout += 1
        if move_right_timeout > 10:
            move_right_timeout = -2
    else:
        move_right_timeout = 0
    if keys[pygame.K_DOWN]:
        fall_ready = True
    return move_left_timeout, move_right_timeout, fall_ready
