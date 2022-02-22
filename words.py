from locale import currency


def check_first_k_letters(word1, word2, k):
    for i in range(k):
        if word1[i] != word2[i]:
            return False
    
    return True

def words_with_k_common_letters(word_array, k):
    n = len(word_array)
    start_index = 0
    current_index = start_index + 1
    maximum_len = 1

    while(start_index < n and current_index < n):
        if check_first_k_letters(word_array[start_index], word_array[current_index], k):
            if(current_index - start_index + 1 > maximum_len):
                maximum_len = current_index - start_index + 1
            current_index += 1
        
        else:
            start_index = current_index
            current_index = start_index + 1

    return maximum_len

n, k = list(map(int, input().split()))

words = []

for i in range(n):
    words.append(input())

words.sort()

print("this is words after sort: ", words)

words_matrix = [[] for i in range(26)]
index = 0
words_matrix[0].append(words[0])
print("this is words_matrix after first append: ",words_matrix)

for i in range(len(words)-1):
    if words[i][0] == words[i+1][0]:
        words_matrix[index].append(words[i+1])
    else:
        index += 1
        words_matrix[index].append(words[i+1])

print("this is word_matrix after all iterations: ", words_matrix)

maximum_answer = 0
for letter in words_matrix:
    print("words with common first letter: ", letter)

for letter in range(len(words_matrix)):
    if maximum_answer < words_with_k_common_letters(words_matrix[letter], k):
        maximum_answer = words_with_k_common_letters(words_matrix[letter], k)

print(maximum_answer)
