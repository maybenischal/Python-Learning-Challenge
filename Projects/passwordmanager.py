passkey = input("Enter your master password: ")

def view():
    with open('./password.text','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User: ", user, "Password: ", password,)

def add():
    id = input("Enter your username: ")
    pwd = input("Enter your passsowrd: ")
    with open('./password.text','a' ) as f:
        f.write( id + " | " + pwd + "\n")

while True:
    mode = input("Would you like to add password or view existing password? (add/view) or press q to quit ").lower()

    if mode == "q":
        break

    if mode == "add":
        add()

    elif mode == "view":
        view()
    
    else:
        print("Invalid mode.")
    