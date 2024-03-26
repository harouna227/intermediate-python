def check_palindrome(val):
    if len(val) < 1:
        return True
    else:
        if val[0] == val[-1]:
            return check_palindrome(val[1:-1])
        else:
            return False

var = input(("Entrez une valeur: "))
if(check_palindrome(var)):
    print("L'entrée est un palindrome")
else:
    print("L'entrée n'est pas un palindrome")