# Лабораторна робота № 2
# Виконали студенти групи АІ, ЛАІ194 Бицкало І. Дем'яненко І. Оганесян М.
# Варіант 3


def letteronly(text):
    """
    This does some sanitising - only letters make it through
    """
    output = ''
    for char in text:
        if 64 < ord(char) < 91:
            if char == 'J':
                char = 'I'
            output += char
    return output


def massageKey(txt):
    """
    This turns the key into a 25 letter grid alphabet one
    that has been expressed linearly
    """
    userkey = letteronly(txt)
    key = ''
    for char in userkey:
        if char not in key:
            key += char
    return key


def massageMessage(txt):
    """
    Break the message into digraphs, repeated letters have an X

    i.e. HELLO becomes HE LX LO

    and ALLOWS is AL LO W
    """
    usrmsg = letteronly(txt)
    msg = ''
    # keep track of where we are in digraph
    First = True
    for i in range(len(usrmsg)):

        # the first letter in a digraph
        if First:
            msg += usrmsg[i]

            # if last letter of message, append X
            if i + 1 == len(usrmsg):
                msg += 'X'

            # if next letter is the same, append X or go onto second letter
            else:
                if usrmsg[i] == usrmsg[i + 1]:
                    msg += 'X'
                else:
                    First = False
        else:
            # append second letter
            msg += usrmsg[i]
            First = True
    return msg


def showgrid(key):
    """
    Show the key grid
    """
    print('\nPlayfair Grid:')
    for j in range(5):
        for i in range(5):
            print(key[i + j * 5], '', end='')
        print()
    print()
    return


def showmsg(msg):
    """
    Break a string into digraphs
    """
    space = True
    for char in msg:
        print(char, end='')
        space = not space
        if space:
            print(' ', end='')
    print()
    return


def playfair(enc, msg, key):
    """
    Encrypt with playfair
    """
    # reversing the operation between encrypt and decrypt
    offset = -1
    if enc:
        offset = +1
    output = ''
    for i in range(0, len(msg), 2):
        # extract letters in digraph
        lett1 = msg[i]
        lett2 = msg[i + 1]
        # find the key position
        pos1 = key.find(lett1)
        pos2 = key.find(lett2)
        # turn into coordinates
        coord1 = [pos1 % 5, pos1 // 5]
        coord2 = [pos2 % 5, pos2 // 5]
        # if in same row, shift along
        if coord1[0] == coord2[0]:
            coord1[1] = (coord1[1] + offset) % 5
            coord2[1] = (coord2[1] + offset) % 5
        # if in same col, shift vert
        elif coord1[1] == coord2[1]:
            coord1[0] = (coord1[0] + offset) % 5
            coord2[0] = (coord2[0] + offset) % 5
        # if on corners of rectangle, go for opp corners
        else:
            tmp = coord2[0]
            coord2[0] = coord1[0]
            coord1[0] = tmp
        # go back from coordinates to key position
        pos1 = coord1[0] + 5 * coord1[1]
        pos2 = coord2[0] + 5 * coord2[1]
        # pull the new letter
        lett1 = key[pos1]
        lett2 = key[pos2]
        # build the output
        output += lett1
        output += lett2
    return output


def showres(msg1, msg2):
    linesize = 50
    for i in range(0, len(msg1), linesize):
        showmsg(msg1[i:i + min(linesize, len(msg1) - i)])
        showmsg(msg2[i:i + min(linesize, len(msg2) - i)])
        print()
    return


userkey = (input('Enter keyword: ') + 'abcdefghijklmnopqrstuvwxyz').upper()
key = massageKey(userkey)

try:
    file_name = 'lab2_text.txt'
    with open(file_name, 'r') as input_file:
        usermsg = input_file.read().upper()
except TypeError:
    raise TypeError("Error occurred while reading file")

msg = massageMessage(usermsg)

enc = True
showgrid(key)

newmsg = playfair(enc, msg, key)

print('Showing digraphs:\n')
showres(msg, newmsg)

print('Encrypted text:')
print(newmsg)
