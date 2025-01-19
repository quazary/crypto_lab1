def caesar_brute_force(file_path):
    # Alphabet to work with
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Read the ciphertext from the file
    with open(file_path, 'r') as file:
        cipher_text = file.read().strip()
    
    # Loop through all possible shifts (1 to 25)
    for shift in range(1, 26):
        decrypted_text = ""
        for char in cipher_text.lower():  # Convert to lowercase for simplicity
            if char in alphabet:
                # Shift character and handle wrap-around
                new_index = (alphabet.index(char) - shift) % 26
                decrypted_text += alphabet[new_index]
            else:
                # Keep spaces and unsupported characters as is
                decrypted_text += char
        print(f"Shift {shift}: {decrypted_text}")

# Path to the text file
file_path = "ciphertext.txt"
# Call the function
caesar_brute_force(file_path)
