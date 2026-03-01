def embed_text():
    input_file = input("Enter input text file: ")
    output_file = input("Enter output text file: ")
    message = input("Enter secret message: ")

    zero = '\u200b'
    one = '\u200c'

    binary = ''.join(format(ord(c), '08b') for c in message)
    hidden = ''.join(zero if b == '0' else one for b in binary)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content + hidden)

    print("Message embedded successfully!")

def extract_text():
    input_file = input("Enter stego text file: ")

    zero = '\u200b'
    one = '\u200c'

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    binary = ""
    for char in content:
        if char == zero:
            binary += '0'
        elif char == one:
            binary += '1'

    bytes_data = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ""

    for byte in bytes_data:
        message += chr(int(byte, 2))

    print("Extracted message:", message)
