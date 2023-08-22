
#
# (c) 2023 MK
#
# code.py
#

class Project(object):
     """ new project basic form """
     def __init__(self):
       super(Project, self).__init__()
       self._name = "Project"
       self._desc = "new python project class"
       self._vers  = "v0.01.08b"
      
     def name(self):
      return self._name

     def desc(self):
       return self._desc

     def vers(self):
       return self._vers
 
     def f(self, x):
      return(x*x)
 


