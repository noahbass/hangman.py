import urllib.request


# play hangman
def hangman():
    # go!
    print('Let\'s play a game of hangman!')

    # get a random word
    response = urllib.request.urlopen('http://randomword.setgetgo.com/get.php').read()
    response = response.decode('utf-8')
    response = response.strip()

    # setup the word and the lists
    word = response.lower()
    word_list = []
    guess_list = ['0'] * len(word)
    guess_count = 0

    # give a hint
    print('The word is %s characters long. \n' % (len(word)))

    # get each letter in the word and put it in the word list
    for c in word:
        word_list.append(c)


    # allow guessing until the word has been guessed
    while '0' in guess_list:
        guess = input('What letter? ').lower()

        if guess == 'give up':
            # the user gave up
            print('You gave up!')
            print('The word was: %s' % (word))
            break
        elif len(guess) == 1:
            # the user made a guess
            if guess in word_list:
                # guess is correct, set it to found
                for i in word_list:
                    if guess == i:
                        location = word_list.index(guess) # get the location of the word
                        guess_list[location] = guess # set guess_list to the guess
                        word_list[location] = '0'    # set the word_list letter to '0' so it cannot be guessed again

                print('Letter found!')
            else:
                if guess_count < 6:
                    print('Letter not found. Try another...')
                    # increase the guess_count
                    guess_count += 1
                else:
                    print('You exceeded the max amount of guesses.')
                    print('The word was: ', word, '\n')
                    break
        else:
            print('Invalid guess. Try a letter...')

        # show progress
        print('Your progress: ', guess_list, '\n')
    else:
        # word has been guessed
        print('You\'ve correctly guessed the word!')
        pass


hangman()
