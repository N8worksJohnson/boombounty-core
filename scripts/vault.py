import sys
import os
from cryptography.fernet import Fernet

# USAGE: 
# Encrypt: python3 scripts/vault.py encrypt <file.md> <key>
# Decrypt: python3 scripts/vault.py decrypt <file.gpp> <key>

def encrypt(filepath, key):
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
        
        # Split Frontmatter from Body
        if b'---' in data[:4]:
            parts = data.split(b'---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                body = parts[2]
            else:
                print("Error: Invalid Frontmatter format")
                return
        else:
            print("Error: No YAML Frontmatter found (---)")
            return

        f = Fernet(key)
        encrypted_body = f.encrypt(body.strip())

        # Create new content: Old Frontmatter + Encryption Flag + Encrypted Blob
        new_content = b"---\n" + frontmatter + b"\nencryption: fernet\n---\n" + encrypted_body
        
        out_path = filepath.replace('.md', '.gpp')
        with open(out_path, 'wb') as f:
            f.write(new_content)
        print(f"🔒 Locked: {out_path}")
        
    except Exception as e:
        print(f"Error encrypting: {e}")

def decrypt(filepath, key):
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
        
        parts = data.split(b'---', 2)
        frontmatter = parts[1]
        encrypted_body = parts[2].strip()

        f = Fernet(key)
        decrypted_body = f.decrypt(encrypted_body)

        print(f"🔓 Payload for {filepath}:")
        print(decrypted_body.decode('utf-8'))
        
    except Exception as e:
        print(f"❌ Decryption Failed. Check your Key. Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: vault.py <encrypt|decrypt> <file> <key>")
        sys.exit(1)

    action = sys.argv[1]
    file = sys.argv[2]
    key = sys.argv[3]

    if action == 'encrypt':
        encrypt(file, key)
    elif action == 'decrypt':
        decrypt(file, key)
