def decor_input(func):
    def inner(name):
        if name=="darshan":
            print("hi darshan very very good morning ")
        else:
            func(name)
    return inner

@decor_input
def wish(name):
    print("good morning")

wish("amit")
wish("darshan")