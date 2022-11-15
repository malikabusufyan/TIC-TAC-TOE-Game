from board import Board
from player import Player

class TicTacToeGame:

    def start(self):
        print("************************")
        print(" Welcome To Tic-Tac-Toe ")
        print("************************")

        board = Board()
        player = Player()
        computer = Player(False)
        board.print_board()

        while True:

            while True:

                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_tie():
                    print("It's a Tie!👍 Try again.")
                    break

                elif board.check_is_game_over(player, player_move):
                    print("Awesome!!! You Won the Game🎈")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("Ooops... The Computer Won!! Please Try Again")
                        break

            play_again = int(input("Would you like to play again? Enter 1 for Yes and 0 for No: "))

            if play_again == 0:
                print("Bye!! Come back Soon")
                break

            elif play_again == 1:
                self.start_new_round(board)

            else:
                print("Your input is Invalid but I assume you wants to play again😀")
                self.start_new_round(board)

    def start_new_round(self, board):
        print("***********")
        print(" New Round ")
        print("***********")
        board.reset_board()


        board.print_board()
    

game = TicTacToeGame()

game.start()

                
