
#!/usr/bin/env python
#coding:utf-8

"""
-----Introduction-----
[Core][forward] Device class for c6509.
"""

import re
# from base.sshv2 import sshv2
from forward.models.baseSSHV2 import BASESSHV2
class C6509(BASESSHV2):

        def addUser(self,username = '',password = ''):
                return BASESSHV2.addUser(self,username = username,password = password,addCommand = 'username {username} secret {password}\n')

        def changePassword(self,username = '',password = ''):
                return BASESSHV2.addUser(self,username = username,password = password,addCommand = 'username {username} secret {password}\n')
