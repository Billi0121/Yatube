from rest_framework import throttling
import datetime as dt

class LunchBrakeThrolling(throttling.BaseThrottle):
    def allow_request(self, request, veiw):
        now = dt.datetime.now().hour
        if now >= 22 and now <= 23:
            return False
        return True