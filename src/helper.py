# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.0
#   kernelspec:
#     display_name: 'Python 3.7.6 64-bit (''mediawiki'': venv)'
#     language: python
#     name: python37664bitmediawikivenv96927934f3b0450ca4e08d63b107526b
# ---

# +
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# -

def fix_string(val, replace=False):
    if isinstance(val, float):
        return None
    if replace:
        return str(val).replace(' ', '')
    return str(val)


def fix_size(val):
    try:
        int(val)
        return int(val)
    except ValueError:
        return ''
