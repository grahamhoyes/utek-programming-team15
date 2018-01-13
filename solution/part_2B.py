import math

weights = [math.pow(10, -5), math.pow(10, -4), math.pow(10, -3), math.pow(10, -2), math.pow(10,-1), 0.88889]

def prob(counts, word):
    if not counts.__contains__(word):
        return 0
    if len(word) == 2:
        if counts[word] == 0 or counts[word[0]] == 0:
            return math.pow(10, -10)
        else:
            return max (weights[0] * (counts[word]/counts[word[:-1]]), math.pow(10, -10)) 
    
    else: 
        if counts[word] == 0 or counts[word[:-1]] == 0:
            return math.pow(10, -10)
        else:
            return max ((weights[len(word)-2] * (counts[word]/counts[word[:-1]])) + prob(counts, word[:-1]), math.pow(10,-10))
            
def Score(counts, sentence):
    sentence = sentence.replace(" ", "")
    score = 0
    for i in range(len(sentence)):
        word = sentence[i]
        end = i + 4
        if end > len(sentence):
            end = len(sentence)
        for j in range(i + 1, end):
            word += sentence[j]
            probability = prob(counts, word)
            if (probability == 0):
                score += -15
            else:
                score += math.log10(probability)
        
    return score
    
def part_2B(counts, sent1, sent2):
    score1 = Score(counts, sent1)
    score2 = Score(counts, sent2)
    if score1 > score2:
        return 1
    else:
        return 2