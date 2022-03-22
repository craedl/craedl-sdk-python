Craedl Python SDK Documentation
===============================

Introduction
************

The Craedl Python SDK (Software Development Kit) enables
`Craedl.org <https://craedl.org>`_ users to access their Craedl accounts using
the Python programming language. This provides a mechanism for using Craedl on
computers without access to a web browser (such as a high-performance computing
cluster) and to automate common Craedl project manipulations (such as file
uploads and downloads) within a Python script.

Quick start
***********

Get started with the Craedl Python SDK by obtaining it via
`PyPI <https://pypi.org/project/craedl/>`_:

.. code-block:: bash

    pip install craedl

Log into your Craedl account at `Craedl.org <https://craedl.org>`_ and generate
an API access token by clicking the key in your profile view. Copy your token
and paste it when prompted after running one of the following commands:

**(A) Configure your account through a system shell**

.. code-block:: bash

    python -m craedl

**(B) Configure your account through an interactive Python interpreter**

.. code-block:: python

    import craedl
    craedl.configure()

Now you can use Python to access your Craedl, for example:

.. code-block:: python

    import craedl
    profile = craedl.auth()
    for craedl in profile.craedls:
        print(craedl)

Documentation
*************

.. toctree::
    docs/basics
    docs/examples
    core/index
