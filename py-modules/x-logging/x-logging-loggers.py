import logging

logger1 = logging.getLogger("File System")
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger("Connection")
logger2.setLevel(logging.DEBUG)

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log_file_name = "logfile.txt"
logger1.addHandler(logging.FileHandler(log_file_name))
logger2.addHandler(logging.FileHandler(log_file_name))

logger1.propagate = False
logger2.propagate = True

logger1.debug("File system message log")
logger2.debug("Connection message log")

# https://stackoverflow.com/questions/53249304/how-to-list-all-existing-loggers-using-python-logging-module
loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
handlers = [
    logging.getLogger(name).handlers for name in logging.root.manager.loggerDict
]
# print(logging.root.manager.loggerDict)
# print("logger2,handlers:", logger2.handlers)
# print(logger1.__getattribute__("name"))
# print(loggers)
