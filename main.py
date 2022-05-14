from game import Game


robo = 'S'
array_game = [['+', '+', '+', '+', '+'],
              ['+', robo, '', '', '+'],
              ['+' ,'' , '+', '*', '+'],
              ['+', '', '', '','+'],
              ['+', '+', '+', '+', '+']]
game = Game(array_game)


while True:
    game.array
    game.walk(game.pos(), robo)
    game.pos()
    
    if(game.win() == True):
        game.array
        break