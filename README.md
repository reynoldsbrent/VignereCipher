# Vignere Encryption

This Python script performs keyword encryption on a given text using a user-provided keyword. It shifts each letter of the text based on the corresponding letter's position in the keyword. The resulting encrypted text is displayed as output.

## How the Encryption Works

- The script takes a clear text and a keyword from the user.
- It creates lists to store individual letters of the text, the keyword, and the encrypted text.
- For each letter in the text, the script finds the corresponding letter from the keyword based on position.
- Shift values are calculated for each keyword letter using the alphabet index.
- The script encrypts each letter of the text using the calculated shifts.
- The encrypted letters are joined to form the encrypted string.

## Example Output:

- Which text should be encrypted: secretmessage
- Which keyword should be used: keyword
- cianskpowqwuv

## How to Use

1. Save the provided code to a file, e.g., `keyword_encryption.py`.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is located.

4. Run the script using the following command:

   ```bash
   python keyword_encryption.py
Enter the text you want to encrypt when prompted.

Enter the keyword you want to use for encryption.

The script will perform keyword encryption and display the resulting encrypted text.