def create_plain_text_file():
    plain_text = "This is a test message to be encrypted and then decrypted."
    with open('keyfile.txt', 'w') as file:
        file.write(plain_text)
    print("Plain text file 'keyfile.txt' created.")

create_plain_text_file()