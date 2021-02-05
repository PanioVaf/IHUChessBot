import os
import users
import logging
from rivescript import RiveScript
from pathlib import Path

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def main():
    """ Main program function. """
    print("Welcome to ChessBot")

    bot = RiveScript(utf8=True)
    bot.load_directory("./brain")
    bot.sort_replies()

    while True:
        msg = input('You> ')

        if msg == '/quit':
            users.cleanup()
            quit()

        user_id = 'localuser'
        print("bot>", bot.reply(user_id, msg))
        
    
if __name__ == "__main__":
    main()
