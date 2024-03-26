# errors and exceptions

# Nous pouvons créer nos propres classes par 
# sous classe à partir de la classe de base exception
class ValueTooHightError(Exception):
    pass

# En generalement si nous voulons que les classe soient 
# plus petite mais nous pouvous l'écrire comme n'importe quelle autre classe
class ValueSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHightError('value is too high')
    if x < 5:
        raise ValueSmallError('value is too small', x)

try:
    test_value(2)
except ValueTooHightError as e:
    print(e)
except ValueSmallError as e:
    print(e.message, e.value)





# try:
#     a = 5/ 0
#     b = a * 4
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else: 
#     print("everything is fine")
# finally:
#     print('cleaning up...')