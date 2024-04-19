#This approach creates the instance as soon as the class is loaded. It’s simple but may waste resources if the object isn’t used immediately.
class EagerSingleton:
    _instance=None

    @staticmethod
    def getInstance():
        if EagerSingleton._instance is None:
            EagerSingleton._instance=EagerSingleton()
        return EagerSingleton._instance
    
    def __init__(self):
        if self._instance is not None:
            raise Exception("Use getInstance method")



#2nd Approach Lazy Initialisation

import threading


class LazySingleton:
    _instance =None
    _lock=threading.Lock()

    @staticmethod
    def getInstance():
        with LazySingleton._lock:
            if LazySingleton._instance is None:
                LazySingleton._instance=LazySingleton()
        return LazySingleton._instance

    def __init__(self):
        if self._instance is not None:
            raise Exception("Use getInstance method")


#3rd Approach Double Lock Checking

import threading 

class DoubleCheckedLockSingleton:
    _instance=None
    _lock=threading.Lock()

    @staticmethod
    def getInstance():
        if DoubleCheckedLockSingleton._instance is not None:
            with DoubleCheckedLockSingleton._lock:
                if DoubleCheckedLockSingleton._instance is None:
                    DoubleCheckedLockSingleton._instance=DoubleCheckedLockSingleton()
        return DoubleCheckedLockSingleton._instance

    def __init__(self):
        if self._instance is not None:
            raise Exception("Use getInstance method")



#Enum Class Way
#In python we hae to define it by using the class

class EnumSingleton:
    _instance=None

    @staticmethod
    def getInstance():
        if EnumSingleton._instance is None:
            EnumSingleton._instance=EnumSingleton()
        return EnumSingleton._instance
    
    def __init__(self):
        if self._instance is not None:
            raise Exception("Use getInstance method")









