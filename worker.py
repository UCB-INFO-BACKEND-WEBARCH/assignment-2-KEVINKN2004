import os
from redis import Redis
from rq import Connection, SimpleWorker
from rq.timeouts import TimerDeathPenalty
from dotenv import load_dotenv

load_dotenv()

class WindowsSimpleWorker(SimpleWorker):
    death_penalty_class = TimerDeathPenalty

if __name__ == "__main__":
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
    connection = Redis.from_url(redis_url)
    with Connection(connection):
        worker = WindowsSimpleWorker(["default"])
        worker.work()