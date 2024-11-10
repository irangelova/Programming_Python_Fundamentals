# **Programming Python Fundamentals Sep 2024** 💻

Repository containing my work during the fundamentals course in Python from SoftUni

🔗 [Link to Python Fundamentals course](https://softuni.bg/trainings/4693/programming-fundamentals-with-python-september-2024)

## **Table of Contents** 📑

- [x] Basic Syntax
- [x] Data Types and Variables
- [x] Pattern drawings
- [x] Lists Basic
- [x] Functions
- [x] List Advanced
- [x] Objects and Classes
- [x] Dictionaries
- [ ] Text Processing
- [ ] Regular Expressions
- [ ] Basic Web Project

## **Developed projects during the course** 📈

### 1. Game of rock🪨, paper📄, scissors✂️

🚀 The goal of the project was to develop a two-player game of rock, paper, schissors where a player plays against the computer. Each player choose simultaneously one of three possible options - rock, paper or scissors. The outcome of the game is then defined according to following rules:
- Paper beats rock (the paper covers the rock)
- Rock beats scissors (the scissors get broken by the rock)
- Scissors beat paper (the paper gets cut by the scissors)

The winner is the player whose choice beats the choice of the opponent. In case both players chose the same option (e.g., "paper"), the game outcome is "draw".

⚙️ The solution consists of several steps:
- Player inputs their choice (rock, paper or scissors). If player input invalid text an error is raised
- With the library "random" and the "randint" method the computer makes a random choice
- After each round the result (win, loss or draw) is evaluated and printed according to the following table: <!--![image](https://github.com/user-attachments/assets/be36617d-7c00-48fc-92b0-de5537077f7a) -->
- After printing the outcome of the round the player is asked wheter they want to play another one
- If the player wants to continue the game they input "yes". Otherwise they input "no" and statistics of the game (number of won, lost and draw rounds) are printed
  
  ![Screenshot 2024-09-28 235741](https://github.com/user-attachments/assets/8599fd35-1c01-4399-ba6f-06efb6f8a6e4)

⏯️ Live demo of the code:

 [<img alt="Play Button" src="https://github.com/user-attachments/assets/458c9ed7-0521-4f88-9eef-cbd555bb7511" width="100" height="50"/>](https://replit.com/@ivetar/RockPaperScissorsbyIveta)

