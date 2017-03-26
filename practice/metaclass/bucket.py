from datetime import timedelta, datetime


class Bucket(object):
    def __init__(self, period):
        self.period_delta = timedelta(period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta

    def __repr__(self):
        return 'Bucket(max_quota=%d, quota_consumed=%d)' % (self.max_quota, self.quota_consumed)


def fill(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True


def test_deduct(amount):
    if deduct(bucket, amount):
        print('Had %d quota' % amount)
    else:
        print('Not enough %d quota' % amount)


if __name__ == '__main__':
    bucket = Bucket(60)
    print('Initial', bucket)

    fill(bucket, 100)
    print('Filled', bucket)

    test_deduct(99)
    print('Now', bucket)

    test_deduct(3)
    print('Still', bucket)
