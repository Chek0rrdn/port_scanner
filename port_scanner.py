#/usr/bin/env python3

import argparse
import socket
import threading

from termcolor import colored


def get_arguments():
    parser = argparse.ArgumentParser(description='Escáner de Puertos')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Host a escanear (Ex. 192.168.1.1)")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Rango de puertos a escanear (EX. -p 1-2000)")
    options = parser.parse_args()

    return options.target, options.port


def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    return s


def port_scanner(port: int, host):
    s = create_socket()

    try:
        s.connect((host, port))
        print(colored(f"\n[+] El puerto {port} esta abierto", 'green'))
    except (socket.timeout, ConnectionRefusedError):
        s.close()
    finally:
        s.close()


def scan_ports(ports, target):
    threads = list()

    for port in ports:
        thread = threading.Thread(target=port_scanner, args=(port, target))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def parse_ports(ports_str):
    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    
    elif ',':
        return map(int, ports_str.split(','))
    
    else:
        return (int(ports_str),)


def main():
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target)



if __name__ == '__main__':
    main()