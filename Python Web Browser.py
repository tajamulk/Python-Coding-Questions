import webbrowser
import sys

address = input("Please enter the address: ")

# Assuming you want to open this address in a web browser
webbrowser.open(f'https://www.google.com/maps/place/{address}')
