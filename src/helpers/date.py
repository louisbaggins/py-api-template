from datetime import datetime, timezone, timedelta
import dateutil.parser

def get_now_iso(timezone_offset, minusDays):
    now = datetime.utcnow().astimezone(timezone(-timedelta(hours=3)))
    now = now - timedelta(days=minusDays)
    return now.isoformat().replace(timezone_offset, 'Z')
