from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tasks.scan_updates import scan_updates

def start_scheduler(app):
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        scan_updates,
        "interval",
        minutes=10,
        args=[app]
    )

    scheduler.start()
