=============
async_to_sync
=============

Convert async coroutine functions to normal ones.

Installation
------------

.. code-block:: bash

    $ pip install async_to_sync

Usage
-----

.. code-block:: python

    import async_to_sync as sync

    # an async object method to demonstrate use
    class async_class:
        async def method(self):
            return True
    async_object = async_class()

    # wrap all async methods of an object
    sync_object = sync.methods(async_object)

    assert sync_object.method() is True

    # wrap a single async callable
    sync_function = sync.function(async_object.method)

    assert sync_function() is True

    # wait for a coroutine
    sync_result = sync.coroutine(async_object.method())

    assert sync_result is True

    # manually stop default event loop
    sync.stop()

    # manually start default event loop
    sync.start()
