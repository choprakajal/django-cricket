# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cricket.views.exceptions import AbstractFunctionError


def abstract_function(func):
    def func_wrapper(*args, **kwargs):
        raise AbstractFunctionError
