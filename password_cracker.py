import hashlib
import itertools
import string
import threading
import time
import os

# Function to hash a password
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Dictionary attack function
def dictionary_attack(dictionary_path, hash_to_crack):
    try:
        with open(dictionary_path, 'r', encoding='latin-1') as f:
            for line in f:
                word = line.strip()
                if hash_password(word) == hash_to_crack:
                    print(f"Password found by dictionary attack: {word}")
                    return word
    except FileNotFoundError:
        print(f"Dictionary file not found: {dictionary_path}")
    return None

# Brute-force attack function
def brute_force_attack(hash_to_crack, max_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            if hash_password(guess) == hash_to_crack:
                print(f"Password found by brute-force attack: {guess}")
                return guess
    return None

# Multithreading wrapper
def start_attack(attack_func, *args):
    thread = threading.Thread(target=attack_func, args=args)
    thread.start()
    return thread

def main():
    hash_to_crack = input("Enter the hash to crack: ")
    max_bruteforce_length = int(input("Enter the maximum length of the password for brute-force attack: "))

    # Path to the SecLists dictionary file
    dictionary_path = 'SecLists/Passwords/Common-Credentials/rockyou.txt'  # Adjust the path as necessary

    if not os.path.isfile(dictionary_path):
        print(f"Error: The dictionary file {dictionary_path} does not exist.")
        return

    # Start dictionary attack
    print("Starting dictionary attack...")
    dict_thread = start_attack(dictionary_attack, dictionary_path, hash_to_crack)
    
    # Start brute-force attack if dictionary attack fails
    print("Starting brute-force attack...")
    brute_thread = start_attack(brute_force_attack, hash_to_crack, max_bruteforce_length)

    # Wait for both threads to complete
    dict_thread.join()
    brute_thread.join()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
