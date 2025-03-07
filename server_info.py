import csv

try:
    with open('server_details.csv','r') as file:
        server_info=csv.reader(file)
        for server in server_info:
            print(f"Server Name : {server[0]}")
except Exception as e:
    print("Unable to find server_details.csv")

