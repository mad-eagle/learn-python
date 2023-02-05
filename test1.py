def encrypt(plaintext, shift):
  """Encrypts a plaintext message using the Caesar cipher."""
  ciphertext = ""
  for ch in plaintext:
    if ch.isalpha():
      # Encrypt uppercase letters
      if ch.isupper():
        ciphertext += chr((ord(ch) - 65 + shift) % 26 + 65)
      # Encrypt lowercase letters
      else:
        ciphertext += chr((ord(ch) - 97 + shift) % 26 + 97)
    # Leave non-alphabetic characters unchanged
    else:
      ciphertext += ch
  return ciphertext

def decrypt(ciphertext, shift):
  """Decrypts a ciphertext message using the Caesar cipher."""
  plaintext = ""
  for ch in ciphertext:
    if ch.isalpha():
      # Decrypt uppercase letters
      if ch.isupper():
        plaintext += chr((ord(ch) - 65 - shift) % 26 + 65)
      # Decrypt lowercase letters
      else:
        plaintext += chr((ord(ch) - 97 - shift) % 26 + 97)
    # Leave non-alphabetic characters unchanged
    else:
      plaintext += ch
  return plaintext

# Test the encryption and decryption functions
plaintext = "Hello, World!"
shift = 3
ciphertext = encrypt(plaintext, shift)
print(ciphertext)  # Output: Khoor, Zruog!
decrypted = decrypt(ciphertext , shift)
print(decrypted)  # Output: Hello, World!