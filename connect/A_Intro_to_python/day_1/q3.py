import random
player_1_score = 0
player_2_score = 0
round = 3
for rounds in range(1, round + 1):
    print(f"Round {rounds} : ")
    player_1 = random.randint(1, 6)
    player_2 = random.randint(1, 6)
    player_1_score += player_1
    player_2_score += player_2
    print(f"player_1 rolled : {player_1} and his score is : {player_1_score}")
    print(f"player_2 rolled : {player_2} and his score is : {player_2_score}")
print(f"Final score : \n player_1 : {player_1_score} \n player_2 : {player_2_score}")    
if player_1_score > player_2_score:
    print("Player 1 is the winner")
elif player_2_score > player_1_score:
    print("Player 2 is the winner") 
else  :
    print("It's a tie")      