import socket


class Host:

    @staticmethod
    def get_name():
        return socket.gethostname()

    @staticmethod
    def get_ip_address():
        try:
            if socket.has_ipv6:
                for res in socket.getaddrinfo('localhost',
                                              0,
                                              0,
                                              socket.SOCK_STREAM):
                    af, socktype, proto, canonname, sa = res
                    if af == socket.AF_INET6:
                        return sa[0]
            else:
                return socket.gethostbyname(Host.get_name())
        except socket.error as err_msg:
            return err_msg

    @staticmethod
    def get_remote_machine_info(remote_host):
        try:
            return socket.gethostbyname(remote_host)
        except socket.error as err_msg:
            print("%s: %s" %(remote_host, err_msg))

    @staticmethod
    def find_service_name(port, protocol='tcp'):
        return socket.getservbyport(port, protocol)

    @staticmethod
    def get_socket_timeout():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return s.gettimeout()

    @staticmethod
    def set_socket_timeout(timeout):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)


if __name__ == "__main__":
    print(Host.get_ip_address())
    print("Local host is: %s [%s]" % (Host.get_name(), Host.get_ip_address()))

    _remote_host = 'www.python.org'
    print("Remote address: %s [%s]" %
          (_remote_host, Host.get_remote_machine_info(_remote_host)))

    for _port in [80, 25]:
        print("Port (%s) is running service - %s" %
              (_port, Host.find_service_name(_port)))

    _port = 53
    print("Port (%s) is running service - %s" %
          (_port, Host.find_service_name(_port, 'udp')))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Current socket timeout: %s" % s.gettimeout())
    print("Setting socket timeout to 100")
    s.settimeout(100)
    print("Current socket timeout: %s" % s.gettimeout())
