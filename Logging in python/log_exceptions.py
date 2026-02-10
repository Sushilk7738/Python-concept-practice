import logging

# logging.basicConfig(level=logging.DEBUG, filemode='w', filename='test.log',
#                 format="{asctime}|{name} |{message}", style="{")

# try:
#     age = int(input("Enter your age: "))
# except Exception as obj:
#     """There are 3 way to log error"""

#     logging.error(obj)
    
    # logging.error('Exception Details: ',exc_info=True)

    # logging.exception('Exception Details: ')
    
    
# ==========================================================================================

logging.basicConfig(level=logging.DEBUG, filemode='w', filename='test.log',
                    format='{asctime}: {name}: {message}', style="{")

class AccessDenied(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AccessDenied("Access Denied !")
    logging.info(f'A user having age {age} has logged in.')

except Exception as obj:
    logging.exception(obj)
    
    
    
    