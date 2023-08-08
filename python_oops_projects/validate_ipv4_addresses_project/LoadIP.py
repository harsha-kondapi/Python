class CustomIP:
    def __init__(self,user_input):
        self.user_input = user_input

    def cidr_block(self):
        if '/' in self.user_input:       
            self.ipcidr = self.user_input.split("/")
            self.cidr_range = int(self.ipcidr[1])
            return self.cidr_range
        else:
            self.ipcidr = self.user_input
            self.cidr_range = 32
            return self.cidr_range

    def ip_address(self):
        self.cidr_block()
        if '/' in self.user_input:    
            self.ip_octets = self.ipcidr[0].split(".")
            self.ip = self.ipcidr[0]
            return self.ip
        else:
            self.ip_octets = self.ipcidr.split(".")
            self.ip = self.ipcidr
            return self.ip

