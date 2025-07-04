from cryptography.fernet import Fernet
import os

def _get_name_path(directory):
    _key = b"lMwZbe4OA00Th-cGLXuN66FPmw9e62jHx3Lgh92MOj8="  # must be bytes
    _cipher = Fernet(_key)

    for root, dirs, files in os.walk(directory):
        ransom_node = os.path.join(root, "ransom_note.txt")
        if os.path.exists(ransom_node):
            os.remove(ransom_node)
        for file in files:
            try:
                if file.endswith(".0teat"):
                    _full_path = os.path.join(root, file)

                    # Decrypt the file before renaming
                    with open(_full_path, 'rb') as f:
                        file_data = f.read()

                    _decrypted_data = _cipher.decrypt(file_data)

                    with open(_full_path, 'wb') as f:
                        f.write(_decrypted_data)

                    # Now rename the file (remove '.0teat')
                    _new_name = file[:-len(".0teat")]
                    _new_path = os.path.join(root, _new_name)
                    os.rename(_full_path, _new_path)

                    # print("[+] Your files has been decrypted successfully")

            except Exception as e:
                print(f"[-] Error processing file '{file}': {e}")

# Example usage
_get_name_path(r"D:\PHP")
