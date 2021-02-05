# Copyright (C) 2020 Vafiadis Panagiotis
#
# Computer Science Department Faculty of Sciences - Campus of Kavala
# International Hellenic University
#
# MPhil in Advanced Technologies in Informatics and Computers
# Advanced Programming and Rich Internet Applications
#
# This is free software and you are welcome to redistribute it
# under certain conditions.
# Copyright (C) 2020 Vafiadis Panagiotis
#
# Computer Science Department Faculty of Sciences - Campus of Kavala
# International Hellenic University
#
# MPhil in Advanced Technologies in Informatics and Computers
# Advanced Programming and Rich Internet Applications
#
# This is free software and you are welcome to redistribute it
# under certain conditions.


import json
import logging
import tempfile

import chess
import chess.engine
import chess.svg
from cairosvg import svg2png


def make_tmp_file():
    return (tempfile.NamedTemporaryFile(prefix='chessbot-images_', suffix=".png")).name


def run_command(user_context, update, context, reply):
    if is_json(reply):
        parsed_json = json.loads(reply)

        if 'command' in parsed_json:
            command_name = parsed_json['command']
            logging.info("Bot sent the command: '%s'" % command_name)
            logging.info(reply)

            if command_name in all_commands:
                all_commands[command_name](user_context, update, context, parsed_json)
            else:
                logging.error("Invalid Command '%s'." % command_name)
        else:
            logging.info("Invalid Json cannot find 'command' keyword.")
    else:
        show_text(user_context, update, context, reply)


def is_json(json_string):
    try:
        json.loads(json_string)
    except ValueError as e:
        return False
    return True


def render_board(board, file_name, size=900):
    svg_code = chess.svg.board(board, size=size)
    svg2png(bytestring=svg_code, write_to=file_name)


def show_text(user_context, update, context, reply):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=reply)


def generate_chessboard_image(user_context, update, context, reply):
    chat_id = update.effective_chat.id
    board_description = reply['board']
    board = chess.Board(board_description)
    temp_name = make_tmp_file()
    render_board(board, temp_name)
    context.bot.send_photo(chat_id=chat_id, photo=open(temp_name, 'rb'))
    if 'msg' in reply:
        context.bot.send_message(chat_id=chat_id, text=reply['msg'])


def new_game(user_context, update, context, reply):
    chat_id = update.effective_chat.id
    user_context.board = chess.Board()
    temp_name = make_tmp_file()
    render_board(user_context.board, temp_name)
    context.bot.send_photo(chat_id=chat_id, photo=open(temp_name, 'rb'))
    context.bot.send_message(chat_id=chat_id, text='Your turn')


def show_image(user_context, update, context, reply):
    chat_id = update.effective_chat.id
    image_name = reply['image']
    msg = reply['msg']
    context.bot.send_photo(chat_id=chat_id, photo=open('images/' + image_name, 'rb'))
    context.bot.send_message(chat_id=chat_id, text=msg)


def pawn_promotes(user_context, update, context, reply):
    chat_id = update.effective_chat.id
    piece = reply['piece'].lower()
    board_description = "8/5kP1/7P/7K/8/8/3p4/8 w - - 0 1"
    msg = ("Pawn promotion occurs when a pawn reaches the farthest rank from its original square—the eighth rank "
           "for White and first rank for Black. When this happens, the player can replace the pawn for a queen, "
           "a rook, a bishop, or a knight. Most of the time, players promote a pawn to a queen.")
    arrows = [chess.svg.Arrow(chess.D2, chess.D1),
              chess.svg.Arrow(chess.G7, chess.G8)]
    board = chess.Board(board_description)
    squares = board.attacks(chess.E4)
    temp_name = make_tmp_file()
    svg_code = chess.svg.board(board, arrows=arrows, squares=squares, size=900)
    svg2png(bytestring=svg_code, write_to=temp_name)
    context.bot.send_photo(chat_id=chat_id, photo=open(temp_name, 'rb'))
    context.bot.send_message(chat_id=chat_id, text=msg)


# {"command": "piece-move", "piece":"<star>"}
def piece_move(user_context, update, context, reply):
    chat_id = update.effective_chat.id
    piece = reply['piece'].lower()

    if piece == 'king':
        board_description = "8/8/8/3K4/8/8/8/8 w - - 0 1"
        msg = "The king can move or capture one square in any direction"
        board = chess.Board(board_description)
        squares = board.attacks(chess.D5)
        temp_name = make_tmp_file()
        svg_code = chess.svg.board(board, squares=squares, size=900)

    elif piece == 'queen':
        board_description = "8/8/8/3Q4/8/8/8/8 w - - 0 1"
        msg = "The Queen can move or capture as far it wants in any direction"
        board = chess.Board(board_description)
        squares = board.attacks(chess.D5)
        temp_name = make_tmp_file()
        svg_code = chess.svg.board(board, squares=squares, size=900)

    elif piece == 'rook':
        board_description = "8/8/8/3R4/8/8/8/8 w - - 0 1"
        msg = ("The Rook can move or capture horizontally or vertically like"
               "the Queen, but lacks the power to move diagonally.")
        board = chess.Board(board_description)
        squares = board.attacks(chess.D5)
        temp_name = make_tmp_file()
        svg_code = chess.svg.board(board, squares=squares, size=900)

    elif piece == 'bishop':
        board_description = "8/8/8/3B4/8/8/8/8 w - - 0 1"
        msg = ("The Bishop is limited to diagonal moves or captures, "
               "it cannot move horizontally or vertically")
        board = chess.Board(board_description)
        squares = board.attacks(chess.D5)
        temp_name = make_tmp_file()
        svg_code = chess.svg.board(board, squares=squares, size=900)

    elif piece == 'knight' or piece == 'horse':
        board_description = "8/8/8/3N4/8/8/8/8 w - - 0 1"
        msg = ("The Knight moves to squares reached by going two squares "
               "vertically or horizontally, and one square to the left or right.")
        board = chess.Board(board_description)
        squares = board.attacks(chess.D5)
        temp_name = make_tmp_file()
        svg_code = chess.svg.board(board, squares=squares, size=900)

    elif piece == 'pawn':
        board_description = "rnbqk1nr/pppp1ppp/8/4p3/4P3/b4P2/PPPP2PP/RNBQKBNR w KQkq - 0 1"
        msg = ("The Pawn, unlike the other pieces, moves in one fashion and "
               "captures in another. The Pawn moves forward, never backward "
               "one square at a time. However, when the Pawn is on its "
               " original square, it has the option of advancing one or two "
               "squares on it's first move. The Pawn captures diagonally "
               " forward to the left or right. Learn what is promotion and how pawn promotes by asking."
               )
        arrows = [chess.svg.Arrow(chess.B2, chess.A3),
                  chess.svg.Arrow(chess.B2, chess.B3),
                  chess.svg.Arrow(chess.B2, chess.B4)]
        board = chess.Board(board_description)
        squares = board.attacks(chess.E4)
        temp_name = make_tmp_file()
        svg_code = chess.svg.board(board, arrows=arrows, squares=squares, size=900)

    else:
        board_description = "rnbqk3/p7/8/8/8/8/P7/RNBQK3 w - - 0 1"
        msg = "A chess piece can be king, queen, rook, bishop, knight, or pawn"
        board = chess.Board(board_description)
        temp_name = make_tmp_file()
        svg_code = chess.svg.board(board, size=900)

    svg2png(bytestring=svg_code, write_to=temp_name)
    context.bot.send_photo(chat_id=chat_id, photo=open(temp_name, 'rb'))
    context.bot.send_message(chat_id=chat_id, text=msg)


def new_move(user_context, update, context, reply):
    chat_id = update.effective_chat.id
    move_coords = reply['move']
    board = user_context.board

    try:
        user_move = chess.Move.from_uci(move_coords)
        if user_move in board.legal_moves:
            board.push(user_move)
            result = user_context.engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)
            temp_name = make_tmp_file()

            mv = chess.Move.from_uci(result.move.uci())

            svg_code = chess.svg.board(board,
                                       lastmove=mv,
                                       size=900)
            svg2png(bytestring=svg_code, write_to=temp_name)
            context.bot.send_photo(chat_id=chat_id, photo=open(temp_name, 'rb'))

            if board.is_game_over():
                update.message.reply_text("The game is over")
                user_context.bot.set_uservar(user_context.id, 'topic', 'random')
            else:
                update.message.reply_text("Your turn")
        else:
            raise Exception

    except Exception as e:
        logging.warning(e)
        temp_name = make_tmp_file()
        render_board(board, temp_name)
        context.bot.send_photo(chat_id=chat_id, photo=open(temp_name, 'rb'))

        context.bot.send_message(chat_id=chat_id, text="This is an invalid move.")
        possible_moves = "Possible moves: "

        for m in board.legal_moves:
            possible_moves = possible_moves + " " + m.uci()

        context.bot.send_message(chat_id=chat_id, text=possible_moves)


all_commands = {
    'text': show_text,
    'draw': generate_chessboard_image,
    'new_game': new_game,
    'new_move': new_move,
    'piece_move': piece_move,
    'image': show_image,
    'pawn_promotes': pawn_promotes
}
