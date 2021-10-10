# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

# 'abba' & 'baab' == true

# 'abba' & 'bbaa' == true

# 'abba' & 'abbba' == false

# 'abba' & 'abca' == false

# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word,words):
    word_ascii = [ord(char) for char in word] #convert unicode
    sum_word_ascci = sum(word_ascii) #sum unicode vals
    res = []
    for _ in words:
        aux_ascii = [ord(char) for char in _]
        sum_aux_ascii = sum(aux_ascii)
        if sum_word_ascci == sum_aux_ascii:
            res.append(_)
    return res


if __name__=='__main__':
    # Display list
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))

#test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
#test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])