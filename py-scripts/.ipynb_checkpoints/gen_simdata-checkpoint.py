#!/usr/bin/env python
# coding: utf-8

import os
from os.path import join
import json
import pandas as pd
import random
import re

# Script for generating simulated data for sunburst diagrams

# colnames
colnames = [
    'ID - personer',
    'PART_ACAD_norm',
    'PART_NON_norm',
    'PART_INT_norm',
    'PART_ORG_norm',
    'PART_TEACH_norm',
    'PART_QUAL_norm',
    'PART_MEDIA_norm',
    'PROD_MEDIA_norm',
    'PROD_AEST_norm',
    'PROD_ACAD_norm',
    'PROD_POLI_norm',
    'PROD_COMM_norm',
    'INFLOW_norm']

# n simulated obs
n = 50

# simulate data
data = {}
for col in colnames:
    if col == 'ID - personer':
        data[col] = list(range(n))
    else:
        data[col] = [i / 100 for i in random.sample(range(300), n)]

df = pd.DataFrame(data)

df.to_excel(join('..', 'data', 'simdata_sunburst.xlsx'), index = False)