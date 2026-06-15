import logging
logging.basicConfig(

    level = logging.DEBUG,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("my first app nandha")
logger.debug("This is debug mesaage and useful for code")
logger.critical("This is debug mesaage and useful for code")
logger.warning("This is debug mesaage and useful for code")