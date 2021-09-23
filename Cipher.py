import string

print ('=== CIPHER ===')
print ('1. Shift Cipher \n2. Substitution Cipher \n3. Affine Cipher \n4. Vigenere Cipher \n5. Extended Vigenere Cipher \n6. Hill Cipher')
pilihan = input("Pilih Cipher: ")


# SHIFT CIPHER =====================================================================

if pilihan == "1":
 print("\n\t== Shift Cipher ==\n")

 #Encryption =======================
 plaintext1 = input("Plain Text = ")
 key1 = input("Shift Key = ")

# Mengecek isi Key (Harus Integer)
 while isinstance(int(key1), int) == False:
  key1 = input("Shift Key (Harus Integer!) =  ")

 key1 = int(key1)%26

 alphabet = string.ascii_uppercase
 shifted = alphabet[key1:] + alphabet [:key1]
 table = str.maketrans(alphabet, shifted)

 encrypted = plaintext1.translate(table)

 print("Hasil Cipher Text = ",encrypted)



elif pilihan == "2":
 print("\n\t== Substitution Cipher ==\n")

 #Encryption =======================
 plaintext2 = input("Plain Text = ")
 key2 = input("Substitution Key (26 Huruf) = ")
 Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

 hasil = ""
 for letter in plaintext2:
     if letter.upper() in Alphabet:
         hasil += key2[Alphabet.find(letter.upper())]
     else:
         hasil += letter

 print("Hasil Cipher Text = ",hasil)

 #Decryption =======================
 ciphertext2 = input("Cipher Text = ")
 key22 = input("Substitution Key (26 Huruf) = ")
 Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

 hasil = ""
 for letter in ciphertext2:
     if letter.upper() in key22:
         hasil += Alphabet[key22.find(letter.upper())]
     else:
         hasil += letter

 print("\n\nHasil Plain Text = ",hasil)


elif pilihan == "3":
 print("\n\t== Affine Cipher ==\n")

 #Encryption =======================
 plaintext3 = input("Plain Text = ")
 key3 = input("Affine Key = ")

elif pilihan == "4":
 print("\n\t== Vigenere Cipher ==\n")

 #Encryption =======================
 plaintext4 = input("Plain Text = ")
 key4 = input("Vigenere Key = ")

 def generateKey(plaintext4, key):
        key = list(key) 
        if len(plaintext4) == len(key):
            return(key)

        else:
            for i in range(len(plaintext4) -
                len(key)):
                key.append(key[i % len(key)])
            return("" . join(key))

 def cipherText(plaintext4, key):
        ciphertext4 = []
        for i in range(len(plaintext4)):
         x = (ord(plaintext4[i]) +
             ord(key[i])) % 26
         x += ord('A')
         ciphertext4.append(chr(x))
         return("" . join(ciphertext4))

 def originalText(ciphertext4, key):
        orig_text = []
        for i in range(len(ciphertext4)):
         x = (ord(ciphertext4[i]) -
             ord(key[i]) + 26) % 26
         x += ord('A')
         orig_text.append(chr(x))
         return("" . join(orig_text))

 key = generateKey(plaintext4, key4)
 ciphertext4 = cipherText(plaintext4,key)
 print("Cipher Text :", ciphertext4)
 print("Original/Decrypted Text :",
    originalText(ciphertext4, key))


elif pilihan == "5":
 print("\n\t== Extended Vigenere Cipher ==\n")

 #Encryption =======================
 plaintext5 = input("Plain Text = ")
 key5 = input("Extended Vigenere Key = ")

elif pilihan == "6":
 print("\n\t== Hill Cipher ==\n")

 #Encryption =======================
 plaintext6 = input("Plain Text = ")
 key6 = input("Hill Key = ")