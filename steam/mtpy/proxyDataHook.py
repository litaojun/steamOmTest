class LazyPerson(object):
    def __init__(self,   **kwargs):
        self.clsHook = []
        self.funHook = []
        self.kwargs = kwargs
    def register_hook(self, obj):
        if hasattr(obj,"__call__"):
            self.funHook.append(obj)
        else:
            self.clsHook.append(obj)

    def __call__(self,):
        self.run()

    def run(self):
        if len(self.funHook):
            for fun in self.funHook:
                fun(self.kwargs)
        if len(self.clsHook)>0:
            for cls in self.clsHook:
                cls(self.kwargs).run()