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

4. Tell your virtualenv to look at the proper settings file. The recommended way to do this is to add the following line to your `.virtualenvs/lilypad/bin/postactivate`:

        export DJANGO_SETTINGS_MODULE=lilypad_server.settings.development

    And this to `.virtualenvs/lilypad/bin/predeactivate`:

        unset DJANGO_SETTINGS_MODULE

5. Launch the server:

        python manage.py runserver
