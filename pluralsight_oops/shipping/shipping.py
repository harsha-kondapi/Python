class ShippingContainer:

    next_serial = 1337

    def __init__(self,owner_code,contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self.next_serial
        self.next_serial += 1

c1 = ShippingContainer("abc",["tools"])
print(c1.next_serial)


c2 = ShippingContainer("xyz",["books"])
print(c2.next_serial)

