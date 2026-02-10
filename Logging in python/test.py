"""
Logging is used to track events that occurs in software when it runs.
It is used in development, debugging, testing etc.
It is useful to track the error, exception, and information.
This module can be used with frameworks like django, flask etc.

"""



# from logging import *
# basicConfig(filename='app.log', level=DEBUG)

# basicConfig(level=INFO)

# basicConfig(level=40)   #error level

# debug("This is debug message") #10
# info("module got completed ") #20
# warning("The warning message is displaying") #30
# error("The error message is displaying")  #40
# critical('The critical message is displaying')  #50



#* change format of log message

# from logging import * 

# basicConfig(filename='app1.log',
#             level=DEBUG,
#             filemode='w',
#             # format='%(asctime)s:%(message)s:%(levelname)s:%(name)s:%(process)s:%(lineno)s',
#             format='{asctime}|{message}|{levelname}|{name}|{process}|{lineno}',
#             datefmt='%d-%b-%y %H:%M:%S', style="{")

# debug('this is debug message.')
# info("The info message is displaying")
# warning('This is warning message displaying')
# error("The error message is displaying")  #40
# critical('The critical message is displaying')  #50





#* Creating logger object:-


import logging
import sys


logging.basicConfig(filename='app2.log', filemode='w', format="{name}: {levelname}: {message}", style="{")


# logger = logging.getLogger("sushil")
# logger = logging.getLogger(sys.argv[0])
logger = logging.getLogger(__name__)
logger.setLevel(10)

logger.info("Here is the information.")
logger.error("Error message goes here")

