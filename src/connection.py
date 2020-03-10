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


class Connection:
    def __init__(self, series):
        self.input_circuit = fix_string(series.inputCircuit)
        self.output_circuit = fix_string(series.outputCircuit)
        self.transmitter = fix_string(series.transmitter)
        self.size = fix_size(series.size)
        if 'taxon' in series:
            self.taxon = fix_string(series.taxon)
        else:
            self.taxon = None
        self.functionality = fix_string(series.functionality)
        self.references = fix_string(series.references)
        self.implementations = fix_string(series.implementations)
    
    def connection_name(self):
        return f'{self.input_circuit}-{self.output_circuit}'
    
    def export_bif(self):
        elements = list()
        separator = '|'
        if self.input_circuit:
            elements.append(f'inputCircuit=Category:{self.input_circuit}')
        else:
            return
        if self.output_circuit:
            elements.append(f'outputCircuit=Category:{self.output_circuit}')
        if self.transmitter:
            elements.append(f'taxons={self.transmitter}')
        if self.size:
            elements.append(f'size={self.size}')
        if self.functionality:
            elements.append(f'functionalAnnotation={self.functionality}')
        if self.references:
            elements.append(f'references={self.references}')
        if self.implementations:
            elements.append(f'implementations={self.implementations}')
        return '{{Connection|' + separator.join(elements) + '}}'
