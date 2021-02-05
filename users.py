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

import logging
import sys

import chess
import chess.engine
import chess.svg
from rivescript import RiveScript

import ch_commands

this = sys.modules[__name__]
this.users = dict()


class UserSession:

    def __init__(self, ch_id):
        self.id = ch_id
        self.bot = RiveScript(utf8=True)
        self.bot.load_directory("./brain")
        self.bot.sort_replies()
        self.engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
        self.board = chess.Board()

    def cleanup(self):
        logging.info("Cleaning up resources")
        self.engine.close()

    def reply(self, update, context):
        current_user = self
        msg = update.message.text
        riverbot_response = self.bot.reply(self.id, msg)
        ch_commands.run_command(current_user, update, context, riverbot_response)


def get_or_create_user(ch_id):
    if ch_id in this.users:
        return this.users[ch_id]
    else:
        this.users[ch_id] = UserSession(ch_id)
        return this.users[ch_id]


def cleanup():
    for u in this.users.values():
        u.cleanup()
