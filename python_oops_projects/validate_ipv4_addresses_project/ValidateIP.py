from LoadIP import CustomIP


def ValidateIpv4(set_ip):
    """

    :param set_ip:
    :return:
    """
    ipval = CustomIP(set_ip)
    ip_add = ipval.ip_address()
    ipv4 = ipval.ip_octets
    
    if len(ipv4) == 4:
        c = 0
        for i in range(len(ipv4)):
            if int(ipv4[i]) <= 255:
                pass
            else:
                c = c + 1
        if c <= 0: 
            print(f"{ipval.ip} is a IPV4 IP Adsress and CIDR Block Range is {ipval.cidr_block()}")
        else:
            print(f"{ipval.ip} is not a IPV4 IP Address")
    else:
        print("IPV4 conatains only 4 octets")
        print(f"{ip_add} is not IPV4 IP Address")

set_ip = input("Enter an IP Address (e.g., 192.168.1.10/24):")
ValidateIpv4(set_ip)

    

