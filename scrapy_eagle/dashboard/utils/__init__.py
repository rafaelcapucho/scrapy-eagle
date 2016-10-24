from datetime import datetime
from calendar import timegm


def iso_to_timestamp(iso):
    epoch = timegm(datetime.strptime(iso, "%Y-%m-%dT%H:%M:%S.%f").timetuple())
    assert isinstance(epoch, int)
    return epoch


def timestamp_to_utc(ts):
    return datetime.utcfromtimestamp(ts)
