import logging


class LoggerManager:

    def __init__(self):

        logging.basicConfig(
            filename="logs/organizer.log",
            level=logging.INFO,
            format="%(asctime)s - %(message)s"
        )

    def log_move(self, source, destination):

        logging.info(
            f"Moved: {source} -> {destination}"
        )
