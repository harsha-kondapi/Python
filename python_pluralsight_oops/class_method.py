class ShippingContainer:

    next_serial = 1337

    @classmethod
    def generateserial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result
    @classmethod
    def create_empty(cls,owner_code):
        return cls(owner_code,contents=[])

    @classmethod
    def create_with_items(cls,owner_code,items):
        return cls(owner_code,contents=list(items))

    def __init__(self,owner_code,contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.generateserial()        #class method

c1 = ShippingContainer("abc",["tools"])
print(c1.next_serial)

c2 = ShippingContainer("xyz",["books"])
print(c2.next_serial)

c3 = ShippingContainer.create_empty("YML")
print(c3.owner_code)
print(c3.contents)

c4 = ShippingContainer.create_with_items("JSON",{1,2,3})
print(c4.contents)

