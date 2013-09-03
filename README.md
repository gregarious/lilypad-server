# Lilypad Server

A Django-based HTTP server hosting the Lilypad API.

## Server Installation (for dev machines)

1.  Install `virtualenv` and `virtualenvwrapper` using [these instructions](http://docs.python-guide.org/en/latest/dev/virtualenvs.html)
    - If you don't have `pip` installed, [check out this guide](http://docs.python-guide.org/en/latest/#getting-started)
      for a full how-to on a good way to set up a local Python installation.

2. Create a new virtual environment for Lilypad:

        $ mkvirtualenv lilypad

3. Install dependencies into the new environment:

        $ pip install -r requirements.txt

4. Three environment variables need to be set:
    1. `DJANGO_SETTINGS_MODULE`: tells any Django process which settings file to use.
    2. `DATABASE_URL`: declares the local DB configuration. You'll need to set up the backend on your own.
    3. `CLIENT_APP_PARENT`: the directory that houses various client-side app repositories. See the note below.

    The recommended way to do this (for development installations, at least) is to add this variable to your virtualenv. To do so, add the following lines to your `.virtualenvs/lilypad/bin/postactivate`, adjusting anything for your environment:

        export DJANGO_SETTINGS_MODULE='lilypad_server.settings.development'
        export DATABASE_URL='postgres://localhost/lilypad_development'
        export CLIENT_APP_PARENT='/path/to/client/repos/parent'

    And this to `.virtualenvs/lilypad/bin/predeactivate`:

        unset DJANGO_SETTINGS_MODULE
        unset DATABASE_URL
        unset CLIENT_APP_PARENT

    _(As an example for_ `CLIENT_APP_PARENT`, _if the `lilypad-pace` repository is cloned at `/home/john/lilypad/lilypad-pace`, the setting would be `/home/john/lilypad`. See "Serving the client app" below for more details.)_

5. Initialize the database

        $ python manage.py syncdb
        $ python manage.py migrate

6 (Optional) Load a data fixture

        $ python manage.py loaddata <fixture_file>

7. Launch the server:

        $ python manage.py runserver

8. Test the server by visiting a valid URL (e.g. http://127.0.0.1:8000/pace/students/)

## Serving the client app (for dev machines)

To avoid cross-site scripting problems, it's easiest to have the Django dev server serve the client apps.

However, since the client apps are in separate repositories, some care must be taken to set up the
environment. The dev server looks in the directory set in the `CLIENT_APP_PARENT` repository for the
cloned client repositories.

For example, to set up the Pace app, assuming you have a directory called `/home/john/lilypad` to house
all your lilypad code:

> 1. Ensure `CLIENT_APP_PARENT` is set to `/home/john/lilypad` (see "Server Installation", step 4)
> 2. Clone the `lilypad-pace` repository into `/home/john/lilypad`
> 3. Profit!

## Production Install Notes

Only the development environment is configured to serve the client apps out of the box. Some care will have to be taken to hook
up the static URLs and index.html pages on a real web server.
