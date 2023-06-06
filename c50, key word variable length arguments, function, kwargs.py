# key word variable length arguments
# For this we have to use **.
# We can call this function by passing any number of keyword arguments. 
# Internally these keyword arguments will be stored inside a dictionary.

def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"--",v)

display(name = "darshan lal", mobile ="8565999", email= "darshanlalinfo@gmail.com")
