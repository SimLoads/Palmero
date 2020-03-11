logo ='''
 _____      _                          
|  __ \    | |                         
| |__) |_ _| |_ __ ___   ___ _ __ ___  
|  ___/ _` | | '_ ` _ \ / _ \ '__/ _ \ 
| |  | (_| | | | | | | |  __/ | | (_) |
|_|   \__,_|_|_| |_| |_|\___|_|  \___/ 
'''

class Palmero:

    def encrypt(self, file, password, outname='', delete_original=True):
        '''
        Encrypt a file

        file: The file to encrypt\n
        password: Password used to encrypt\n
        
        Error ImportError: Usually raised if pycryptodomex is not found\n
        Error FileNotFoundError: Raised if the file does not exist\n
        '''
        from Crypto.Cipher import AES
        with open(file, 'r', encoding='ISO-8859-1') as openfile:
            data = openfile.read()
        data = data.encode('utf-8')
        key = self.__getKeys(password)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        if outname == '': outname = self.__getFileName(file, True)
        else: outname = self.__getFileName(outname, True)
        file_out = open(outname, "wb")
        [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
        if delete_original:
            import os
            os.remove(file)
        return True

    def decrypt(self, file, password='', outfile=False, keyfile=''):
        '''
        Decrypt an encrypted file

        file: The file to decrypt\n
        password: Password used to encrypt\n
        
        Error PasswordError: Password is incorrect\n
        Error ImportError: Usually raised if pycryptodomex is not found\n
        Error FileNotFoundError: Raised if the file does not exist\n
        '''
        
        from Crypto.Cipher import AES

        inname = self.__getFileName(file, True)
        file_in = open(inname, "rb")
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
        if keyfile == '':
            key = self.__getKeys(password)
        else:
            with open(keyfile, 'r') as keyf:
                uuid = keyf.read()
            key = self.__getKeys(password, genuuid=uuid, withGen=True)
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        try:
            data = cipher.decrypt_and_verify(ciphertext, tag)
        except ValueError:
            raise PasswordError("Decryption failure, password is incorrect")

        data = str(bytes(data).decode('utf-8'))
        if outfile:
            import os
            with open((self.__getFileName(file, False)), 'w') as writeout:
                writeout.write(data)
            os.remove(inname)
        else:
            return data
    
    def keyGen(self, password, outfile=False):
        '''
        Generate a key for decryption on other devices

        password: Password used to decrypt file\n
        
        Error ImportError: Usually raised if pycryptodomex is not found\n
        '''
        key = self.__getKeys(password, forGen=True)
        if outfile:
            with open('key.txt', 'w') as out:
                out.write(key)
            print('Saved to key.txt')
        else:
            return key


    def __stringObfuscate(self,stringToObfuscate):
        return(stringToObfuscate + ", Memes")

    def __getFileName(self, file, frd):
        if frd:
            filename = str(file) + ".pmnc"
        else:
            filename = str(file).replace('.pmnc','')
        return filename
        
    def __puncStrip(self, text):
        import string
        text = str(text)
        text = (text.translate(str.maketrans('', '', string.punctuation))).replace(' ','')
        return text

    def __getKeys(self, password, forGen=False, withGen=False, genuuid=''):
        import platform, hashlib
        from Crypto.Protocol.KDF import PBKDF2
        if withGen:
            uuid=genuuid
        else:
            uuid = hashlib.md5((self.__puncStrip(platform.uname())).encode('utf-8')).hexdigest()
        if forGen:
            return uuid
        uidkey = str.encode((uuid + password))
        key = PBKDF2(password, uidkey, dkLen=32)
        return key

    def logo(self):
        import time
        for item in logo.splitlines():
            print(item)
            time.sleep(0.1)

class PasswordError(Exception):
    pass