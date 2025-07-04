# Educational Ransomware Simulation (Python + Tkinter)

> ⚠️ **DISCLAIMER**: This project is for educational purposes only. Do not use it on any system without **explicit permission**. Misuse may violate computer crime laws.

This Python project simulates basic ransomware behavior:
- Encrypts selected file types
- Shows a fake ransomware GUI with countdown
- Sets a ransom note and changes desktop wallpaper
- Includes a decryption script (with correct key)

---

## 🧰 Features

- ✅ Encrypts files with `.docx`, `.jpg`, `.pdf`, `.zip`, etc.
- ✅ Displays a GUI similar to WannaCry
- ✅ Countdown timer (1 hour)
- ✅ Drops `ransom_note.txt` in each folder
- ✅ Wallpaper is changed after encryption
- ✅ Includes decryption logic to recover files

---

## 🔐 Encryption Details

- Uses [`cryptography.Fernet`](https://cryptography.io/)
- AES-128 under the hood (symmetric encryption)
- Hardcoded key used for both encryption & decryption

---

## 📂 Targeted File Extensions

```python
_TARGET_EXTENSIONS = (
    ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".pdf", ".txt", ".jpg", ".jpeg", ".png",
    ".mp3", ".mp4", ".avi", ".zip", ".rar", ".7z",
    ".psd", ".ai", ".sql", ".db", ".csv"
)
```
## ⚙️ Requirements
- Python 3.8+
- cryptography library
---

ransomware_sim/
│
├── ransomware_gui.py       # 🔐 Main ransomware simulation script with GUI and encryption
├── decrypt_files.py        # 🔓 Decryption script to restore encrypted files
├── README.md               # 📘 Documentation and usage instructions
│
├── assets/                 # 📁 Folder for images and other resources
│   └── wallpaper.jpg       # 🖼 Wallpaper image to display as warning
│
└── secret.key              # 🔑 Stored encryption key (written at runtime)

## 🛑 Warnings
- This is not a toy — files will be encrypted for real.
- If you forget the key, recovery is impossible.
- Do not test on real data or systems you do not own.
---
## 📜 License
-  License — for educational use only.
