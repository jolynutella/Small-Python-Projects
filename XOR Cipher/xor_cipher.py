# Лабораторна робота № 3
# Виконали студенти групи АІ, ЛАІ194 Бицкало І. Дем'яненко І. Оганесян М.


def encryptDecrypt(inpString):
    """Function that encrypt and decrypt text"""
    # Define XOR key
    try:
        xorKey = str(input("Enter key: "))
    except TypeError:
        raise TypeError("Keyword must be a single character!")
    # calculate length of input string
    length = len(inpString)

    # perform XOR operation of key with every character in string
    for i in range(length):
        inpString = (inpString[:i] + chr(ord(inpString[i]) ^ ord(xorKey)) + inpString[i + 1:])
        print(inpString[i], end="")

    return inpString


# Driver Code
if __name__ == '__main__':
    try:
        file_name = 'lab3_text.txt'
        with open(file_name, 'r') as input_file:
            sampleString = input_file.read().upper()
    except TypeError:
        raise TypeError("Error occurred while reading file")

    # Encrypt the string
    print("Encrypted String: ", end="")
    sampleString = encryptDecrypt(sampleString)
    print("\n")

    # Decrypt the string
    print("Decrypted String: ", end="")
    encryptDecrypt(sampleString)
