import logging, sys

def configure_logging(level: int = logging.INFO):
    fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    logging.basicConfig(stream=sys.stdout, level=level, format=fmt)
