# Lillypad Server

A Django-based HTTP server hosting the Lilypad API.

## Installation (for dev machines)

1.  Install `virtualenv` and `virtualenvwrapper` using [these instructions](http://docs.python-guide.org/en/latest/dev/virtualenvs.html)
    - If you don't have `pip` installed, [check out this guide](http://docs.python-guide.org/en/latest/#getting-started)
      for a full how-to on a good way to set up a local Python installation.

2. Create a new virtual environment for Lilypad:

        $ mkvirtualenv lilypad

3. Install dependencies into the new environment:

    First manually install the source version of the Django 1.4 nonrel packages:

        $ pip install git+https://github.com/django-nonrel/django@nonrel-1.4
        $ pip install git+https://github.com/django-nonrel/djangotoolbox@toolbox-1.4
        $ pip install git+https://github.com/django-nonrel/mongodb-engine@mongodb-engine-1.4-beta

    Then install the rest of the requirements:

        $ pip install -r requirements.txt

4. Since there's no standard `settings` module, the `DJANGO_SETTINGS_MODULE` environment variable needs to be set before any Django process is run. The recommended way to do this (for development installations, at least) is to add this variable to your virtualenv. To do so, add the following line to your `.virtualenvs/lilypad/bin/postactivate`:

        export DJANGO_SETTINGS_MODULE=lilypad_server.settings.development

    And this to `.virtualenvs/lilypad/bin/predeactivate`:

        unset DJANGO_SETTINGS_MODULE

5. Launch the server:

        python manage.py runserver
