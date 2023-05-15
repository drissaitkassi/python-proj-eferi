def log(original_function):
    """ decorateur qui reçoit une fonctionne (original function) et qui fait 
    deux actions :
    1) crée un ficher log.txt et ecrir dedans le nom de la fonction original  function et ses arguments 
    2) executer la fonction original function avec les argument donnée
    
    """
    def new_function(*args, **kwargs):
        
        with open("log.txt", "w") as logfile:
            logfile.write(f"Function '{original_function.__name__}' called with positional arguments {args} and keyword arguments {kwargs}.\n")
        print("message afficher sur toutes les fonctiones décorée")
        return original_function(*args, **kwargs)

    return new_function



# Better decorating directly on its definition
@log
def my_function(message):
    print(message)

@log
def somme(x,y):
    print(x+y)

somme(10,11)
#my_function("test message")