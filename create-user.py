#!/usr/bin/python3
import os 
import re
import sys

def main():
    for line in sys.stdin:

        #split the line using : 
        fields = line.strip().split(':')
        
        #use re.match to check for # lines
        match = re.match(r'^#', line)
        
        #check if the fields variable has 5 elements
        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]
        
        #combine last and first name into gecos variable
        gecos = "%s %s,,," % (fields[2], fields[3])
        
        #if there is multiple groups, separate them using ,
        groups = fields[4].split(',')

        print("==> Creating accounts for %s..." % (username))
        
        #create user with gecos information
        cmd = "/usr/sbin/adduser -- disabled-password --gecos '%s' %s" % (gecos, username)
        
        os.system(cmd)
        #set user's password
        print ("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        os.system(cmd)
        
        #add users to the group
        for group in groups:
            if group != '-':
                print ("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)

if __name__ == '__main__':
    main()
