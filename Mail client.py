import smtplib

def msg(message):
    return message


print("***MAIL TESTER***")
print("**Welcome**")
print('*welcome*')
print("Welcome to SMTP sender Script... \n")


while True:
    choice = input("Press 'L' to see list of server host and port numbers or press 'C' to continue: >> ").upper()
    if choice == "L":
        print("Googlemail: smtp.google.com >> 465")
        break
    elif choice == "C":
        print("**Moving on** \n")
        break
    else:
        print("Invalid Option, Please choose a valid option. Please pick an option \n")
        continue


hostname = str(input("[+] Enter Hostname or IP: "))
port = int(input("[+] Enter Port Number: "))
username = str(input("[+] Enter your username: "))
password = str(input("[+] Enter your password: "))
from_address = str(input("[+] Enter From Address: "))
to_address = str(input("[+] Enter TO Address: "))
# msg = str(input("[+] Type Your message: "))

message = msg(input("[+] Enter Your Message: "))
file = open("content.txt", 'w')
file.write(msg(message))

try:
    server = smtplib.SMTP_SSL(hostname, port)
    server.login(username, password)
    server.sendmail(
        from_address,
        to_address,
        message)
    server.quit()
    print("Email sent")
except:
    print("Can't send")
