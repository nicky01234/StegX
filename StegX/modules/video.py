import cv2
import numpy as np

def embed():
    input_video = input("Enter input AVI video path: ")
    output_video = input("Enter output AVI video path: ")
    message = input("Enter secret message: ")

    cap = cv2.VideoCapture(input_video)

    if not cap.isOpened():
        print("Error opening video file.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    # Convert message to bits
    bits = []
    for char in message:
        for i in range(8):
            bits.append((ord(char) >> (7 - i)) & 1)

    bits += [0]*8  # End marker

    bit_index = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        flat = frame.flatten()

        for i in range(len(flat)):
            if bit_index < len(bits):
                flat[i] = (flat[i] & 0xFE) | bits[bit_index]
                bit_index += 1
            else:
                break

        new_frame = flat.reshape(frame.shape)
        out.write(new_frame)

    cap.release()
    out.release()

    if bit_index < len(bits):
        print("Video too small for message!")
    else:
        print("Message embedded successfully!")

def extract():
    input_video = input("Enter stego AVI video path: ")

    cap = cv2.VideoCapture(input_video)

    if not cap.isOpened():
        print("Error opening video file.")
        return

    bits = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        flat = frame.flatten()
        bits.extend([pixel & 1 for pixel in flat])

    cap.release()

    chars = []
    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i:i+8]:
            byte = (byte << 1) | b

        if byte == 0:
            break

        chars.append(chr(byte))

    print("Extracted message:", "".join(chars))
