import bcrypt



password = input("Enter password: ")
b = password.encode("utf-8")
hashed = bcrypt.hashpw(b, bcrypt.gensalt(rounds=10))
aux = str(hashed)
aux2 = aux[2:]
password = aux2[:-1]
print(password)



