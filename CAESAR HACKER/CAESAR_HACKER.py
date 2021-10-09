print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): # Loop through every possible key.
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  # Get the number of the symbol.
            num = num - key  # Decrypt the number.

            if num < 0:
                num = num + len(SYMBOLS)

            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol

    # Display the key being tested, along with its decrypted text:
    print('Key #{}: {}'.format(key, translated))