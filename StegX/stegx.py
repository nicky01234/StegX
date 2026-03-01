#!/usr/bin/env python3

from colorama import Fore, Style
from modules import image, audio, text

def banner():
    with open("assets/banner.txt", "r") as f:
        print(Fore.GREEN + f.read())
        print(Style.RESET_ALL)

def main_menu():
    print("\n1) Image Steganography")
    print("2) Audio Steganography")
    print("3) Text Steganography")
    print("0) Exit")
    return input("Select option: ")

def operation_menu():
    print("\n1) Embed")
    print("2) Extract")
    return input("Select operation: ")

def main():
    banner()

    while True:
        choice = main_menu()

        if choice == "1":
            op = operation_menu()
            if op == "1":
                image.embed()
            elif op == "2":
                image.extract()

        elif choice == "2":
            op = operation_menu()
            if op == "1":
                audio.embed()
            elif op == "2":
                audio.extract()

        elif choice == "3":
            op = operation_menu()
            if op == "1":
                text.embed()
            elif op == "2":
                text.extract()

        elif choice == "0":
            print("Exiting StegX...")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
