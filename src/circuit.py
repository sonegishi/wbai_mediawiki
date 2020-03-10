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
#     display_name: Python 3
#     language: python
#     name: python3
# ---

#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from helper import fix_string, fix_size


class Circuit:
    def __init__(self, series):
        self.names = fix_string(series.names)
        self.has_parts = fix_string(series.hasParts, replace=True)
        if 'taxon' in series:
            self.taxon = fix_string(series.taxon)
        else:
            self.taxon = None
        self.functionality = fix_string(series.functionality)
        self.references = fix_string(series.references)
        self.implementations = fix_string(series.implementations)
        self.equivalent_to = fix_string(series.equivalentTo)
        self.uniform = series.uniform
        self.size = fix_size(series.size)
        self.transmitter = series.transmitter

    def export_bif(self):
        elements = list()
        separator = '|'
        if self.names:
            elements.append(f'names={self.names}@en')
        else:
            return

        if self.has_parts:
            elements.append(f'hasParts={self.has_parts}')
        if self.taxon:
            elements.append(f'taxons={self.taxon}')
        if self.functionality:
            elements.append(f'functionalAnnotation={self.functionality}')
        if self.references:
            elements.append(f'references={self.references}')
        if self.implementations:
            elements.append(f'implementations={self.implementations}')
        if self.equivalent_to:
            elements.append(f'equivalentTo={self.equivalent_to}')
        if self.size:
            elements.append(f'size={self.size}')
        if self.transmitter:
            elements.append(f'transmitter={self.transmitter}')

        if self.uniform:
            return f'{{UniformCircuit|{separator.join(elements)}}}'
        elif not self.uniform:
            return f'{{Circuit|{separator.join(elements)}}}'
