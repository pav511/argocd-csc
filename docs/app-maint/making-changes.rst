##############
Making Changes
##############

Since the configuration is stored as code, commit messages are required when making changes.
The commit message must start with the site the change is being made for followed by a short description of the change.
Longer descriptions can be handled in the normal git way, but the site prefix is still mandatory.
An example is shown below.

.. code-block:: bash

  git ci -m "Summit: Update command-line for DIMMs."

For larger work, branches and pull requests must be used to effect the changes.
Before merging the pull request, all the commits must be squashed into a single one with a commit message formatted like above.
The site tags used are:

* Summit
* NTS
* TTS
* BTS
