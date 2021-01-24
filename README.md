# IHUChessBot
## Description
This is Chess-Bot used for teaching someone the base principles and rules of chess.  

## Functionality
We need the platform TELEGRAM to set the bot. Using the Token provided from the platform we start the communication. The communication is based on the user interaction of asking questions. The users asks questions related to chess. It is given the ability to play a game with the Bot as well.

The communication is based on RiverScript.

## New functionality (TBA)
Update with commands related the game, like:
- offer/take draw
- play with either black or white
- more dialogues 
- use NLP for better understanting 

## Install the Bot
- Download and install Telegram from telegram.org 
- Go to contacts, search and select BotFather
- Run /start
- /newBot
- select the name you wish and alter the desctiption based on the help info provide (follow the instuctions)

Using the token provided from Telegram you can access the http API. Set it to the code and start interacting 
More information can be found at https://core.telegram.org/bots/api

## Install dependencies

If you are on a Mac or Linux machine, you probably already have Python installed. In this project we use Python 3.6.
We need to make sure though that we install pip and virtualenv for the correct version of Python on your computer. Open a terminal and run the following command:

```
$ sudo easy_install pip
$ sudo easy_install virtualenv

or if you get an error
$ python3 -m pip install --upgrade pip
$ pip3 install virtualenv

```

We clone the repository :

```
$ git clone https://github.com/PanioVaf/IHUChessBot.git
```

We are creating a virtual enviroment in order to install the dependencies locally.


```
$ cd IHUChessBot/
$ which python3
$ virtualenv -p $(which python3)  .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

## How to Run
Open the project to IDE (PYCHARM was used for this one)
Right click on \_\_main__.py and hit Run \_\_main__ 

OR

The commands to run the **IHUChessBot** from terminal is given below. 

```
$ cd IHUChessBot/
$ source .env/bin/activate
$ ./run.sh     
```
