from colorama import init
init()

from colorama import Fore, Back, Style

try:

    the_file = open('sketch.txt')

    for each_line in the_file:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            print(Style.BRIGHT + Fore.RED + role, end='')
            print(Fore.RESET + ' said: ', end='')
            print(Fore.GREEN + line_spoken, end='')
        except TypeError:
            print("TypeError Here!!!!!!!!!!!!!!!!!!!")
        except ValueError:
            pass

    the_file.close()

except IOError:
    print("File not found!!")
