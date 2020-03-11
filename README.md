# Palmero
Palmero is a hyper-simplification of encryption in Python.

## Features

### Palmero features encryption key generation based on the identitiy of the machine you're encrypting on.
Meaning that unless you know the password and are on the machine the file was created on, the file won't be unlocked. That said, machine ID generation is possible, so you can give someone both the password and your machine's unique ID to bypass this if need be.

### Super easy encryption and decryption
Using Palmero is as easy as calling ```encrypt()``` or ```decrypt``` with your source file and password. Palmero has already been tuned to offer high levels of security, and allows for customizablity with some parameters.

### Uses Pycryptodome under the hood
Most of the fundementals of the encryption process are handled by Pycryptodome, which allows for many levels of customisability and fine tuning in the source code. 
