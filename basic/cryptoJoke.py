



# Each letter in the word should be switched with it's opposite leter in the alphabet
# i.e. a -> z, e -> v
# 'wrw blf hvv ozhg mrtsg'h vkrhlwv?' -> 'did you see last night's episode?'
# 'Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!' -> 'Yeah! I can't believe Lance lost his job at the colony!!'
def switchWord(word):
    def switch(c):
        index = ord(c)
        posInAlphabet = index - ord('a')
        newPosition = ord('a') - 1 + 26 - posInAlphabet
        return chr(newPosition)
    newWord = ''
    word = unicode(word)
    for i in range(0,len(word), 1):
        if word[i].isalpha() and word[i].islower():
            newWord += switch(word[i])
        else :
            newWord += word[i]
    return newWord

def main():
    print 'hello world'
    print 'bad'
    testWord = 'abcdesillyz'

    l = len(testWord)
    print l
    # for i in range(0, l, 1):
    #     print str(i) + ':'+testWord[i]+':' + str(ord(testWord[i]))+':'+switch(testWord[i])

if __name__ == '__main__':
  main()
  print switchWord("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
  print switchWord("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
