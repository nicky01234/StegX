from PIL import Image

def embed_image():
    input_img = input("Enter input PNG/BMP image: ")
    output_img = input("Enter output image name: ")
    message = input("Enter secret message: ")

    img = Image.open(input_img)
    pixels = img.load()

    binary = ''.join(format(ord(c), '08b') for c in message) + '1111111111111110'

    data_index = 0
    width, height = img.size

    for y in range(height):
        for x in range(width):
            if data_index < len(binary):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary[data_index])
                data_index += 1
                pixels[x, y] = (r, g, b)
            else:
                break

    img.save(output_img)
    print("Message embedded successfully!")

def extract_image():
    input_img = input("Enter stego image: ")

    img = Image.open(input_img)
    pixels = img.load()

    binary = ""
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary += str(r & 1)

    bytes_data = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ""

    for byte in bytes_data:
        if byte == '11111110':
            break
        message += chr(int(byte, 2))

    print("Extracted message:", message)
