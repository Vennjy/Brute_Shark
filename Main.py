import time

def main(password):
    start = time.time()

    dictionary = []
    var = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.<>/?`~!@#$%^&*()-_=+[{]}|;:'
    for b in var:
        dictionary.append(b)
    letter = []
    pWord = password

    for x in range(0, len(pWord)):
        for y in range(0, len(dictionary)):
            if pWord[x] == dictionary[y]:
                letter.append(dictionary[y])

                print('\r', ''.join(letter), end='')
            else:

                print('\r', ''.join(letter), end='')

    print('\r', ''.join(letter))
    end = time.time()
    elapsed = end - start
    print('time it took: ', int(elapsed))


# example of using this script would be main('Vennjy_is_cool'), syntax: main(password to crack).
