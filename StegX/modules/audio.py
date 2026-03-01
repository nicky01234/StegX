import wave
import numpy as np

def embed():
    input_audio = input("Enter input WAV file path: ")
    output_audio = input("Enter output WAV file path: ")
    message = input("Enter secret message: ")

    with wave.open(input_audio, 'rb') as wf:
        params = wf.getparams()
        frames = wf.readframes(wf.getnframes())

    samples = np.frombuffer(frames, dtype=np.int16)

    bits = []
    for char in message:
        for i in range(8):
            bits.append((ord(char) >> (7 - i)) & 1)

    bits += [0]*8

    if len(bits) > len(samples):
        print("Audio file too small!")
        return

    for i in range(len(bits)):
        samples[i] = (samples[i] & ~1) | bits[i]

    with wave.open(output_audio, 'wb') as wf:
        wf.setparams(params)
        wf.writeframes(samples.tobytes())

    print("Message embedded successfully!")

def extract():
    input_audio = input("Enter stego WAV file path: ")

    with wave.open(input_audio, 'rb') as wf:
        frames = wf.readframes(wf.getnframes())

    samples = np.frombuffer(frames, dtype=np.int16)
    bits = [sample & 1 for sample in samples]

    chars = []
    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i:i+8]:
            byte = (byte << 1) | b
        if byte == 0:
            break
        chars.append(chr(byte))

    print("Extracted message:", "".join(chars))
