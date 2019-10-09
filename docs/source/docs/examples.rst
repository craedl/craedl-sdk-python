Examples
========

Download data
*************

.. code-block:: python

    import craedl
    profile = craedl.auth()

    # get the 0-th project in your list of projects
    project = profile.get_projects()[0]

    # browse the data in your project
    home = project.get_data()

    # get the contents of a particular directory
    directory = home.get('path/to/data/in/Craedl')
    (dirs, files) = directory.list()

    # download the 0-th file's data in this directory
    file_downloaded = files[0].download('path/on/local/computer/to/save/data')

Upload data
***********

.. code-block:: python

    import craedl
    profile = craedl.auth()

    # get the 0-th project in your list of projects
    project = profile.get_projects()[0]

    # browse the data in your project
    home = project.get_data()

    # get a particular directory
    directory = home.get('path/to/data/in/Craedl')

    # create a new directory inside directory
    directory_new = directory.create_directory('new-directory-name')

    # upload a new file into directory_new
    file_new = directory_new.create_file('/path/on/local/computer/to/read/data')
