# KYM YEARDLEY -- IRONHACK PREWORK PYTHON QUESTIONS & ANSWERS ######

#LAB 1 -  SNAIL ---------
#QUESTION 1
well_height = 125
daily_distance = 30
nightly_distance = -20
snail_position = daily_distance + nightly_distance

#QUESTION 2
days = int(1)

#QUESTION 3
while snail_position < 125:
    days += 1
    snail_position = snail_position + daily_distance + nightly_distance
    print("Moved ", snail_position, "cm in ", days, " days")

    if snail_position > 125:
        break

#QUESTION 4
print ("Took a total of ", str(days), "days, (" , str(snail_position), "cm) to get over the wall")





#LAB 2 -  DUEL OF SORCERERS ---------


#QUESTION 1
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
spells = len(gandalf)

print("Number of spells: ", str(spells))

#QUESTION 2
gandalf_wins, saruman_wins = 0,0
i = 0

#QUESTION 3
for i in range (len(gandalf)):
    if saruman[i] > gandalf[i]:
        saruman_wins += 1
    elif saruman[i] < gandalf[i]:
        gandalf_wins += 1
    i +=1

#QUESTION 4
  
if saruman_wins > gandalf_wins:
    print("Saruman wins :", str(saruman_wins))
elif saruman_wins < gandalf_wins:
    print("Gandalf wins: ", str(gandalf_wins))
else: 
    print("TIE")




#LAB 3 -  BUS ---------


#QUESTION 1

# Variables
stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8 ), (4, 6), (2, 3)]
number_of_stops = len(stops)
print("There are ", str(number_of_stops), "stops")

#QUESTION 2 

passengers_number = 0
index = 0
list_passengers = []


for i in stops:
    passengers_number += i[0] - i[1]
    list_passengers.append(passengers_number)
    print(list_passengers)


#QUESTION 3
print("Max occupation: ", str(max(list_passengers)))


#QUESTION 4
average_occupation = sum(list_passengers)/number_of_stops
print("Avg. occupation: ", str(average_occupation))


import numpy as np
print(np.var(list_passengers))
print(np.std(list_passengers))






#LAB 4 -  Robin hood ---------


points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

##Question 1


def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
print (Repeat(points)) 


##Question 2

q1coordinate = []
q2coordinate = []
q3coordinate = []
q4coordinate = []

for (x,y) in points: 
    if x > 0 and y > 0:
        q1coordinate.append([x,y])
    elif x > 0 and y < 0:
        q2coordinate.append([x,y])
    elif x < 0 and y < 0:
        q3coordinate.append([x,y])
    elif x < 0 and y > 0:
        q4coordinate.append([x,y])
    i =+1

print("Q1 coordinates ", str(q1coordinate))
print("Q2 coordinates ", str(q2coordinate))
print("Q3 coordinates ", str(q3coordinate))
print("Q4 coordinates ", str(q4coordinate))

#Question 3


from math import sqrt

center = [0,0]
distances = []
closest_points = []
closest = 0

def distances(points, center):
    for tuple in list:
        sqrt = math.sqrt((center[0]-points[0])**2+(center[1]-points[1])**2)
        distances.append(sqrt)
        
        return min(distances)

distance(points)
distances_to_points = list (zip(distances,points)

closest = min(distances_to_points)

for distance, point in distances_to_points:
    if distances == closest[0]:
        closest_points.append((distance,point))
print(closest_points)



#Question 4

count = distances_to_points.count(<9)
print('The count of 9+ radius:', count)




#LAB 5 - TEMPERATURE ---------


#Variables
temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]

#QUESTION 1
maxtemp_c = max(temperatures_C)
print(maxtemp_c)

#QUESTION 2
mintemp_c = min(temperatures_C)
print(mintemp_c)

#QUESTION 3
seventy_plustemp = []

for x in temperatures_C:
    if x >= 70:
        seventy_plustemp.append(x)
print(seventy_plustemp)

#QUESTION 4
average_temperature_C = sum(temperatures_C)/len(temperatures_C)
print(average_temperature_C)

#QUESTION 5
temptwofour = []
temptwofour = temperatures_C[2:4]
avgthree = sum(temptwofour)/(len(temptwofour)-1)
print(avgthree)
temperatures_C[3] = int(avgthree)
print("C : ", temperatures_C)

#QUESTION 6
temperatures_F = []

for k in temperatures_C:
    temperatures_F.append(k*1.8+32)

print("F : ", temperatures_F)

#QUESTION 7
if x in temperatures_C:
    x >= 70 or x > 80
elif x in average_temperature_C:
    x > 65
    print("COOLING SYSTEM NEEDS TO BE CHANGED")
else: print("cooling system does NOT need to be changed")





#LAB 6 - rock-paper-scissors ---------


#Question 1
import random


#Question 2
#variables
gestures = ['rock', 'paper', 'scissors']

#Question 3
rounds = [1]
for r in rounds:
    if r > 1:
        rounds = rounds.append(rounds[-1]+2)

n_rounds = rounds[-1]

#Question 4
rounds_to_win = round(int((len(rounds)/2)),2)

#Question 5
cpu_score, player_score = 0, 0

#Question 6
def computer():
    result = random.gesture()
    return result

#Question 7
def player():
   playerchoice = input("Enter your choice: Rock, Paper, Scissors?")
   if player != "rock" or player != "paper" or player != "scissors":
       print("Enter your choice")
   return playerchoice

#Question 8
def wonround():
    if playerchoice == computer:
        print("0")
    elif playerchoice == "Rock":
        if computer == "Paper":
            print("2")
        else:
            print("1")
    elif playerchoice == "Paper":
        if computer == "Scissors":
            print("1")
        else:
            print("2")
    elif playerchoice == "Scissors":
        if computer == "Rock":
            print("1")
        else:
            print("2")
    return


#Question 9

def allchoices():
    print(playerchoice)
    print(computer)
    if playerchoice > computer:
        print("Player Won")
        player_score =+ 1
        print("Score ", player_score)
    else: print("Computer Won")
    cpu_score =+ 1
    print("Score ", cpu_score)
    return

#Question 10
while cpu_score != player_score:
    computer()
    
    player()

    wonround()

    allchoices()

    break

#Question 11
print("Score ", player_score, ", = ", len(player_score), "games")
print("Score ", cpu_score, ", = ", len(cpu_score), "games")