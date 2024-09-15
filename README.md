# Public Key Importer and Encryption Tool

## Overview

This project includes both Python and Bash scripts designed to:

1. Import public keys.
2. Generate a text message.
3. Encrypt the message with a specific key.
4. Export the encrypted file under a specific name.

These tasks are executed in a loop, allowing for a smooth user experience.

## Python Script

### Functions

1. **`cle_import()`**
   - Imports public keys from a specified directory.
   - Prompts the user to enter the directory path containing the public keys.
   - Processes and imports each file using GPG.

2. **`text_generate()`**
   - Generates a text file with user-provided content.
   - Prompts the user to enter the text.
   - Saves the text to `generated.txt` in the current directory.

3. **`encryption()`**
   - Encrypts the generated text file using a specific public key.
   - Lists available GPG keys and prompts the user for the recipient's key ID or email.
   - Encrypts the file and saves it with a `.gpg` extension.

4. **`main()`**
   - Executes the functions in a loop based on user input.
   - Options include importing public keys, generating text, encrypting the text, or exiting.

### Usage

Run the Python script with:
```bash
python cryto.py
