import inspect

components_packages = ["controllers", "dao"]

class DI_Container:

    def __init__(self):
        self.beans = {}


    def register(self, cls):
        self.beans[cls.__name__] = cls()


    def get_bean(self, cls):
        classname = cls.__name__
        return  self.beans[classname]


class DI_Container_Manager:
    __di_container = DI_Container
