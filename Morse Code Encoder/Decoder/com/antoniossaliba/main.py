ENCODING_LIST = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '!': '-.-.--',
    ':': '---...',
    ';': '-.-.-.',
    '/': '-..-.',
    '-': '-....-',
    '@': '.--.-.',
    '=': '-...-'
}

DECODING_LIST = {
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '-.-.--': '!',
    '---...': ':',
    '-.-.-.': ';',
    '-..-.': '/',
    '-....-': '-',
    '.--.-.': '@',
    '-...-': '='
}

menu = input("Do you want to start? ('Yes' or 'no') ").lower()

while menu != 'yes' and menu != 'no':
    print("You have to enter either 'yes' or 'no'")
    menu = input("Do you want to start? ('Yes' or 'no') ").lower()

while menu == 'yes':
    decode_encode = input("Do you want to encode or decode? ('Encode' or 'Decode' or 'Exit' to exit) ").lower()

    while decode_encode != 'encode' and decode_encode != 'decode' and decode_encode != 'exit':
        print("You have to enter either 'encode' or 'decode' or 'exit' to quit the program.")
        decode_encode = input("Do you want to encode or decode? ('Encode' or 'Decode' or 'Exit' to exit) ").lower()

    if decode_encode == 'exit':
        break

    if decode_encode == 'encode':
        input_str = input("Enter a string that involves [a-z]/[0-9]/['.', ',', '?', '!', ':', ';', '/', '-', '@', '=']"
                          " (Separate words by a single white space character) ").lower()
        delimiter = input("Choose the delimiter between two words (Either '/' or 3 white space characters). Insert 1 or 2: ")
        while delimiter != '1' and delimiter != '2':
            print('Invalid option for the delimiter!')
            delimiter = input("Choose the delimiter between two words (Either '/' or 3 white space characters). Insert 1 or 2: ")
        encoded_str = str()
        try:
            split_str = input_str.split(" ")
            for word in split_str:
                for char in word:
                    encoded_str += ENCODING_LIST[char]
                    encoded_str += " "
                encoded_str = encoded_str.rstrip()
                if delimiter == '1':
                    encoded_str += '/'
                else:
                    encoded_str += '   '
            print(f'Your encoded string is: {encoded_str[0:len(encoded_str) - 1]}')
        except:
            print('Found an invalid pattern. Review the rules!')
    else:
        input_str = input("Enter a encoded string to decode it! The allowed delimiters between words are '/' or 3 white"
                          " space characters: ").lower()
        delimiter = input("Choose the delimiter between two words (Either '/' or 3 white space characters). Insert 1 or 2: ")
        while delimiter != '1' and delimiter != '2':
            print('Invalid option for the delimiter!')
            delimiter = input("Choose the delimiter between two words (Either '/' or 3 white space characters). Insert 1 or 2: ")
        decoded_str = str()
        try:
            if delimiter == '1':
                delimiter = '/'
            else:
                delimiter = '   '
            words = input_str.split(delimiter)
            for word in words:
                letters = word.split(' ')
                for letter in letters:
                    decoded_str += DECODING_LIST[letter]
                decoded_str += " "
            print(f"Your decoded string is: {decoded_str.rstrip()}")
        except:
            print("Found an invalid pattern. Review the rules!")

    menu = input("Do you want to continue? ('Yes' or 'no') ").lower()

    while menu != 'yes' and menu != 'no':
        print("You have to enter either 'yes' or 'no'")
        menu = input("Do you want to continue? ('Yes' or 'no') ").lower()

print('Thank you...')