'''
The crypt library is not available on windows. Will use the hashlib module
'''
import hashlib

def main():
    with open( '..\lib\dictionary.txt', 'r' ) as dictionary:
        with open( '..\lib\hashedPasswords.txt', 'r' ) as hashedPasswords:
            hashedWords = hashedPasswords.readlines()
            for password in dictionary.readlines():
                hashedPassword = hashlib.sha512( password.strip('\n') ).hexdigest()
                if hashedPassword in hashedWords:
                    print "[+] Password is %s for hash %s\n\n" % ( password, hashedPassword )
                
if __name__ == '__main__':
    main()