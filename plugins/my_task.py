import json
class MyTask:
    def __init__(self,param1, param2, param3, param4):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.vals = {
            'Output1' : [],
            'Output2' : [],
            'Output3' : [],
            'Output4' : [],
        }
    
    def my_function(self):
        self.vals['Output1'].append(self.param1)
        self.vals['Output2'].append(self.param2)
        self.vals['Output3'].append(self.param3)
        self.vals['Output4'].append(self.param4)
        return json.dumps(self.vals, indent = 4)