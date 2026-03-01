import wave

def embed_audio():
    input_audio = input("Enter input WAV file: ")
    output_audio = input("Enter output WAV file: ")
    message = input("Enter secret message: ")

    song = wave.open(input_audio, mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    binary = ''.join(format(ord(c), '08b') for c in message)
    binary += '1111111111111110'

    for i in range(len(binary)):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(binary[i])

    with wave.open(output_audio, 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_bytes)

    song.close()
    print("Message embedded successfully!")

def extract_audio():
    input_audio = input("Enter stego WAV file: ")

    song = wave.open(input_audio, mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    binary = ""
    for byte in frame_bytes:
        binary += str(byte & 1)

    bytes_data = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ""

    for byte in bytes_data:
        if byte == '11111110':
            break
        message += chr(int(byte, 2))

    song.close()
    print("Extracted message:", message)
