

from cw_19_02_2018.decorators import *


#@Component
class UserController:

    #@Autowired
    def set_userDAO(self, userDAO):
        self.userDAO = userDAO


    def process(self):
        #print ("working with %s" % self.userDAO.getName())
        print("DDDD")


def Autowired(f):
    pass-
