def morse_Translator(morse_text):
    alphabet = {
        '.-': 'A', '.---': 'J', '...': 'S',
        '-...': 'B', '-.-': 'K', '-': 'T',
        '-.-.': 'C', '.-..': 'L', '..-': 'U',
        '-..':  'D', '--': 'M', '...-': 'V',
        '.': 'E', '-.': 'N', '.--': 'W',
        '..-.': 'F', '---': 'O', '-..-': 'X',
        '--.': 'G', '.--.': 'P', '-.--': 'Y',
        '....': 'H', '--.-': 'Q', '--..': 'Z',
        '..': "I", '.-.': 'R',
    }
    

    latin_text = ''
    morse_words = morse_text.strip().split('  ')
    for morse_word in morse_words:
        words = morse_word.split(' ')
        for word in words:
            if word in alphabet:
                latin_text += alphabet[word]
        latin_text += ' '



    return latin_text.strip()


def latin_Translator(latin_text):
    alphabet = {
        'A': '.-', 'J': '.---', 'S': '...',
        'B': '-...', 'K': '-.-', 'T': '-',
        'C': '-.-.', 'L': '.-..', 'U': '..-',
        'D': '-..', 'M': '--', 'V': '...-',
        'E': '.', 'N': '-.', 'W': '.--',
        'F': '..-.', 'O': '---', 'X': '-..-',
        'G': '--.', 'P': '.--.', 'Y': '-.--',
        'H': '....', 'Q': '--.-', 'Z': '--..',
        "I": '..', 'R': '.-.',
    }


    morse_text = ''
    latin_words = latin_text.strip().upper().split(' ')
    for latin_word in latin_words:
        for word in latin_word:
            if word in alphabet:
                morse_text += alphabet[word] + ' '
        morse_text += ' '

    return morse_text.strip()



while True:
    print('1.Morse ------ > Latin\n', '2.Latin ------> Morse\n', '3.Cikis')

    choice = input('Secim edin: ')
    if choice == '1':
        morse_text = input('Morse metn: ')
        latin_text = morse_Translator(morse_text)
        print('Çevrilen Morse kodu:' + latin_text)
        print()

    elif choice == '2':
        latin_text = input('Latin metn: ')
        morse_text = latin_Translator(latin_text)
        print('Çevrilen Morse kodu:' + morse_text)
        print()

    elif choice == '3':
        print('Program bitdi.')
        break

    else:
        print('Yanlış məlumat')
        print()











#     alphabet = {
#         'A': '.-', 'J': '.---', 'S': '...',
#         'B': '-...', 'K': '-.-', 'T': '-',
#         'C': '-.-.', 'L': '.-..', 'U': '..-',
#         'D': '-..', 'M': '--', 'V': '...-',
#         'E': '.', 'N': '-.', 'W': '.--',
#         'F': '..-.', 'O': '---', 'X': '-..-',
#         'G': '--.', 'P': '.--.', 'Y': '-.--',
#         'H': '....', 'Q': '--.-', 'Z': '--..',
#         "I": '..', 'R': '.-.',
#     }
    
#     if translator == 'morseToLatin':
#         text = ''
#         morse_words = text.split(' ')
#         for morse_word in morse_words:
#             words = morse_word.split(' ')
#             for word in words:
#                 if word in alphabet:
#                     text += alphabet[word]
#             text += ' '

#         return text.strip()

#     if translator == 'latinToMorse':
#         text = ''
#         latin_words = text.split(' ')
#         for latin_word in latin_words:
#             for word in latin_word:
#                 if word in alphabet:
#                     text += alphabet[word]
#             text += ' '

#         return text.strip()

# while True:
#     print('1.Morse ------ > Latin\n', '2.Latin ------> Morse\n', '3.Cikis')

#     choice = input('Secim edin: ')
#     if choice == '1':
#         text = input('Morse metn: ')
#         latin_text = morse_Translator(text, translator = 'morseToLatin')
#         print(latin_text)
#         print()

#     elif choice == '2':
#         text = input('Latin metn: ')
#         morse_text = morse_Translator(text, translator = 'latinToMorse')
#         print(morse_text)
#         print()

#     elif choice == '3':
#         print('Program bitdi.')
#         break

#     else:
#         print('Yanlış məlumat')
#         print()