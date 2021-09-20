import re
import socket


def is_ip_valid(ip_address):
    ip_pattern = "^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\\.(?!$)|$)){4}$"
    return re.match(ip_pattern, ip_address)


def is_ip_valid_via_socket(ip_address):
    try:
        socket.inet_pton(socket.AF_INET, ip_address)
    except AttributeError:
        try:
            socket.inet_aton(ip_address)
        except socket.error:
            return False
    except socket.error:
        return False
    return True
