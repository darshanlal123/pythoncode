# Default Arguments: Sometimes we can provide default values for our positional arguments.
    
def wish(name="Guest"):
    print("Hello",name,"Good Morning")
wish("Durga")
wish()
#  If we are not passing any name then only default value will be considered.

# Note: After default arguments we should not take non default arguments.