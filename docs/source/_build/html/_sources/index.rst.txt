.. Apitalker documentation master file, created by
   sphinx-quickstart on Sun Jul  5 06:19:10 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Apitalker's documentation!
=====================================

Apitalker is a Python wrapper for `Apitalks`_ REST API service. 

.. _Apitalks: https://www.api.store/

**Author**: Radek 'bednaJedna' Bednarik

**Installation**: ``pip install apitalker``

**Repository**: `github`_

**PyPi**: here_

.. _here: https://pypi.org/project/apitalker/

.. _github: https://github.com/bednaJedna/att

Some examples to get you started
--------------------------------

Query single "page" of the API data resource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To send request and return one "page" of data of given resource, use `apitalker.api.API.query()` method.
You can also use mapped data resources in `apitalker.resources` for your convenience.::

   from apitalker.api import API, ApiResponse
   from apitalker.resources import Czso

   api = API("yourapikey")

   r = api.query(Czso.ciselniky_kraj)

   if isinstance(r, ApiResponse):
      print(r.data)

Query for all data (all "pages") of the API data resource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To get all data, which are provided by given resource, you have to query the api repeatedly. For that, use
method `apitalker.api.API.get_data()`.::

   from apitalker.api import API
   from apitalker.resources import Czso

   api = API("yourapikey")

   data, error = api.get_data(Czso.ciselniky_kraj)

   if error is None:
      print(data.as_dataframe.head)

Content
=======


.. toctree::
   :maxdepth: 4

   apitalker
   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
