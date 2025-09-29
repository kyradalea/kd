dict = {
    "Hans" : 24,
    "Prag" : 23,
    "Bunyod" : 18,
}

print(dict)
print(dict["Prag"])

dict["Prag"] = 30
print(dict["Prag"])

del dict["Bunyod"]
print(dict)