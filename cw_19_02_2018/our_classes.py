from cw_19_02_2018 import UserController
from cw_19_02_2018.di_container import DI_Container, DI_Container_Manager

if __name__ == "__main___":
    di_cont = DI_Container_Manager.get_DI_Container()
    uc = DI_Container.get_bean(UserController)
    uc.process()