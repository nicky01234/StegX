#!/usr/bin/env python3

from colorama import Fore, Style
from modules import image, audio, text

VERSION = "1.0.0"

def banner():
    with open("assets/banner.txt", "r") as f:
        print(Fore.GREEN + f.read())
        print(Style.RESET_ALL)

def main_menu():
    print("\n1) Image Steganography")
    print("2) Audio Steganography")
    print("3) Text Steganography")
    print("0) Exit")
    return input("\nSelect option: ")

def sub_menu():
    print("\n1) Embed")
    print("2) Extract")
    return input("Select option: ")

def main():
    banner()

    while True:
        choice = main_menu()

        if choice == "1":
            action = sub_menu()
            if action == "1":
                image.embed_image()
            elif action == "2":
                image.extract_image()

        elif choice == "2":
            action = sub_menu()
            if action == "1":
                audio.embed_audio()
            elif action == "2":
                audio.extract_audio()

        elif choice == "3":
            action = sub_menu()
            if action == "1":
                text.embed_text()
            elif action == "2":
                text.extract_text()

        elif choice == "0":
            print("Exiting StegX...")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
