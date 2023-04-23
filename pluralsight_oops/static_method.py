class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self,owner_code,contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()


c1 = ShippingContainer("ESC",["Electronis"])
print(c1.serial)
print(ShippingContainer.next_serial)

c2 = ShippingContainer("ESC",["Electronis"])
print(c2.serial)
print(ShippingContainer.next_serial)
