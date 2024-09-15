import os
import subprocess
 

current_directory = os.path.dirname(os.path.abspath(__name__))

def cle_import():
    folder_path = input("type the path of your public keys :")

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            pass
        print("Processing file:", filename)
        command = ["gpg", "--import", file_path]
        subprocess.run(command)


def text_generate(): 
    global file_path
    filename = "generated.txt"
    file_path = os.path.join(current_directory, filename)
    text = input("write your text :")
    with open(file_path, "w") as f:
        f.write(text)

    print(f"the text file is generated in '{file_path}'")


def encryption():
    encrypted_file = file_path+".gpg"
    print("showing imported keys.....")
    keys_output = subprocess.check_output(["gpg", "--list-keys"])
    keys_output = keys_output.decode("utf-8")
    print(keys_output)
    recipient_key_id = str(input("enter the id or the gmail for the public key. example:'root@gmail.com' : "))
    choice = input("are you sure you wanna do this yes/no :")
    if choice == "yes":
        process = subprocess.Popen(
            ["gpg", "--trust-model", "always", "--encrypt", "--recipient", recipient_key_id, "--output" , encrypted_file, file_path],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        process.communicate(input="yes/n")
        if process.returncode == 0:
            print('Command executed successfuly .')
        else:
            print('Command failed .')
        print(f"your just encrypt {encrypted_file}")

    if choice == "no":
        print("good bye...")
        time.sleep(2)

if __name__ == "__main__":
    try:
        choice = str(input("Do you want to import public keys (yes/no): ").strip().lower())
        
        if choice == 'yes':
            cle_import()  # Call your cle_import function
            
        elif choice == 'no':
            print("\nOkay, it's your choice.")
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")
    
    except ValueError as e:
        print(f"An error occurred: {e}")

    try:
        choice = str(input("do you want de generate a text file  with encryption (yes/no): ").strip().lower())
        if choice == 'yes':
            text_generate()
            encryption()
        elif choice == 'no':
            print("\nokay it's your choice bye ")
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")    
    except ValueError as e :
        print(f"An error occurred: {e}")