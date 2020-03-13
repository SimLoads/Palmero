# Palmero
<a href="https://github.com/SimLoads/Palmero/blob/master/LICENSE" title="License"><img src="https://img.shields.io/github/license/SimLoads/palmero"></a> <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=DYF7QMKWBK8PS&source=url" title="Support project"><img src="https://img.shields.io/badge/Support%20project-paypal-brightgreen.svg"></a> 

Palmero is a hyper-simplification of encryption in Python.
```
pip install palmero
```

## Features

### Palmero features encryption key generation based on the identitiy of the machine you're encrypting on.
Meaning that unless you know the password and are on the machine the file was created on, the file won't be unlocked. That said, machine ID generation is possible, so you can give someone both the password and your machine's unique ID to bypass this if need be.

### Super easy encryption and decryption
Using Palmero is as easy as calling ```encrypt()``` or ```decrypt()``` with your source file and password. Palmero has already been tuned to offer high levels of security, and allows for customizablity with some parameters.

### Uses Pycryptodome under the hood
Most of the fundementals of the encryption process are handled by Pycryptodome, which allows for many levels of customisability and fine tuning in the source code. 

### Examples

Be sure to first link the main class to a variable:  
```
plm = palmero.Palmero()
```

To encrypt a file _secrets.txt_ with the password _foo_ then you would use:   
```
plm.encrypt("secrets.txt", "foo")
```
You could add to this that you want to save the encrypted data to a different file name, by using the _outfile_ parameter:  
```
plm.encrypt("secrets.txt", "foo", outfile="bar")
```
Now, to decrypt this file, it's as easy as:  
```
plm.decrypt("bar", "foo")
```
This returns the decrypted data as a string. Alternatively, you could write the decrypted data right to a file with:  
```
plm.decrypt("bar", "foo", outfile=True)
```
Let's assume now you want to send your friend an encrypted file, and he already knows the password. He won't be able to decrypt it, as the key to decrypt files is machine-specific. To get around this, you can also send your friend your custom Machine ID, which you can get by using:  
```
plm.keygen("foo")
```
Which returns the machine ID as a string. You could also write this directly to a file, _key.txt_, using:  
```
plm.keygen("foo", outfile=True)
```
Further info can be found as help in the script. 
