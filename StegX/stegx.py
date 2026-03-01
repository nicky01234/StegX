#!/usr/bin/env python3

from colorama import Fore, Style

VERSION = "1.0.0"

def banner():
    with open("assets/banner.txt", "r") as f:
        print(Fore.GREEN + f.read())
        print(Style.RESET_ALL)

def main_menu():
    print("1) Image Steganography")
    print("2) Audio Steganography")
    print("3) Video Steganography")
    print("4) Text Steganography")
    print("0) Exit")
    return input("Select option: ")

def main():
    banner()

    while True:
        choice = main_menu()

        if choice == "1":
            print("Image module selected")
        elif choice == "2":
            print("Audio module selected")
        elif choice == "3":
            print("Video module selected")
        elif choice == "4":
            print("Text module selected")
        elif choice == "0":
            print("Exiting StegX...")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
