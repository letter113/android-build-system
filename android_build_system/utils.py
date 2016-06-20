import subprocess
import logging


def run_cmd(cmd, timeout=30):
    logging.info("Running: ")
    logging.info(" ".join(a for a in cmd))
    subprocess.call(cmd, timeout=timeout)


def init_logger():
    formatter = logging.Formatter('%(asctime)s %(levelname)8s %(filename)s @ '
                                  '%(lineno)d %(funcName)s: %(message)s')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    logger.addHandler(console)