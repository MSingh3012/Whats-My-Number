def check_prime(guess):
    if guess % 2 == 0:
        print("%i is not prime, incrementing" % guess)
        return False
    i = 2
    for i in range(3, int(guess / 2), 2):
        if guess % i == 0:
            print("%i is not prime, incrementing" % guess)
            return False
    else:
        print("%i is prime! (1/6)" % guess)
        return True


def detect_one_seven(guess):
    guess_list = list(str(guess))
    detections = 0
    for n in guess_list:
        if n == '1':
            print("   But %i contains a one, incrementing" % guess)
            detections += 1
            return False
        elif n == '7':
            print("   But %i contains a seven, incrementing" % guess)
            detections += 1
            return False
    if detections == 0:
        print("   (2/6) And %i does not contain a one or a seven" % guess)
        return True


def digit_sum(guess):
    string = list(str(guess))
    total = 0
    for c in string:
        total += int(c)
    if total <= 10:
        print("   (3/6) And total of digits is %i (is <= 10)" % total)
        return True
    else:
        print("   But total is %i (is > 10), incrementing" % total)


def first_two_sum(guess):
    g_str = str(guess)
    total = int(g_str[0]) + int(g_str[1])
    if total % 2 != 0:
        print("   (4/6) And sum of first two digits is %i (odd)" % total)
        return True
    else:
        print("   But sum of first two digits is %i (even), incrementing" % total)
        return False


def get_index_second_to_last(guess):
    g_str = str(guess)
    i = int(g_str[len(g_str) - 2])  # Indices start at 0, subtract one, and another one to get the second to last
    if i != 0 and i % 2 == 0:
        print("   (5/6) And the second to last digit in %i is %i (even)" % (guess, i))
        return True
    elif i == 0:
        print("   But second to last digit %i == 0, which is neither even nor odd, incrementing" % i)
        return False
    elif i % 2 != 0:
        print("   But the digit %i in %i is not even, incrementing" % (i, guess))
        return False


def last_is_length(guess):
    g_str = str(guess)
    i = g_str[len(g_str) - 1]  # Indices start at 0, subtract one to get to last digit
    if int(i) == int(len(g_str)):
        print("   (6/6) And last digit %s equals the length of %i, %s" % (i, guess, len(g_str)))
        return True
    else:
        print("   But %s does not equal the length of %i (%s != %s)" % (i, guess, i, len(str(guess))))
        return False


def test():
    all_guess = []  # Creating a list to store all possible guesses in, just in case there happens to be another one after the first
    guess = 11  # Guess is 'between 1 and 1000', but the first requirement needs two digits, and 10 isn't prime, so 11
    while guess < 1000:
        if check_prime(guess) and detect_one_seven(guess) and digit_sum(guess) and first_two_sum(guess) and \
                get_index_second_to_last(guess) and last_is_length(guess):

            print("   Adding guess %i to list" % guess)
            all_guess.append(guess)  # This insures we see all possible combinations, not just the first one.
            guess += 2  # All even numbers are divisible by two, so we don't need to test them.
        else:
            guess += 2  # ^^^^
    print("Guesses are " + str(all_guess))


test()