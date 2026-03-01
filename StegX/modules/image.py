from PIL import Image
import numpy as np

def embed():
    input_img = input("Enter input image path: ")
    output_img = input("Enter output image path: ")
    message = input("Enter secret message: ")

    img = Image.open(input_img)
    data = np.array(img)
    flat = data.flatten()

    bits = []
    for char in message:
        for i in range(8):
            bits.append((ord(char) >> (7 - i)) & 1)

    bits += [0]*8  # end marker

    if len(bits) > len(flat):
        print("Image too small!")
        return

    for i in range(len(bits)):
        flat[i] = (flat[i] & 0xFE) | bits[i]

    new_data = flat.reshape(data.shape)
    Image.fromarray(new_data.astype('uint8')).save(output_img)

    print("Message embedded successfully!")

def extract():
    input_img = input("Enter stego image path: ")

    img = Image.open(input_img)
    data = np.array(img)
    flat = data.flatten()

    bits = [pixel & 1 for pixel in flat]

    chars = []
    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i:i+8]:
            byte = (byte << 1) | b
        if byte == 0:
            break
        chars.append(chr(byte))

    print("Extracted message:", "".join(chars))
