
#
# code.py
#
# (c) 2023 Mike Knerr
#
# a basic class to instantiate
# for template project new-pyproject
#

class Project(object):
     """ new project basic form """
     def __init__(self):
       super(Project, self).__init__()
       self._name = "Project"
       self._desc = "python project class"
       self._vers  = "v0.01.09"
      
     def name(self):
      return self._name

     def desc(self):
       return self._desc

     def vers(self):
       return self._vers
 
     def f(self, x):
      return(x)

     def sqr(self,x):
      return(x*x)
          
          
 


