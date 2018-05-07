def hangman(word):
    guessWrong = 0
    stages = ["",
              "___________           ",
              "|          |          ",
              "|          |          ",
              "|          O          ",
              "|         /|\         ",
              "|         / \         ",
              "|                     ",
              ]
    
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while guessWrong < len(stages) -1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            guessWrong += 1

        print((" ".join(board)))
        e = guessWrong +1 
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))
        
hangman("cat")
    
