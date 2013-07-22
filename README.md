# Lillypad Server

A Django-based HTTP server hosting the Lilypad API.

## Installation (for dev machines)

1.  Install `virtualenv` and `virtualenvwrapper` using [these instructions](http://docs.python-guide.org/en/latest/dev/virtualenvs.html)
    - If you don't have `pip` installed, [check out this guide](http://docs.python-guide.org/en/latest/#getting-started)
      for a full how-to on a good way to set up a local Python installation.

2. Create a new virtual environment for Lilypad:

        $ mkvirtualenv lilypad

3. Install dependencies into the new environment:

        $ pip install -r requirements.txt

4. Three environment variables need to be set:
    1. `DJANGO_SETTINGS_MODULE`: tells any Django process which settings file to use
    2. `DATABASE_URL`: declares the local DB configuration.
    3. `CLIENT_APP_PARENT`: the directory that houses various client-side app repositories

    The recommended way to do this (for development installations, at least) is to add this variable to your virtualenv. To do so, add the following lines to your `.virtualenvs/lilypad/bin/postactivate`:

        export DJANGO_SETTINGS_MODULE='lilypad_server.settings.development'
        export DATABASE_URL='postgres://localhost/lilypad_development'
        export CLIENT_APP_PARENT='/path/to/client/repos/parent'

    And this to `.virtualenvs/lilypad/bin/predeactivate`:

        unset DJANGO_SETTINGS_MODULE
        unset DATABASE_URL
        unset CLIENT_APP_PARENT

    _(As an example for_ `CLIENT_APP_PARENT`_, if the `lilypad-pace` project is cloned at `/lilypad/lilypad-client/lilypad-pace`, the setting would be `/lilypad/lilypad-client`.)_


5. Launch the server:

        python manage.py runserver


## Production Install Notes

Only the development environment is configured to server the client apps out of the box. Some care will have to be taken to hook
up the static URLs and index.html pages on a real web server.