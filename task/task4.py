'''

Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string , except with the words in backwards order.
For example, say I type the string:
{ My name is Michele. }
Then I would see the string:
{ Michele is name My }

'''

def main():
    user = str(input('Bir cumle daxil edin: '))

    word = user.split()
    word_list = []

    for i in word:
        word_list.insert(0, i)

        words = ' '.join(word_list)

    print(words)

main()

# import reverse
# def main():
#     user = str(input('Bir soz daxil edin: '))

#     word = user.split()
#     word = user.reverse()
#     word = user[::-1]

#     words = ' '.join(word)

#     print(words)

# main()
