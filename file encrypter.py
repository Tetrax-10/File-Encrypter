from cryptography.fernet import Fernet  # pip install cryptography
import os

task = input("Type\n1 : encryption\n2 : decryption\nAnswer : ")


def getFileInfo(task):
    global raw_file_name
    global file_name
    global extension
    if task == "1":
        raw_file_name = input("Enter the File Name with extension : ")
        file_name = raw_file_name.split(".")[0]
    elif task == "2":
        raw_file_name = input(
            "Enter the Decrypted File Name with extension : ")
        file_name = raw_file_name.split(".")[0].split(" encrypted")[0]
    extension = raw_file_name.split(".")[-1]


def encryptIt():
    key = Fernet.generate_key()
    try:
        os.mkdir(f"./{file_name} encrypted")
    except:
        pass
    # writes key to the file
    with open(f"./{file_name} encrypted/{file_name} key.key", 'wb') as filekey:
        filekey.write(key)

    # reads key from the file
    with open(f"./{file_name} encrypted/{file_name} key.key", 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    # locates the file to encrypt
    with open(f"{file_name}.{extension}", 'rb') as file_:
        original = file_.read()

    # encrypts the file with the generated key
    encrypted = fernet.encrypt(original)

    # saves the encrypted file
    with open(f"./{file_name} encrypted/{file_name} encrypted.{extension}", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decryptIt():
    # reads key from the file
    with open(f"./{file_name} encrypted/{file_name} key.key", 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    # locates the encrypted file
    with open(f"./{file_name} encrypted/{file_name} encrypted.{extension}", 'rb') as encrypted_file:
        encrypted_file = encrypted_file.read()

    # decrypts the file with the key from the file
    decrypted = fernet.decrypt(encrypted_file)

    try:
        os.mkdir(f"./{file_name} decrypted")
    except:
        pass

    # saves the decrypted file
    with open(f"./{file_name} decrypted/{file_name}.{extension}", 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


if task == "1":
    print("just put the file in the same folder as this python script")
    getFileInfo(task)
    encryptIt()
    print("Encrypted Successfully\nCaution : Do not rename or edit the file\nSave the generated folder in a second place")
elif task == "2":
    print("just put the folder that has been generated in the same folder as this python script")
    getFileInfo(task)
    decryptIt()
    print("Decrypted Successfully")
else:
    print("Operation Failed. Enter the correct operation")
    quit()
