import asyncio
import atexit
import threading

_loop = None
_thread = None
def get_event_loop():
    global _loop, _thread
    if _thread is None:
        if _loop is None:
            _loop = asyncio.get_event_loop()
        _thread = threading.Thread(target=_loop.run_forever)
        _thread.start()
    return _loop
def start():
    get_event_loop()
def stop():
    global _loop, _thread
    if _loop is not None:
        _loop.call_soon_threadsafe(_loop.stop)
    if _thread is not None:
        _thread.join()
        _thread = None

def coroutine(coroutine, loop = None):
    if loop is None:
        loop = get_event_loop()
    future = asyncio.run_coroutine_threadsafe(coroutine, loop)
    result = future.result()
    return result

def function(function, loop = None):
    def call(*params, **kwparams):
        async_coroutine = function(*params, **kwparams)
        return coroutine(async_coroutine, loop)
    return call

class methods:
    def __init__(self, object, loop = None):
        self.__object = object
        self.__loop = loop
    def __getattr__(self, name):
        result = getattr(self.__object, name)
        if asyncio.iscoroutinefunction(result):
            return function(result, self.__loop)
        else:
            return result
