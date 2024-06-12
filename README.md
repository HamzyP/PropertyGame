# Buying and Selling Property Game (to be re-named)

The game allows players to buy and sell properties to build their portfolio.
- Built with python, tkinter.
- Database is SQLite3 and managed with DB Browser(sqlite).


## Description
The game allows players to explore a range of properties with varying values and income potentials.
Players start with a certain amount of money and can use it to purchase and invest in properties. 
Each property increases in value as each month passes and when put on rent they can gain additonal income.
The goal is to accumulate as much wealth as possible.

- This is an early version of the program. The later version that works is lost so have to fix all the bugs/functionality.
- Was built for computer science A-Level OCR project.

## Features

- Property Market: A dynamic range of properties including residential, industrial and commercial properties. 
- Buying and Selling: Purchase properties at market prices and sell them for a profit.
- Income Generation: Earn passive income from owned properties based on their value and rental yield.
- Leaderboard: There is a leaderboard where you can compare your liquid capital with other users.
  
## Issues
Currently there are issues with the saving features. 
I am rebuilding the save function with the hopes of fixing it. 
An idea I have is move all the saves to the database instead of a textfile which is evidently causing issues.
Originally used a textfile for the save and a database for the user details to add complexity for a better mark.
Now the goal is to actually get it functioning instead of for a better grade.

- The different pages have been separated into different files but game.py is still larger than I would like it to be.
