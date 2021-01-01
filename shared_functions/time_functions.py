from datetime import datetime, timedelta


def get_current_timestamp():
    return datetime.now()


def add_time_to_date(timetype, current_time, length):
    timetype = str(timetype)
    if timetype == 'seconds':
        newtime = current_time + timedelta(seconds=length)
    if timetype == 'days':
        newtime = current_time + timedelta(days=length)
    return newtime
