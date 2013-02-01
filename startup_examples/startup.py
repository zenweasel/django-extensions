#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is an example startup file to be loaded by django-extensions shell_plus
# in ipython mode.
# All variables and methods defined in this file are forwarded to the ipython shell.

import logging


# Toggle SQL Query logging
def _toggle_logging(self, *args, **kwargs):
    l = logging.getLogger('django.db.backends')
    if l.level == logging.DEBUG:
        print "Disabling DB logging"
        l.setLevel(logging.ERROR)
    else:
        print "Enabling DB logging"
        l.setLevel(logging.DEBUG)


# Patch django so that it allows to do further DB actions after errors
def patch_django_db():
    from django import db
    from django.db.backends.util import CursorDebugWrapper
    old_execute = CursorDebugWrapper.execute
    old_execute_many = CursorDebugWrapper.executemany

    def execute_wrapper(*args, **kwargs):
        try:
            old_execute(*args, **kwargs)
        except Exception, ex:
            logger.error("Database error:\n%s" % ex)
            db.close_connection

    def excecute_many_wrapper(*args, **kwargs):
        try:
            old_execute_many(*args, **kwargs)
        except Exception, ex:
            logger.error("Database error:\n%s" % ex)
            db.close_connection

    CursorDebugWrapper.execute = execute_wrapper
    CursorDebugWrapper.executemany = excecute_many_wrapper
patch_django_db()

# Can be used to show the current log level inside the prompt
# (see ipython sample config how to use it)
class LoggingInfo(object):
    def __str__(self):
        import logging
        if logging.getLogger("django.db.backends").level == logging.DEBUG:
            return "SQL LOG MODE "
        else:
            return ""
loginfo = LoggingInfo()
