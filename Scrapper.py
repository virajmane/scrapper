import re
import pyperclip

def phonescrap(file):
    exp = re.compile(r"\d{10}|[+\d\d]?\d{12}")
    found = []
    with open("{}".format(file), encoding="utf8") as file:
        reading = file.readlines()
    for i in reading:
        found += exp.findall(i)
    with open("scrapped.txt", "w+") as write:
        write.writelines("Phone Numbers are\n")
        write.writelines("\n".join(found))
        write.writelines("\n")

def emailscrap(file):
    exp = re.compile(r"[A-Za-z_.0-9]*@\w{4,7}.com")
    found = []
    with open("{}".format(file), encoding="utf8") as mails:
        reading = mails.readlines()
    for i in reading:
        found += exp.findall(i)
    if found == None:
        print("No Emails Found")
    with open("scrapped.txt", "a") as write:
        write.writelines("\nEmails Are:\n")
        write.writelines("\n".join(found))
print("Please insert the path of the file\n")
file = input(str())
phonescrap(file)
emailscrap(file)
#Scrapper

