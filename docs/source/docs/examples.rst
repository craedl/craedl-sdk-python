Examples
========

See Craedls
***********

.. code-block:: python

    import craedl
    profile = craedl.auth()

    # print your craedl tree
    for craedl in profile.craedls:
      print(craedl)

    # get a particular craedl
    craedl = profile.get_craedl('craedl-slug', 1)

Printing the Craedl tree generates output such as:

.. code-block:: bash

    Test Craedl [craedl-slug:1]
      - Child 1 [craedl-slug:2]
          - Child 1a [craedl-slug:5]
              - Child 1a1 [craedl-slug:7]
          - Child 1b [craedl-slug:8]
          - Child 1c [craedl-slug:9]
      - Child 2 [craedl-slug:3]
          - Child 2a [craedl-slug:4]

where 'craedl-slug' is the Craedl's slug (visible in the URL through the web browser)
and the number is the Craedl's ID. Getting a particular Craedl requires this
slug and ID.

Download data
*************

.. code-block:: python

    import craedl
    profile = craedl.auth()

    # get a craedl
    craedl = profile.get_craedl('craedl-slug', 1)

    # access the data in your craedl
    root = craedl.get_data()

    # get the contents of a particular directory
    directory = root.get('path/to/data/in/Craedl')
    children = directory.list()
    for directories in children['dirs']:
      print(directories)
    for files in children['files']:
      print(files)

    # download the 0-th file's data in this directory
    file_downloaded = files[0].download('path/on/local/computer/to/save/data')

Upload data
***********

.. code-block:: python

    import craedl
    profile = craedl.auth()

    # get a craedl
    craedl = profile.get_craedl('craedl-slug', 1)

    # access the data in your craedl
    root = craedl.get_data()

    # get a particular directory
    directory = root.get('path/to/data/in/Craedl')

    # create a new directory inside directory
    directory_new = directory.create_directory('new-directory-name')

    # upload a new file into directory_new
    directory_new = directory_new.upload(
        '/path/on/local/computer/to/read/data'
    )

Upload directory recursively
****************************

.. code-block:: python

    import craedl
    profile = craedl.auth()

    # get a craedl
    craedl = profile.get_craedl('craedl-slug', 1)

    # access the data in your craedl
    root = craedl.get_data()

    # get a particular directory
    directory = root.get('path/to/data/in/Craedl')

    # upload the directory recursively
    # this incantation of upload() will pick up from where it left off
    # if it is stopped for any reason
    directory = directory.upload(
        '/path/on/local/computer/to/read/data',
        rescan=False, # ignores new children in directories already transferred
        output=True # outputs progress to STDOUT
    )
