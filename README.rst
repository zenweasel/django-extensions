===================
 Django Extensions
===================

Django Extensions is a collection of custom extensions for the Django Framework.

Customizations of this fork
===========================

This fork changes the way the IPython shell is loaded to be able to add additional configuration and startup logic to the 
Django shell. 
It loads the users IPython configuration (from ~/.config/ipython/profile_default) and allows to define a startup file, 
which can come in handy to add additional, django-project-specific functions and variables.

A sample IPython configuration is provided which adds the current development stage from settings.py 
to the IPython prompt.

I modified django_extensions/management/commands/shell_plus.py and django_extensions/management/shells.py.

To load a file on start of the Django shell, you have to tell Django shell the path to your startup file via
the environment variable PYTHONSTARTUP. The django-shell will automatically import all functions and variables from this 
startup script.


Getting Started
===============

The easiest way to figure out what Django Extensions are all about is to watch the `excellent screencast by Eric Holscher`__. In a couple minutes Eric walks you through a half a dozen command extensions.

Getting It
==========

You can get Django Extensions by using pip or easy_install::

 $ pip install django-extensions
 or
 $ easy_install django-extensions

If you want to install it from source, grab the git repository from GitHub and run setup.py::

 $ git clone git://github.com/django-extensions/django-extensions.git
 $ cd django-extensions
 $ python setup.py install

Using It
========

Generate (and view) a graphviz graph of app models::

 $ python manage.py graph_models -a -o myapp_models.png

Produce a tab-separated list of `(url_pattern, view_function, name)` tuples for a project::

 $ python manage.py show_urls

Getting Involved
================

Open Source projects can always use more help. Fixing a problem, documenting a feature, adding translation in your language. If you have some time to spare and like to help us, here are the places to do so:

- GitHub: https://github.com/django-extensions/django-extensions
- Mailing list: http://groups.google.com/group/django-extensions
- Translations: https://www.transifex.net/projects/p/django-extensions/

Documentation
=============

You can view documentation online at:

- http://packages.python.org/django-extensions/

Or you can look at the docs/ directory in the repository.

__ http://ericholscher.com/blog/2008/sep/12/screencast-django-command-extensions/

