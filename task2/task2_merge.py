#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import csv
import datetime
import gzip
import json
import math
import os
import sys


def main(columns_file, output_files_dir):
    predicted_types = []
    for line in open(columns_file):
        # 2bmr-jdsv.DBA.txt.gz
        prefix, column, _, _ = line.strip().split('.')
        json_file = '%s/%s.%s.json' % (output_files_dir, prefix, column)
        with open(json_file) as fin_json:
            c = json.load(fin_json)
            c['column_name'] = '%s.%s' % (prefix, column)
            predicted_types.append(c)
    with open('task2.json', 'w') as fout:
        fout.write(json.dumps({'predicted_types': predicted_types}, indent=4))

    actual_types = []
    with open('columns_type.txt') as fin:
        for line in fin:
            types, column_file = line.rstrip().split('\t')
            prefix, column, _, _ = column_file.split('.')
            actual_types.append({
                'column_name': '%s.%s' % (prefix, column),
                'manual_labels': [{'semantic_type': t  if t != '' else 'other'} for t in types.split(',')]
                })
    with open('task2-manual-labels.json', 'w') as fout:
        fout.write(json.dumps({'actual_types': actual_types}, indent=4))


if __name__ == '__main__':
    columns_file = sys.argv[1]
    output_files_dir = sys.argv[2]
    main(columns_file, output_files_dir)
