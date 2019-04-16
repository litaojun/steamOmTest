class ProxyHook(object):
    def __init__(self,   **kwargs):
        self.clsHook = []
        self.funHook = []
        self.kwargs = kwargs
    def register_hook(self, obj):
        if hasattr(obj,"__call__"):
            self.funHook.append(obj)
        else:
            self.clsHook.append(obj)

    def __call__(self,**kwargs):
        self.run(**kwargs)

    def run(self,**kwargs):
        if len(self.funHook):
            for fun in self.funHook:
                fun(**kwargs)
        if len(self.clsHook)>0:
            for cls in self.clsHook:
                cls(**kwargs).run()