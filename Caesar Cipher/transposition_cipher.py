# Лабораторна робота № 1
# Виконали студенти групи АІ, ЛАІ194 Бицкало І. Дем'яненко І. Оганесян М.
# Варіант 7

import math

key = str(input("Enter keyword: "))


# Encryption function
def encryptMessage(msg):
    cipher = ""

    # track key indices
    k_index = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # add the padding character '_' in empty cell of the matrix
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    # create Matrix and insert message and padding characters row-wise
    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]

    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_index])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        k_index += 1

    return cipher


# Decryption
def decryptMessage(cipher):
    decrypted_msg = ""

    # track key indices
    k_index = 0

    # track msg indices
    msg_index = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # convert key into list and sort alphabetically, so we can access each character by its alphabetical position.
    key_lst = sorted(list(key))

    # create an empty matrix to store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    # Arrange the matrix column wise according to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[k_index])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_index]
            msg_index += 1
        k_index += 1

    # convert decrypted msg matrix into a string
    try:
        decrypted_msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("You can't use repeating characters in keyword!")

    null_count = msg.count('_')

    if null_count > 0:
        return msg[: -null_count]

    return msg


# Read file with text
try:
    input_name = 'lab1_text.txt'
    with open(input_name, 'r') as input_file:
        msg = input_file.read()
except TypeError:
    raise TypeError("Error occurred while reading file")

# Printing encrypted and decrypted text
cipher = encryptMessage(msg)
print("Encrypted Text:\n {}".format(cipher))
print(" ")
print("Decrypted Text:\n {}".format(decryptMessage(cipher)))
