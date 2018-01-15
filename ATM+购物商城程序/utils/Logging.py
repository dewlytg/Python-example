#!/usr/bin/env python

#coding:utf-8

import  logging,datetime

# get current datetime
today = datetime.datetime.now().strftime("%Y-%d-%m")

def logger(level,msg,username):
    # create logger
    logger = logging.getLogger(username)
    logger.setLevel(logging.DEBUG)

    # create file handler and set level to warn
    fh = logging.FileHandler("./logs/%s.%s.log" %(username,today),encoding="utf-8")
    fh.setLevel(logging.INFO)

    # create formatter
    fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
    datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)

    # add formatter to fh and add fh to logger
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    """
    logger.debug("debug message")
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
    logger.critical("critical message")
    """

    if level == "debug":
        logger.debug(msg)
    elif level == "info":
        logger.info(msg)
    elif level == "warning":
        logger.warning(msg)
    elif level == "error":
        logger.error(msg)
    elif level == "critical":
        logger.critical(msg)

if __name__  == "__main__":
    logger("error","this is a error log","tg")
    logger("error","this is a error log","t1")