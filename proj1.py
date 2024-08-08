import tkinter as tk
from tkinter import messagebox

# Caesar Cipher function
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Encrypt function to display result
def encrypt_message():
    text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = caesar_cipher(text, shift)
    messagebox.showinfo("Encrypted Message", encrypted_text)

# Decrypt function to display result
def decrypt_message():
    text = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text = caesar_cipher(text, -shift)
    messagebox.showinfo("Decrypted Message", decrypted_text)

# Setting up the Tkinter window
root = tk.Tk()
root.title("Caesar Cipher")

# Labels and input boxes for text and shift
label_text = tk.Label(root, text="Enter your message:")
label_text.grid(row=0, column=0, padx=10, pady=10)

entry_text = tk.Entry(root, width=40)
entry_text.grid(row=0, column=1, padx=10, pady=10)

label_shift = tk.Label(root, text="Enter the shift value:")
label_shift.grid(row=1, column=0, padx=10, pady=10)

entry_shift = tk.Entry(root, width=5)
entry_shift.grid(row=1, column=1, padx=10, pady=10)

# Buttons for encryption and decryption
button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message)
button_encrypt.grid(row=2, column=0, padx=10, pady=10)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message)
button_decrypt.grid(row=2, column=1, padx=10, pady=10)

# Running the Tkinter event loop
root.mainloop()
