class Super:

    #public data member
    var1=None

    #protected data member
    _var2=None

    #private data member
    __var3=None

    #Constructor
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3

    #public member function
    def displayPublicMember(self):

        #accessing public data members
        print("Public Data Member:",self.var1)

    #protected member function
    def _displayProtectedMembers(self):

        #accessing protected data members
        print("Protected Data Member:",self._var2)

    
    #private member function
    def _displayPrivateMembers(self):

        #access private Data Members
        print("Private Data Member:",self.__var3)

    #public member function
    def accessPrivateMembers(self):

        #access private member
        self._displayPrivateMembers()

    
class Sub(Super):

    #constructor
    def __init__(self,var1,var2,var3):
        Super.__init__(self,var1,var2,var3)

    #public member function
    def accessProtectedMembers(self):
        
        #accessing protected member functions of super class
        self._displayProtectedMembers()

#create objects

obj=Sub("Hello","all","people !")

#calling public member functions of the class

obj.displayPublicMember()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

#object can access protected member
print("Object is accessing protected member:",obj._var2)

#object can not access private member,so it will generate Attribute