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
    directory = directory.create_directory('new-directory-name')

    # get the new directory
    directory_new = directory.get('new-directory-name')

    # upload a new file into directory_new
    directory_new = directory_new.upload_file(
        '/path/on/local/computer/to/read/data'
    )

Upload directory recursively
****************************

.. code-block:: python

    import craedl
    profile = craedl.auth()

    # get a research group's project
    research_group = p.get_research_group('url-slug-goes-here')
    project = research_group.get_project('Project Name Goes Here')

    # choose the destination directory within the project
    # this uses the root directory for the project by default
    home = project.get_data()

    # upload the directory recursively
    # this incantation of upload_directory() will pick up from where it left off
    # if it is stopped for any reason
    home = home.upload_directory(
        '/path/on/local/computer/to/read/data',
        rescan=False, # ignores new children in directories already transferred
        output=True # outputs progress to STDOUT
    )
