import random
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

scores= [0]*len(epsilonVals)
bandits = generate_bandits()
for k in range(len(epsilonVals)):
    for i in range(200):
        scores[k] += play_game(bandits, epsilonVals[k])

for i in range(len(scores)):
    scores[i] = scores[i]/200
print(scores)


#play game with uncertainty -  make temp list add uncertanties, play based on max uncertain no epislons just greed