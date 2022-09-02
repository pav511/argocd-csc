##############
Making Changes
##############

The repository is enforcing branch protections on ``main``, so a pull request is required to make changes to the configuration.
A branch naming convention is not strictly enforced, but most will be like ``tickets/<Jira ticket key>``.
Since the configuration is stored as code, commit messages are required when making changes.
The commit message must start with the site the change is being made for followed by a short description of the change.
Longer descriptions can be handled in the normal git way, but the site prefix is still mandatory.
An example is shown below.

.. code-block:: bash

  git ci -m "Summit: Update command-line for DIMMs."

All pull requests should be squashed to a single commit to help with rollback.
There are linting tests that need to pass, so make sure that they do.
Pull requests will require a reviewer, so create a pull request and drop the URL into the #ts-build Slack channel.
Someone there will acknowledge they are picking up the pull request and assign it to themselves.
When the pull request is merged, the corresponding branch will be deleted.
The site tags used are:

* ``Summit``
* ``TTS``
* ``BTS``

If a change applies to all sites, use the tag ``All`` at the commit message start.
Changes or updates to documentation only, no configuration or chart changes, should be tagged with ``Docs`` at the commit message start.
Changes or updates to ``bin`` scripts only, no configuration or chart changes, should be tagged with ``Script`` at the commit message start.
