# Password Cracker

## Overview

This project is a multithreaded password-cracking tool designed to recover plaintext passwords from their MD5 hash. It employs two primary methods: a dictionary attack using a predefined list of possible passwords, and a brute-force attack that systematically tries all possible character combinations up to a specified length.

## Features

- **Dictionary Attack**: Utilizes a common password dictionary to attempt to match the hash.
- **Brute-Force Attack**: Tries all possible combinations of characters within a specified length to find the correct password.
- **Multithreading**: Executes both dictionary and brute-force attacks simultaneously to optimize the time taken to crack the password.
- **Customizable Brute-Force Length**: Allows the user to specify the maximum length for brute-force password attempts.

## Requirements

- Python 3.x
- A dictionary file such as `rockyou.txt` from the [SecLists repository](https://github.com/danielmiessler/SecLists).

## Installation

1. **Clone the repository** or download the project files:
   ```bash
   git clone https://github.com/messedupmohit/password-cracker.git
   cd password-cracker

2. **Ensure you have the dictionary file**:
    SecLists/Passwords/Common-Credentials/rockyou.txt

3. **Run the script**:
    python password_cracker.py
