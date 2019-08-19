from patternCount import PatternCount

def FrequentWords(Text, k):
    """find the most frequent pattern (k-mers) in Text 
        given the number of k-mers (k)"""
    # FrequentPatterns = {}
    Count = {}
    for i in range(0, len(Text)-k+1):
        pattern = Text[i:i+k]
        Count[i] = PatternCount(Text, pattern)
    print(Count)

    # if pattern in FrequentPatterns:
    #     FrequentPatterns[pattern] += 1
    # else:
    #     FrequentPatterns[pattern] = 1

    # return the key with max value
    # freq_key = max(FrequentPatterns, key=FrequentPatterns.get)
    # print(FrequentPatterns)
    # print(freq_key)


FrequentWords("ACAACTATGCATACTATCGGGAACTATCCT", 5)
