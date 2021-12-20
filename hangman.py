result = ''
file = open('wordlist.txt','r')    # opening the text file, reading the words and appending then into a list.
words = []
for word in file.readlines():
    words.append(word.strip())

# Here, we take the input (number of chances the user wants ot play) from the user: k.
# We assume that the length of the word the user is going to guess and the length of every word in our text file is k
k = int(input('Enter K (This is the number of guesses you will have) : '))

answer = []   # when the user guesses the correct letter, we replace the _ in the list with the letter and print it out.
for i in range(k):
    answer.append('_')

# The code below (under the while loop) works as only as long as this condition holds true.
# subtract 1 from k everytime the user guesses a wrong letter or finally if the user manages to find the answer.

while k > 0:
    record = {} # lists of words are values of keys which correspond to the position of the letter the user guesses.
    guess = input('Please enter letter: ')

    for word in words:
        if guess not in word:
            if -1 not in record:
                record[-1] = [word]
            else:
                record[-1].append(word)
            continue

        for i in range(len(word)):
            if word[i] == guess:
                if i in record:
                    record[i].append(word)
                if i not in record:
                    record[i] = [word]

    # we finished creating the dictionary. Checking which list has the most words.
    max = -1
    for key, value in record.items():
        if len(value) > max:
            max = len(value)
            words = value    # the list with the maximum number of words is going to be assigned as words.
            pos = key

    if pos == -1:    # when the list of words that do not contain the guess is the longest
        k -=1
        s = ''
        for i in answer:
            s +=i
        print('Sorry, your answer is wrong! {} chances left.  {}'.format(k,s))
        continue

    answer[pos] = guess    # when the words containing the letter are more. insert the guessed letter into answer.
    s = ''
    for letter in answer:
        s += letter
    k -=1
    print('you guessed correctly! {} chances left.  {}'.format(k,s))

    if '_' not in s:
        result = 'you win'
        break

if result == 'you win':
    print(result)
else:
    result = 'you loose'
    print(result)
