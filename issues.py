#  from generate_rule import GenerateRule   
# logger.debug("password policy data = {}".format(response))
match = re.match(r"^([a-z]{2}-[a-z]+-\d{1}).*", self.region)
key=""Deleted""   
# for i in self.rules:  
#     print(i)
#     print('************') 
#     print('************') 
class Rule(object): 
    def __init__(self,name:str, status:str, **kwargs):
      """Create a rule object from the given name and severity""" 
      self.name = name
      self.status = status
      self.kwargs = kwargs
    def __str__(self):
      data = {}
      data['name'] = self.name
      data['status'] = self.status
      for k,v in self.kwargs.items():
        data[k] = v
      return data
    
class GenerateRule(object):
    def __init__(self,name:str, status:str, **kwargs):
      """Create a rule object from the given name and severity"""
      self.name = name
      self.status = status
      self.kwargs = kwargs
    @property
    def data(self):
      data = {}
      data['name'] = self.name
      data['status'] = self.status
      for k,v in self.kwargs.items():
        data[k] = v
      return data


# from generate_rule import GenerateRule
# logger.debug("password policy data = {}".format(response))
match = re.match(r"^([a-z]{2}-[a-z]+-\d{1}).*", self.region)

# for i in self.rules:
#     print(i)
#     print('************')
#     print('************')
class Rule(object):
    def __init__(self,name:str, status:str, **kwargs):
      """Create a rule object from the given name and severity"""
      self.name = name
      self.status = status
      self.kwargs = kwargs
    def __str__(self):
      data = {}
      data['name'] = self.name
      data['status'] = self.status
      for k,v in self.kwargs.items():
        data[k] = v
      return data
    





class GenerateRule(object):
    def __init__(self,name:str, status:str, **kwargs):
      """Create a rule object from the given name and severity"""
      self.name = name
      self.status = status
      self.kwargs = kwargs
    @property
    def data(self):
      data = {}
      data['name'] = self.name
      data['status'] = self.status
      for k,v in self.kwargs.items():
        data[k] = v
      return data














