import random
import time

def main():
    #initialize all counter vars to 0
    playerRounds, cpuRounds, roundCount, totalRounds= (0,0,0,0)
    playerGames, cpuGames, playerTotalRounds, cpuTotalRounds = (0,0,0,0)
    playerGamePrecent, cpuGamePercent, playerRoundPercent, cpuRoundPercent = (0,0,0,0)
    totalDraws, drawPercent = (0,0)

    # becasue one pass will always result in one game played
    totalGames = 1

    description= """
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

    results[0][0] = "rr" #draw
    results[0][1] = "rs" #win
    results[0][2] = "rp" #lose

    results[1][0] = "pp" #draw
    results[1][1] = "pr" #win
    results[1][2] = "ps" #lose

    results[2][0] = "ss" #draw
    results[2][1] = "sp" #win
    results[2][2] = "sr" #lose

    ##############################################################

    print(description)
    
    # run the game until the user decides when to quit
    while True:

        # Each game is best of 3 rounds
        # player and cpu Rounds represent the number of rounds won during the current game
        while((playerRounds < 2) and (cpuRounds < 2)):
            print (score.format(playerRounds, cpuRounds))

            # ask the user to choose a weapon and validate their input 
            while True:
                playerChoice = input("Make a selection: Rock (R), Scissors(S), Paper(P) >> ")
                if playerChoice.lower() not in ('r', 'p', 's'):
                    print("!Not a valid entry! valid entries: r, p, or s ")
                else:
                    break
                
            # a random weapon is selected for the cpu from the tuple
            cpuChoice = random.choice(('r', 'p', 's'))

            # concatinate player and cpu choices into a single string
            # the resulting two character string will determine the winner
            matchUp = playerChoice + cpuChoice

            # comment out time.sleep(1) for faster gameplay 
            # count down for dramatic effect
            print("\n   --Rock!")
            time.sleep(1)
            print("    -Paper!")
            time.sleep(1)
            print("     Scissors!")
            time.sleep(1)        

            # display the player and cpu choices
            if playerChoice == 'r':
                playerWeapon = weapons[0]
            elif playerChoice == 'p':
                playerWeapon = weapons[1]
            else:
                playerWeapon = weapons[2]

            if cpuChoice == 'r':
                cpuWeapon = weapons[0]
            elif cpuChoice == 'p':
                cpuWeapon = weapons[1]
            else:
                cpuWeapon = weapons[2]            
            
            #display the chosen weappons on the stage
            print (stage.format(playerWeapon,cpuWeapon,align='^', width='10'))

            # compare the current matchUp to the possible results
            # Draw
            if (matchUp == results[0][0] or matchUp == results[1][0] or matchUp == results[2][0]): 
                print ('{:{align}{width}}'.format('DRAW.', align='^', width='21'))
                totalDraws += 1
                
            #player wins
            elif (matchUp == results[0][1] or matchUp == results[1][1] or matchUp == results[2][1]):
                print ('{:{align}{width}}'.format('YOU WON!', align='^', width='25'))
                playerRounds += 1
                playerTotalRounds += 1

            #cpu wins
            else:
                print ('{:{align}{width}}'.format('YOU LOST!', align='^', width='25')) 
                cpuRounds += 1
                cpuTotalRounds += 1                

            roundCount += 1
            totalRounds += 1

        if playerRounds >= 2:
            print('')
            print('')
            playerGames += 1
            print (score.format(playerRounds, cpuRounds))
            print('YOU WON THE GAME.')            
            
        else:
            print('')
            print('')
            cpuGames += 1
            print (score.format(playerRounds, cpuRounds))
            print('YOU LOST THE GAME.')

        # ask if user would like to play another game
        while True:
            playerChoice = input("\nWould you like to play again? Yes[y] No[n]>> ")
            if playerChoice.lower() not in ('y', 'n'):
                print("\n!Not a valid entry! valid entries: y, or n ")
            else:
                break

        # the player chooses to end the game calcualte and display the stats from session
        if playerChoice == 'n':
            playerGamePercent = playerGames/totalGames
            cpuGamePercent = cpuGames/totalGames

            playerRoundPercent = playerTotalRounds/totalRounds
            cpuRoundPercent = cpuTotalRounds/totalRounds

            drawPercent = totalDraws/totalRounds
            
            print(stats.format(totalGames, totalRounds, totalDraws, drawPercent,\
                               playerGames, playerGamePercent, playerTotalRounds,\
                               playerRoundPercent,cpuGames, cpuGamePercent,\
                               cpuTotalRounds, cpuRoundPercent, width=5, prec=2))
            input('>>> Hit any key to end session')
            break
            
        # if yes increment game counter and reset counters for best of 3 rounds
        # if this isn't done counters will be left with the result of the previous game 
        # This breaks the second while loop condition causing the game to end instantly
        else:
            totalGames += 1
            
            playerRounds = 0
            cpuRounds = 0
            roundCount = 0

################################################################
if __name__ == "__main__":
    main()
