import random
import math
def generate_bandits():
    bandits = []
    for i in range(10):
        bandits.append(random.normalvariate(0,1))
    return bandits

epsilonVals = [0, 0.001, 0.01, 0.1, 0.5, 1]


def play_game(bandits, epsilonVal):
    banditCount = [0]*10
    banditSums = [0]*10
    qVals = [0]*10
    for i in range(2000):
        if(random.random() < epsilonVal):
            index = int(random.random()*10)
            banditCount[index] +=1
            banditSums[index] += random.normalvariate(bandits[index], 1)
            qVals[index] = banditSums[index]/banditCount[index]
        else:
            index = qVals.index(max(qVals))
            banditCount[index] +=1
            banditSums[index] += random.normalvariate(bandits[index], 1)
            qVals[index] = banditSums[index]/banditCount[index]
    return sum(banditSums)

def play_game_with_uncertaintiy(bandits):
    banditCount = [0]*10
    banditSums = [0]*10
    uncertanties = [1]*10 #I START UNCERTANTIES AT 1 CAUSE IT JUST ACTS NORMAL GREEDY AT 0
    qVals = [0]*10
    for i in range(2000):
        index = uncertanties.index(max(uncertanties))
        banditSums[index] += random.normalvariate(bandits[index], 1)
        banditCount[index] +=1
        qVals[index] = banditSums[index]/banditCount[index]
        uncertanties[index] = qVals[index]+ (math.log(sum(banditCount))/(banditCount[index]+1e-10))**0.5
    return sum(banditSums)


scores= [0]*len(epsilonVals)
bandits = generate_bandits()
cheat_score = 0
for i in range(2000):
    cheat_score += random.normalvariate(max(bandits), 1)

print("cheating score", cheat_score)
for k in range(len(epsilonVals)):
    for i in range(200):
        scores[k] += play_game(bandits, epsilonVals[k])

for i in range(len(scores)):
    scores[i] = scores[i]/200
    print(str(epsilonVals[i]) +"- ", scores[i])
print("highest score epsilon val " + str(epsilonVals[scores.index(max(scores))]) +"-", max(scores))

ucb_score = 0
for i in range(200):
    ucb_score += play_game_with_uncertaintiy(bandits)
print("ucb score", ucb_score/200, ", "+str(round(100-(ucb_score/(200*cheat_score))*100,2)) + "% difference")


#play game with uncertainty -  make temp list add uncertanties, play based on max uncertain no epislons just greed