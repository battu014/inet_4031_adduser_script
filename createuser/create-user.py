#!/usr/bin/python3
import os 
import re
import sys

def main():
    for line in sys.stdin:
        fields = line.strip().split(':')
        
        match = re.match(r'^#', line)

        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]

        gecos = "%s %s,,," % (fields[2], fields[3])

        groups = fields[4].split(',')

        print("==> Creating accounts for %s..." % (username))

        cmd = "/usr/sbin/adduser -- disabled-password --gecos '%s' %s" % (gecos, username)
        
        os.system(cmd)
        
        print ("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        os.system(cmd)

        for group in groups:
            if group != '-':
                print ("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)

if __name__ == '__main__':
    main()
