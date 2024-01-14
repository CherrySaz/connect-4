# Welcome to my Connect 4 Game

![computer gameplay](https://github.com/CherrySaz/connect-4/assets/134415334/6d97e702-1eb5-4d4b-a9c1-d79c9e97b807)

# About my project

Welcome to my Connect 4 game. This is a fun strategy game created using Python and has been built in the terminal. It is a Player vs Player game, as well as a player vs computer game. The choice is yours!
As a small child, Connect 4 was a family favourite, which gave me my inspiration for my project. It's so much fun! Who can score four in a row first? Can you beat the computer?

# Some history about the game

The game was originally released under a company called 'Score Four' until in 1968, it was bought by a company called 'Funtastic'.
The more modern version of the game was created by 2 business partners, 'Howard Wexler', a toy inventor, and 'Ned Strongin'.
The game was licensed in 1974 by Milton Bradley, which was later purchased by a toy company that is still going strong today, Hasbro.
In 1988, Connect 4 was solved for the first time. Today, there are various different sizes of the game. There's a household version, a travel version, an electronic version and even a giant garden version so you can play it outside in the warmer months.There are even giant versions of Connect 4 in pub gardens and play areas around the Country, which just shows its popularity!

![Connect 4](https://github.com/CherrySaz/connect-4/assets/134415334/762b8ff6-f709-474d-ac27-64d5ace94e13) ![Travel Connect 4](https://github.com/CherrySaz/connect-4/assets/134415334/040bc42b-7f80-4cda-99d3-a3c9624d3927) ![Electronic Connect 4](https://github.com/CherrySaz/connect-4/assets/134415334/8e407482-cbbc-4731-a583-b08fb60465de) ![Giant Connect 4](https://github.com/CherrySaz/connect-4/assets/134415334/b34bce77-1838-4332-8753-ea28864aa6d8)

## User Experience (UX)

My Connect 4 game is a command line application. It's written in the Python language only and is playable on one screen. The user can choose to play with another player, using the same kyboard, or, they can choose to play against the computer if they so wish.  The user will be asked which option they would like to select. Option 1 will be playing against the computer, and Option 2, against another player. They will then be asked to enter their name, which makes it more personable for the user, instead of just having 'Player 1' or 'Player 2'. They will then be presented with a board (or grid) on screen. They will be asked to make a move in turn. Once a move has been chosen, their initial will be displayed on the player board to show where they have placed their player token. When player against the computer, the computer's move will be displayed an 'o' for 'opponent' by default.
Once 4 in a row have been acheived by either player, or computer, a message will be displayed to say who wins.


![A player who has won](https://github.com/CherrySaz/connect-4/assets/134415334/af0da8ac-0b1e-427b-b7a7-d0360659183a)

## How to play

1. Click the link to the game and open on your browser
2. You will be greeting with a welcome message and presented with the player board. You will also be asked to choose an option
3. Choose an option, 1 or 2
4. Enter your name / names
5. Choose a column
6. Continue to choose columns until 4 in a row is acheived
7. Once game has completed, the winner is announced
8. Choose another column to play again or exit

## Features

• Welcome message

• Choice of playing player vs player or against the computer

• A clear game board to play on

• Winner is announced once four in a row is acheived

• Option to play again immediately after. No reloading or waiting



## Testing


This game was tested in the terminal throughout using run.py. It was also tested using The Code Institute's PEP-8 template. (https://pep8ci.herokuapp.com/)

![Pep-8 screenshot](https://github.com/CherrySaz/connect-4/assets/134415334/e4e72963-3047-4f50-b9a3-fc6be56ae5f5)














## 


## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
