from log import logging
def add(a,b):
    logging.debug("Addition operation is getting performed")
    return a+b
logging.debug("add function is called")
add(2,3)