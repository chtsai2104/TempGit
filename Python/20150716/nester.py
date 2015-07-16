"""This is the "nester.py" module and it provides one function called print_lol()
   which prints lists that may or may not include nested lists."""
def print_lol(list_name):
    """This function takes one positional argument called "list_name", which
       is any Python list (of possibly nested lists). Each data in the
       provided list is (recursively) printed to  the screen on it's own line."""
    for each_item in list_name:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
