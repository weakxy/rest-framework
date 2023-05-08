from rest_framework.throttling import BaseThrottle, SimpleRateThrottle


class MyThrottles(SimpleRateThrottle):
    # def allow_request(self, request, view):
    #     pass
    #
    # def wait(self):
    #     pass
    # scope = "none"   scope可以用来起名（比如没有登录的）
    scope = "weakxy"

    def get_cache_key(self, request, view):
        return request.user
