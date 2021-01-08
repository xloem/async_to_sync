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
        async def sum(self, a, b):
            return a + b
    async_object = async_class()

    # wrap all async methods of an object
    sync_object = sync.methods(async_object)

    assert sync_object.sum(1,2) == 3

    # wrap a single async callable
    sync_function = sync.function(async_object.sum)

    assert sync_function(4,5) == 9

    # wait for a coroutine
    sync_result = sync.coroutine(async_object.sum(6,7))

    assert sync_result == 13

    # manually stop default event loop
    sync.stop()

    # manually start default event loop
    sync.start()
