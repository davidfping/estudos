import subprocess
import colorama
from datetime import *
colorama.init()


def time():
    while True:
        time = datetime.now()
        timenow = time.strftime('%d/%m/%Y %H:%M')
        timenowsaida = colorama.Fore.MAGENTA + timenow
        return timenowsaida


def PingStatus(host):

    try:
        r = str(subprocess.check_output(f'ping -n 1 {host}'))

        if 'TTL' in r:
            return colorama.Fore.GREEN + 'UP'
    except:
        return colorama.Fore.RED + 'DOWN'

def PingLatencia(host):
    try:
        r = str(subprocess.check_output(f'ping -n 1 {host}'))
        ltlr = list(r.split(' '))
        ltlr = filter(None, ltlr)
        for i in ltlr:
            if i[0] == 't':
                ltl = colorama.Fore.BLUE + 'latencia: ' + colorama.Fore.YELLOW + i
        if 'TTL' in r:
            return ltl
    except:
        return ' '


VPN = ' 10.10.20.80 '
Net = ' google.com.br '
Netsaida = colorama.Fore.YELLOW + 'Internet:'
VPNsaida = colorama.Fore.YELLOW + 'VPN:'


while True:
    print(f'\r{time()} {VPNsaida} {PingStatus(VPN)} {Netsaida} {PingStatus(Net)} {PingLatencia(Net)}', end=" ")

