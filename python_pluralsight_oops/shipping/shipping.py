import iso6346
class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _general_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code,serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6)
        )
    @classmethod
    def create_empty(cls,owner_code,**kwargs):      #named constrcutors or factory methods (basically normal/regular defined methods)
        return cls(owner_code,contents=[],**kwargs)

    @classmethod
    def create_with_items(cls,owner_code,items, **kwargs):      #named constrcutors or factory methods (basically normal/regular defined methods)
        return cls(owner_code,contents=list(items), **kwargs)

    def __init__(self,owner_code,contents, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(         #for polymorphic dispatch invoke static methods through "self"
            owner_code = owner_code,
            serial = ShippingContainer._general_serial()
        )

class RefregiratedShippingContainer(ShippingContainer):

    MAX_CELSIUS  = 4.0

    def __init__(self,owner_code,contents,*,celsius,**kwargs):
        super().__init__(owner_code,contents,**kwargs)
        if celsius > RefregiratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self.celsius = celsius


    @staticmethod
    def _make_bic_code(owner_code,serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6),
            category= 'R'
        )
'''
c1 = ShippingContainer("abc",["tools"])
print(c1.next_serial)

c3 = ShippingContainer("pqr",["shoes"])
print(c3.owner_code)

c4 = ShippingContainer.create_empty("YML")
print(c4.owner_code)

c5 = ShippingContainer.create_with_items("JSON",{1,2,3})
print(c5.owner_code,c5.contents)
'''