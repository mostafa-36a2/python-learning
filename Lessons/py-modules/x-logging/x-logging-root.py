import logging

from colorama import Back, Fore, Style

logging.basicConfig(
    # filename="rootlog.txt",  # Instead of printout
    format=f"{Fore.CYAN}%(asctime)s {Fore.BLUE}%(levelname)-8s {Fore.GREEN}%(message)s{Style.RESET_ALL}",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
