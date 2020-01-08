
def myxml(standard, content='', **kwargs):
    
    k_w_args = "".join([f' {k}="{v}"'  for k, v in kwargs.items()])
    
    return f"<{standard}{k_w_args}>{content}</{standard}"



print(myxml('foo', 'bar', a=1, b=2, c=3))


##Workthrough
#Take in one arg and return it as a string
def myxml(tagname):
    return f"<{tagname}></{tagname}>"

##args
#*args means take in ANY number of arguments, all of which will be put into a tuple
#*args is meant for situations in which you don’t know how many values you’ll be getting, and you can accept any number.
#Use *args when you’ll put its value into a for loop, and that if you’re grabbing elements from *args with numeric indexes, then you’re probably doing something wrong.

#it doesn't matter whether or not the user passes in content
def myxml(tagname, content=''):
    return f"<{tagname}>{content}</{tagname}>"

##kargs
#When we define a function with **kwargs, we are effectively telling Python that we might pass any name-value pair in the style name=value. 
#kargs are used to create a dictionary: keys are keyword names and values are keyword values
attrs = ''.join([f' {key}="{value}"' for key, value in kwargs.items()])

