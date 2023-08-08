from LoadIP import CustomIP

ip1 = CustomIP("10.0.1.255")
result = ip1.cidr()

print(result)
