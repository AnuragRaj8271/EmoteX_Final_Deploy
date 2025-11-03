def middleware(request, call_next):
    return call_next(request)
