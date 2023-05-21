def log(logfilename="log.txt"):
    def decorator(original_function):
        def new_function(*args, **kwargs):
            with open(logfilename, "a") as logfile:
                logfile.write(f"Function '{original_function.__name__}' called with positional arguments {args} and keyword arguments {kwargs}.\n")

            return original_function(*args, **kwargs)

        return new_function

    return decorator

@log("someotherfilename.txt")
def my_function(message):
    print(message)


@log("log-analytics.txt")
def somme(x,y):
    print(x+y)

somme(10,11)