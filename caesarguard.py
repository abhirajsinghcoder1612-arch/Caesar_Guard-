import tkinter as tk
from tkinter import filedialog
import os
import sys
import random
import ctypes
from PIL import Image, ImageTk


def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return filename


try:
    myappid = "caesarguard.securitytool.v1"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception:
    pass


def encrypt(message, shift):
    encrypted_message = ""
    for letter in message:
        if letter.isupper():
            position = ord(letter) - 65
            new_position = (position + shift) % 26
            encrypted_message += chr(new_position + 65)
        elif letter.islower():
            position = ord(letter) - 97
            new_position = (position + shift) % 26
            encrypted_message += chr(new_position + 97)
        else:
            encrypted_message += letter
    return encrypted_message


def decrypt(message, shift):
    return encrypt(message, -shift)


def on_open_click():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)


def on_encrypt_click():
    message = text_area.get("1.0", tk.END).rstrip("\n")
    try:
        shift = int(shift_box.get())
        result = encrypt(message, shift)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, result)
    except ValueError:
        text_area.insert(tk.END, "\n[Please enter a valid shift number]")


def on_decrypt_click():
    message = text_area.get("1.0", tk.END).rstrip("\n")
    try:
        shift = int(shift_box.get())
        result = decrypt(message, shift)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, result)
    except ValueError:
        text_area.insert(tk.END, "\n[Please enter a valid shift number]")


def on_save_click():
    message = text_area.get("1.0", tk.END).rstrip("\n")

    try:
        shift = int(shift_box.get())
    except ValueError:
        result_label.config(text="Please enter a valid shift number before saving.")
        return

    encrypted_content = encrypt(message, shift)

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(encrypted_content)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, encrypted_content)
        result_label.config(text="File saved (encrypted): " + file_path)


def shred_file(file_path, passes=3):
    if not os.path.exists(file_path):
        return False

    file_size = os.path.getsize(file_path)

    with open(file_path, "r+b") as file:
        for _ in range(passes):
            file.seek(0)
            random_data = bytes(random.getrandbits(8) for _ in range(file_size))
            file.write(random_data)
            file.flush()
            os.fsync(file.fileno())

    os.remove(file_path)
    return True


def on_shred_click():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        success = shred_file(file_path)
        if success:
            result_label.config(text="File shredded and deleted: " + file_path)
        else:
            result_label.config(text="Could not find file to shred.")


app = tk.Tk()
app.title("CaesarGuard")
app.geometry("520x520")

try:
    app.iconbitmap(resource_path("caesarguard_logo.ico"))
except Exception:
    pass

logo_image = Image.open(resource_path("caesarguard_logo.png"))
logo_image = logo_image.resize((80, 80))
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(app, image=logo_photo)
logo_label.pack(pady=(15, 0))

tk.Label(app, text="🔒 CaesarGuard", font=("Helvetica", 16, "bold")).pack(pady=(5, 0))
tk.Label(app, text="Simple encryption & secure file tool", font=("Helvetica", 9), fg="gray").pack()

tk.Label(app, text="Shift number:").pack(pady=(10, 0))
shift_box = tk.Entry(app, width=10)
shift_box.pack()

text_area = tk.Text(app, wrap="word")
text_area.pack(expand=True, fill="both", padx=10, pady=10)

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Open File", command=on_open_click).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Encrypt", command=on_encrypt_click).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Decrypt", command=on_decrypt_click).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Save File", command=on_save_click).grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="Shred File", command=on_shred_click, fg="red").grid(row=0, column=4, padx=5)

result_label = tk.Label(app, text="", wraplength=480, fg="gray")
result_label.pack(pady=(0, 10))

app.mainloop()
