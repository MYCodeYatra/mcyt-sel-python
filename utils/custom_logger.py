import logging
import os
from datetime import datetime
class CustomLogger:
    @staticmethod
    def get_logger(name="AutomationFramework"):
        """
        Creates a custom logger that outputs to both Console and a File.
        """
        logger = logging.getLogger(name)
        # If the logger already has handlers, return it to prevent duplicate logs
        if logger.hasHandlers():
            return logger
        logger.setLevel(logging.DEBUG)
        # 1. Create a dynamic log file name with today's date
        log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d")
        log_file = os.path.join(log_dir, f"automation_{date_str}.log")
        # 2. Create Handlers (File and Console)
        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()
        # 3. Create a beautiful Log Format: [DATE] [LEVEL] [LOGGER] Message
        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - [%(name)s] : %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        # 4. Attach the Handlers to the Logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        return logger