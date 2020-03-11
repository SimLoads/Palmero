import palmero
plm = palmero.Palmero()

def main():
    plm.logo()
    print("\n0: Create test file")
    print("1: Encrypt File")
    print("2: Decrypt File")
    print("3: Generate Key")
    print("4: Help")
    next = input()
    if next == "0":
        with open('example.txt', 'w') as exm:
            exm.write("This is an example of a file to encrypt!\n1 2 3 4 \n|?<>:!@#$%^&*()|}{][]}")
        print("Created 'example.txt'")
        main()

    if next == "1":
        file = input("File to encrypt: ")
        passw = input("Password: ")
        try:
            plm.encrypt(file, passw)
        except FileNotFoundError:
            print("That file doesn't exist!")
            input()
            main()
        print("Encrypted!")
        input()
        main()

    if next == "2":
        file = input("File to decrypt: ")
        passw = input("Password: ")
        try:
            data = plm.decrypt(file, passw)
        except FileNotFoundError:
            print("That file doesn't exist!")
            input()
            main()
        except:
            print("Your password is incorrect!")
            input()
            main()
        print("Decrypted!\nData is: %s" % data)
        input()
        main()

    if next == "3":
        passw = input("Password: ")
        try:
            key = plm.keyGen(passw)
        except:
            print("There was an error!")
            input()
            main()
        print("Generated!\nThe key is %s" % key)
        input()
        main()

    if next == "4":
        helpx()
        main()
    

def helpx():
    print("Encrypt: Used to encrypt a file. Returns True if successful.\nParameters:\n")
    enchelp = {
        "file":"Specify the file to encrypt",
        "password":"The password used for encryption",
        "outname":"(Optional, Off by default) The name of the encrypted file",
        "delete_original":"(Optional, On by default) Delete the original file after encrypting"
    }
    for key,val in enchelp.items():
        print("%s: %s" %(key, val))
    
    print("\nDecrypt: Used to decrypt a file. Returns decrypted data.\nParameters:\n")
    dcrhelp = {
        "file":"Specify the file to decrypt",
        "password":"The password used for decryption",
        "outfile":"(Optional, Off by default) Save the decrypted data back to a file, named per the encrypted file name",
        "keyfile":"(Optional) Specify location of a decryption key, stored in a file."
    }
    for key,val in dcrhelp.items():
        print("%s: %s" %(key, val))   

    print("\nGenerate Key: Used to generate a decryption key, so files can be decrypted on other computers. Returns key string that can be saved to a file.\nParameters:\n")
    gnkhelp = {
        "password":"The password used for decryption",
        "outfile":"(Optional, Off by default) Save the generated key to a file",
    }
    for key,val in gnkhelp.items():
        print("%s: %s" %(key, val))   
    
    input()
main()