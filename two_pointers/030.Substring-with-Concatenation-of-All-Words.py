def findSubstring(str, words):
    mapping = {}
    #length of each word, size of the sliding window
    size = len(words[0])
    result = []
    #maximum size of the concatenated string
    max_size = size * len(words)

    for word in words:
        if word not in mapping:
            mapping[word] = 0
        mapping[word] += 1
    
    for i in range(size):
        #need to reset count and mapping
        count = 0
        copy = mapping.copy()
        for j in range(i, len(s)-size+1, size):
            sub = s[j:j+size]
            if sub in copy:
                copy[sub] -= 1

                if copy[sub] >= 0:
                    count += 1

            #when window size is over the max_size, we need to pop out word
            pop_start = j - max_size 
            if pop_start >= 0:
                pop_sub = s[pop_start:pop_start+size]
                if pop_sub in copy:
                    copy[pop_sub] += 1
                    if copy[pop_sub] > 0:
                        count -= 1
            if count == len(words):
                result.append(pop_start+size)

    return result
            
    

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

print(findSubstring(s, words))
# Output: [6,9,12]


        