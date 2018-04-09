from cw_19_02_2018.di_container import DI_Container, DI_Container_Manager


def Component(cls):
    DI_Container_Manager.get_DI_container().register(cls)
    return cls

def Autowired():
    pass

#isinspect