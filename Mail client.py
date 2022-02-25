import smtplib

print("***MAIL TESTER***")
print("**Welcome**")
print("Welcome to SMTP sender Script... \n")
choice = input("Press 'L' to see list of server host and port numbers or press 'C' to continue: >> ").upper()

while True:
    if choice == "L":
        print("Googlemail: smtp.google.com >> 465")
        break
    elif choice == "C":
        print("**Moving on**")
        break
    else:
        print("Invalid Option, Please choose a valid option.")
        break

hostname = str(input("Enter Hostname or IP: "))
port = int(input("Enter Port Number: "))
username = str(input("Enter your username: "))
password = str(input("Enter your password: "))
from_address = str(input("Enter From Address: "))
to_address = str(input("Enter TO Address: "))
msg = str(input("Type Your message: "))


server = smtplib.SMTP_SSL(hostname, port)
server.login(username, password)
server.sendmail(
    from_address,
    to_address,
    msg)
server.quit()
