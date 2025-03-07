name = input("What is your Name?")
surname = input("What is your Surname?")



try:
    with open("student.txt","a") as file:
        file.write(f"My Name is : {name}\n")
        file.write(f"My SurName is : {surname}\n")
except Exception as e:
    print("File is not Found")

try:
    with open("student.txt","r") as file:
        for line in file.readlines():
            print(line)
except Exception as e:
    print("File is not Found")

