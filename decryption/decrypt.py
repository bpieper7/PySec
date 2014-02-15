'''
The crypt library is not available on windows. Will use the hashlib module.

This file will get hashed password list from PySec\lib\hashedPasswords.txt and then
    attempt to do a dictionary attack on the basis of user input.

If the user does not input an decryption type then this script will attempt to run
    all decryption methods.
'''
import argparse
import hashlib

def main():
    dict = { 'md5' : useMD5, 'sha1' : useSHA1, 'sha224' : useSHA224, 'sha256' : useSHA256, 'sha384' : useSHA384, 'sha512' : useSHA512, '' : useAllDecryption }
    try:
        parser = argparse.ArgumentParser( description='Enter type of encryption method, none will attempt to run all' )
        parser.add_argument( 'type', type=str, nargs='*', help='Will only run specified encryption type. md5 sha1 sha224 sha256 sha384 sha512 or none (runs all)' )
        args = parser.parse_args()
        types = map( lambda x:x.lower(), args.type )
    except:
        print 'error getting input'
        
    with open( '..\lib\dictionary.txt', 'r' ) as dictionary:
        with open( '..\lib\hashedPasswords.txt', 'r' ) as hashedPasswords:
            hashedWords = hashedPasswords.readlines()
            if not types:   # if the user did not specify a decryption type
                useAllDecryption( hashedWords, dictionary )
            else:
                for password in dictionary.readlines():
                    for type in types:
                        hashedPassword = dict[ type ]( password.strip('\n') )
                        if hashedPassword in hashedWords:
                            print "[+] Password is %s for hash %s\n\n" % ( password, hashedPassword )
                
def useAllDecryption( hashedWords, dictionary ):
    for password in dictionary.readlines():
        if useMD5( password.strip( '\n' ) ) in hashedWords:
            print "[+] Password is %s for hash %s\n\n" % ( password, useMD5( password.strip( '\n' ) ) )
        elif useSHA1( password.strip( '\n' ) ) in hashedWords:
            print "[+] Password is %s for hash %s\n\n" % ( password, useSHA1( password.strip( '\n' ) ) )
        elif useSHA224( password.strip( '\n' ) ) in hashedWords:
            print "[+] Password is %s for hash %s\n\n" % ( password, useSHA224( password.strip( '\n' ) ) )
        elif useSHA256( password.strip( '\n' ) ) in hashedWords:
            print "[+] Password is %s for hash %s\n\n" % ( password, useSHA256( password.strip( '\n' ) ) )
        elif useSHA512( password.strip( '\n' ) ) in hashedWords:
            print "[+] Password is %s for hash %s\n\n" % ( password, useSHA512( password.strip( '\n' ) ) )
            
def useMD5( password ):
    return hashlib.md5( password ).hexdigest()
def useSHA1( password ):  
    return hashlib.sha1( password ).hexdigest()
def useSHA224( password ):
    return hashlib.sha224( password ).hexdigest()
def useSHA256( password ):
    return hashlib.sha256( password ).hexdigest()
def useSHA384( password ):
    return hashlib.sha384( password ).hexdigest()
def useSHA512( password ):
    return hashlib.sha512( password ).hexdigest()
    
if __name__ == '__main__':
    main()