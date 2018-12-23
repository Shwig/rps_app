import random
import time


def main():
    # initialize all counter vars to 0
    player_rounds = 0
    cpu_rounds = 0
    round_count = 0
    total_rounds = 0
    player_games = 0
    cpu_games = 0
    player_total_rounds = 0
    cpu_total_rounds = 0
    player_game_precent = 0
    cpu_game_percent = 0
    player_round_percent = 0
    cpu_round_percent = 0
    total_draws = 0
    draw_percent = 0

    # becasue one pass will always result in one game played
    total_games = 1

    description = """
    ##############################################################
    #                                                            #
    #     Welcome to the Rock, Paper, Scissors game!             #
    #                                                            #
    #     To play select r, p, or s from the keyboard            #
    #     then hit enter.                                        #
    #                                                            #
    #     The winner is the best of 3 rounds.                    #
    #     Good luck!                                             #
    #                                                            #
    ##############################################################
    """

    score = """
               Score
        ####################
         Player     CPU
           {:d}         {:d}
        ####################
    """

    stage = """               Shoot!
        =====================
        {:{align}{width}s}VS{:{align}{width}s}
        =====================
    """

    stats = """
       Thank you for playing!
              Stats
        ###################
         Total Games: {:d}
        Total rounds: {:d}
         Draw rounds: {:d}
              Draw %: {:.{prec}f}

        Player wins: {:d}
              win %: {:.{prec}f}
         Rounds won: {:d}
            round %: {:.{prec}f}

        Cpu wins: {:d}
           win %: {:.{prec}f}
        Rnds won: {:d}
         round %: {:.{prec}f}
        ###################
    """

    weapons = ["Rock", "Paper", "Scissors"]

    # 2D array to hold all possible results
    n = 3
    m = 3
    results = [[0] * m for i in range(n)]

    results[0][0] = "rr"  # draw
    results[0][1] = "rs"  # win
    results[0][2] = "rp"  # lose

    results[1][0] = "pp"  # draw
    results[1][1] = "pr"  # win
    results[1][2] = "ps"  # lose

    results[2][0] = "ss"  # draw
    results[2][1] = "sp"  # win
    results[2][2] = "sr"  # lose

    ##############################################################

    print(description)

    # run the game until the user decides when to quit
    while True:

        # Each game is best of 3 rounds
        # player and cpu Rounds represent the number of rounds won during the current game
        while (player_rounds < 2) and (cpu_rounds < 2):
            print(score.format(player_rounds, cpu_rounds))

            # ask the user to choose a weapon and validate their input
            while True:
                player_choice = input("Make a selection: Rock (R), Scissors(S), Paper(P) >> ")
                if player_choice.lower() not in ('r', 'p', 's'):
                    print("!Not a valid entry! valid entries: r, p, or s ")
                else:
                    break

            # a random weapon is selected for the cpu from the tuple
            cpu_choice = random.choice(('r', 'p', 's'))

            # concatinate player and cpu choices into a single string
            # the resulting two character string will determine the winner
            match_up = player_choice + cpu_choice

            # comment out time.sleep(1) for faster gameplay
            # count down for dramatic effect
            print("\n   --Rock!")
            time.sleep(1)
            print("    -Paper!")
            time.sleep(1)
            print("     Scissors!")
            time.sleep(1)

            # display the player and cpu choices
            if player_choice == 'r':
                player_weapon = weapons[0]
            elif player_choice == 'p':
                player_weapon = weapons[1]
            else:
                player_weapon = weapons[2]

            if cpu_choice == 'r':
                cpu_weapon = weapons[0]
            elif cpu_choice == 'p':
                cpu_weapon = weapons[1]
            else:
                cpu_weapon = weapons[2]

            # display the chosen weappons on the stage
            print(stage.format(player_weapon, cpu_weapon, align='^', width='10'))

            # compare the current matchUp to the possible results
            # Draw
            if match_up == results[0][0] or match_up == results[1][0] or match_up == results[2][0]:
                print('{:{align}{width}}'.format('DRAW.', align='^', width='21'))
                total_draws += 1

            # player wins
            elif match_up == results[0][1] or match_up == results[1][1] or match_up == results[2][1]:
                print('{:{align}{width}}'.format('YOU WON!', align='^', width='25'))
                player_rounds += 1
                player_total_rounds += 1

            # cpu wins
            else:
                print('{:{align}{width}}'.format('YOU LOST!', align='^', width='25'))
                cpu_rounds += 1
                cpu_total_rounds += 1

            round_count += 1
            total_rounds += 1

        if player_rounds >= 2:
            print('\n\n')
            player_games += 1
            print(score.format(player_rounds, cpu_rounds))
            print('YOU WON THE GAME.')

        else:
            print('\n\n')
            cpu_games += 1
            print(score.format(player_rounds, cpu_rounds))
            print('YOU LOST THE GAME.')

        # ask if user would like to play another game
        while True:
            player_choice = input("\nWould you like to play again? Yes[y] No[n]>> ")
            if player_choice.lower() not in ('y', 'n'):
                print("\n!Not a valid entry! valid entries: y, or n ")
            else:
                break

        # the player chooses to end the game calcualte and display the stats from session
        if player_choice == 'n':
            player_game_percent = player_games/total_games
            cpu_game_percent = cpu_games/total_games

            player_round_percent = player_total_rounds/total_rounds
            cpu_round_percent = cpu_total_rounds/total_rounds

            draw_percent = total_draws/total_rounds

            print(stats.format(total_games, total_rounds, total_draws, draw_percent,
                               player_games, player_game_percent, player_total_rounds,
                               player_round_percent, cpu_games, cpu_game_percent,
                               cpu_total_rounds, cpu_round_percent, width=5, prec=2))
            input('>>> Hit any key to end session')
            break

        # if yes increment game counter and reset counters for best of 3 rounds
        # if this isn't done counters will be left with the result of the previous game
        # This breaks the second while loop condition causing the game to end instantly
        else:
            total_games += 1

            player_rounds = 0
            cpu_rounds = 0
            round_count = 0


if __name__ == "__main__":
    main()    
