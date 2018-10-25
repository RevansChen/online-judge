# Python3

# 有限制修改區域
def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        return ''.join(sorted(list(set(w1) - set(w2))))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]
