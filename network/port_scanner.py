'''
This script will test the ports at an address which is specified by the user
input is specified through command-line arguments

ex: python port_scanner.py 192.168.0.1
ex: python port_scanner.py 192.168.0.1,192.168.1.1 -p 21,22,80
'''


import socket
import argparse

def main():
    try:
        parser = argparse.ArgumentParser( description='Enter IP Address(es) and Port(s)' )
        parser.add_argument( 'addresses', type=str, nargs='+', help='Target IP Address(es)' )
        parser.add_argument( '-p', '--ports', type=str, nargs='+', help='Target Port(s), if not provided all ports are tested' )
        args = parser.parse_args()
        targetHosts = args.addresses
        if not args.ports:
            targetPorts = [ i for i in xrange( 1, 65536 ) ]
        else:
            targetPorts = map( int, args.ports )

    except:
        print 'error'

    socket.setdefaulttimeout(.2)
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    for host in targetHosts:
        for port in targetPorts:
            try:
                result = sock.connect( ( host, port ) )
                print '[+] Host: %s Open Port: %i' % ( host, port )
            except:
                pass
            

if __name__ == '__main__':
    main()