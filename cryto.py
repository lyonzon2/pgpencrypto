import os
import subprocess


def cle_import():
    folder_path = input("type the path of your public keys :")

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue
        print("Processing file:", filename)
        command = ["gpg", "--import", file_path]
        subprocess.run(command)


def text_generate():
    text = input("write your text :")
    with open("/home/simo/Desktop/generated.txt", "w") as f:
        f.write(text)

    print("the text file is generated in '/home/simo/Desktop/generated.txt'")


def encryption():
    print("first i will show the keys that we already import")
    keys_output = subprocess.check_output(["gpg", "--list-keys"])
    keys_output = keys_output.decode("utf-8")
    print(keys_output)

    recipient_key_id = input("enter the id or the gmail for the public key, example:'root@gmail.com'  :")

    text_file = input("enter the path of the text file u wanna crypto, example:'plain.txt'  :")

    encrypted_file = input("enter the name of the encrypted file u want to be, example:'plain.gpg'   : ")

    # command = ["gpg", "--encrypt", "--recipient", recipient_key_id, "--output", encrypted_file, text_file]
    choice = input("are u sure u wanna do this yes/no ")
    if choice == "yes":
        # Run the subprocess command that requires a yes or no response
        process = subprocess.Popen(
            ["gpg", "--trust-model", "always", "--encrypt", "--recipient", recipient_key_id, "--output", encrypted_file,
             text_file],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        # send "yes" as the response
        process.communicate(input="yes/n")
        if process.returncode == 0:
            print('Command executed successfuly .')
        else:
            print('Command failed .')
        print(f"your just encrypt {text_file} to {encrypted_file}")

    if choice == "no":
        print("bye")


while True:
    choice = input("do you want to import public keys Yes/no: ")

    if choice == 'yes':
        cle_import()
        break
    elif choice == 'no':
        print("\nokay it's your choice bye ")
        break

while True:
    choice = input("do you want de generate a text file  with encryption Yes/no: ")
    if choice == '':
        continue
    break

if choice == 'yes':
    text_generate()
    encryption()

elif choice == 'no':
    print("\nokay it's your choice bye ")
