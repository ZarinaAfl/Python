from cw_19_02_2018.decorators import *


@Component
class UserController:

    #@Autowired
    def __init__(self, userDAO):
        #self.userDAO = userDAO
        pass

    def process(self):
        #print ("working with %s" % self.userDAO.getName())
        print("DDDD")