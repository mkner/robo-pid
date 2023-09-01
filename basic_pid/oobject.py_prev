
class Object(object):
     # successive classes override
     # these in init
     def __init__(self): #,instance="Instance Name"):
         self._id = id(self)
         self._name="Object"
         self._desc="Object - base class"
         self._vers="v0.01.07"
         self._model = "" # more for derived classes
         self._about="About object class"
         self._instance_name = ""
         self._debug_flag = False
       
     def whoami(self):
          print(self._name,self._vers,self._model)
     
     def getWhoami(self):
         return str(self._name+" "+self._vers+" "+self._model)
     
     def whoamiStr(self):
         return self.getWhoami()
     
     def getId(self):
         return self._id
     
     def getName(self):
           return self._name

     def getDesc(self):
        return self._desc
    
     def getVersion(self):
        return self._vers
    
     def getVers(self):
        return self._vers
    
     def getAbout(self):
        return self._about
    
     def setName(self,n):
         self._name = n
    
     def setDesc(self,d):
         self._desc = d
     
     #def setVers(self,v):
     #    self._vers =v
         
     #def setAbout(self,a):
     #     self._about = a
    
     def setDebugOn(self):
         self._debug_flag = True
         
     def setDebugOff(self):
         self._debug_flag = False
     
     def debugOn(self):
         self.setDebugOn()
     
     def debugOff(self):
         self.setDebugOff()
         
    # the shell commands
     
     def id(self):
         print(self._id)
         
     def name(self):
           print(self._name)

     def desc(self):
        print(self._desc)
    
     def version(self):
        print(self._vers)
    
     def vers(self):
        print(self._vers)
    
     def about(self):
        print(self._about)
        
     def debug(self):
         return self._debug_flag
     
     def isDebugOn(self):
         # backward compat
         return self.debugIsOn()
          #return self.debug()
      
     def debugIsOn(self):
         # makes more sense w/ if debugIsOn():...
         return self._debug_flag
        #return self.debug()
      

 
