# Keyword Arguments: We can pass argument values by keyword i.e by parameter name.

def wish(name, msg):
    print("hi ", name, msg)

wish(name="darshan lal",msg="good morning , how are you?")

wish(name= "AMit",msg="Bhag saale...... BC")

# Here the order of arguments is not important but number of arguments must be matched.
# Note: We can use both positional and keyword arguments simultaneously. But first we have to take positional arguments and then keyword arguments,otherwise we will get syntaxerror.