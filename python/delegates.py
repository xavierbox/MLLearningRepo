# delegation 

from typing import Any


class A:

    def __init__( self ):
        self.name = 'I ma class A'
    
    def __len__(self): 
        print('called class A len ')
        return 4 

    def talk( self):
        print( 'class a talking ')

        

class B:

    def __init__( self ):
        self._a  = A()

    def __getattr__(self, name: str) -> Any:
        print( 'enterin g here 1 ')
        return getattr( self._a, name) #  .getattribute__(name)

    #def __getattr__(self, name: str) -> Any:
    #    return getattr( self._a, name )


class Yeah:

    def __init__(self, data):
        self.name = 'name'
        self.d = data  

    
    # Gets called when an attribute is accessed
    #def __getattribute__(self, item):
    #    print ('__getattribute__ ', item)
    #    #return None 
    #    # Calling the super class to avoid recursion
    #    return self.d.__getattribute__(item)
    
    # Gets called when the item is not found via __getattribute__

    def __len__(self):
        return len( self.d.samples )
    
    def __getattr__(self, item):
        print( 'Not found __getattr__ ', item)
        return self.d.__getattribute__(item)



y1 = Yeah( image_datasets['train'])
y1.name
y1.samples

print('len')
#y1.samples  
y1.class_to_idx