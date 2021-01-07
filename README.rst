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

    sync_object = sync.methods(async_class())
    sync_function = sync.function(async_class().method)
    sync_function = sync.coroutine(async_class().method())
