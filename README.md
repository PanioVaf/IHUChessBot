# IHUChessBot
## Description
This is Chess-Bot used for teaching someone the base principles and rules of chess.  

## Functionality
The communication is based on the user interaction of asking questions. 

## Game description
for Dice game: They roll alternately from 10 dice. Every time that the 2 players roll the dice or one brings a bigger result than the other or bring the same result. In the first case, the cumulative is informed score of the player who brought the highest score. In the second case no no score is updated.

for Card game: All available (card) players participate in a hand of cards. In the beginning shuffle the deck and then draw from a card alternately until the cards run out. At the end of the game, each player presents them aces he has and opens his cards. The winner is the one who has collected more aces.

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
