from myhdl import _Signal



class SignalCollection(object):
    def __init__(self):
        pass

        

    def get_signal_names(self):
        def test(x):
            return isinstance(x,_Signal._Signal)

        return [k for k,v in self.__dict__.items() if test(v)]

    
    def get_signals(self):
        for k,v in self.__dict__.items():
            if isinstance(v,_Signal._Signal):
                yield k,v
 

    def assign(self,_id,new_sig):
        if _id in self.__dict__:
            if type(self.__dict__[id])==type(new_sig):
                self.__dict__[id] =  new_sig
            else:
                raise ("error")
