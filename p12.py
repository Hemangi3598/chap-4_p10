# wapp to read username and password
# if username is kaml and password is classes
# then o/p should be succcess else failure


from getpass import *
username = input(" enter your username ")
password = getpass(" enter your password ")
if ( username == "kamal") and (password == "classes"):
	print(" success")
else:
	print("failure")


# input --> echo jo type karoge wo dikhega
# getpass --> non- echo  jo type karoge wo nahi dikhega