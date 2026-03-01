def embed():
    cover_file = input("Enter cover text file path: ")
    output_file = input("Enter output text file path: ")
    message = input("Enter secret message: ")

    zero = '\u200b'
    one = '\u200c'

    bits = []
    for char in message:
        for i in range(8):
            bits.append((ord(char) >> (7 - i)) & 1)

    bits += [0]*8

    hidden = ''.join([zero if b == 0 else one for b in bits])

    with open(cover_file, 'r', encoding='utf-8') as f:
        text = f.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text + hidden)

    print("Message embedded successfully!")

def extract():
    input_file = input("Enter stego text file path: ")

    zero = '\u200b'
    one = '\u200c'

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    bits = []
    for char in content:
        if char == zero:
            bits.append(0)
        elif char == one:
            bits.append(1)

    chars = []
    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i:i+8]:
            byte = (byte << 1) | b
        if byte == 0:
            break
        chars.append(chr(byte))

    print("Extracted message:", "".join(chars))
