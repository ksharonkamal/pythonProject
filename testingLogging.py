# import logging
# logging.basicConfig(level=logging.ERROR,filename="example.log", format='%(asctime)s, %(message)s')
# logging.debug("This is a debug message")
# logging.info("This is an info log")
# logging.warning("This is a warning log ")
# logging.error("This is an error log")
# logging.critical("This a critical log")

# import logging
# logging.basicConfig(filename="example.log")
# logging.warning("{0} before you {1}".format("look","leap"))

import logging
logging.basicConfig(filename="example.log",level=logging.DEBUG,format='%(created)f,%(filename)s, %(funcName)s, '
                                                                      '%(levelname)s, %(levelno)s, %(lineno)d, %(message)s')

def fun():
    logging.info("{0} before you {1}".format("look","leap"))
    print("in fun function")
fun()