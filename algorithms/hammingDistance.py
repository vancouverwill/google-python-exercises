
'''
hamming distance is the simplest of string comparison algorithms
all it does is look for differences between the two strings
i.e the number of substitutions needed to make the strings match
'''


def hammingDistance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1, s2))

# split up algorithm over multiple lines to see what python native functions do
def myHammingDistance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")

    total = 0
    for num in range(0, len(s1)) :
        charAOrd = ord(s1[num])
        charBOrd = ord(s2[num])
        result = bool(charAOrd - charBOrd)
        total += result

    return total

def main():
  print 'hamming distance'
  wordA = "wamming"
  wordB = "hammony"
  print wordA + " " + wordB
  print hammingDistance(wordA, wordB)
  print myHammingDistance(wordA, wordB)



# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
