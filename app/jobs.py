import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def due_date_notif(task_title):
    time.sleep(5)
    logger.info(f"Reminder: Task '{task_title}' is due soon!")