import urllib.request

try:
    webUrl = urllib.request.urlopen('https://www.python.org/', timeout=5)
except:
    print('\033[31mO site pudim não está acessível no momento... =C\033[m')
else:
    print('\033[32mO site pudim está acessível no momento!\033[m')
