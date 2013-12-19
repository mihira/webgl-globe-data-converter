#!/usr/bin/env python

from globe import Position, DataPoint
from collections import Counter
import csv
import os
import args

MAX_MAG = 0.3
DATA_GROUP_NAME = '*'
INPUT_PARAM = '-i'
OUTPUT_PARAM = '-o'
DEFAULT_OUT_FILE = 'data.json'

def get_magnitude(counter, top):
    return (MAX_MAG * counter) / top

def add_pos(pos_counter, pos):
        lat = pos[0]
        lon = pos[1]
        try:
            pos_counter.update((Position(lat, lon),))
        except Exception as exc:
            print 'Position', '(%s,%s)' % (lat, lon), 'failed to be processed:', exc

def read_positions_from_file(in_file):
    print 'Extracting points from', in_file
    points = []
    csv_file = open(in_file, 'rb')
    pos_reader = csv.reader(csv_file)
    pos_list = [(row[0], row[1]) for row in pos_reader]
    csv_file.close()
    pos_counter = Counter()
    print 'Grouping points...'
    map(lambda pos: add_pos(pos_counter, pos), pos_list)
    top_pair = pos_counter.most_common(1)
    top = 0
    if top_pair:
        top = top_pair[0][1]
        print 'Calculating group magnitudes...'
        points = [str(DataPoint(pos, get_magnitude(pos_counter[pos], top))) for pos in pos_counter]
    if points:
        print 'SUCCESS'
    else:
        print 'ERROR'
    print
    print len(points), 'points grouped from', len(pos_list), 'initial points'
    print 'Highest peak contains', top, 'points grouped.'
    print
    return '[\n["%s",\n[%s]\n]\n]' % (DATA_GROUP_NAME,(','.join(points)))

def save(data, out_file):
    print 'Saving data into', out_file
    dir = os.path.dirname(out_file)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    file = open(out_file, 'w')
    file.write(data)
    file.close()

def get_io_files():
    opts = args.grouped
    in_file = None
    out_file = DEFAULT_OUT_FILE
    if INPUT_PARAM in opts:
        input_opt = opts[INPUT_PARAM]
        if len(input_opt):
            in_file = input_opt[0]
    if OUTPUT_PARAM in opts:
        output_opt = opts[OUTPUT_PARAM]
        if len(output_opt):
            out_file = output_opt[0]
    return in_file, out_file

def convert(in_file, out_file):
    data = read_positions_from_file(in_file)
    save(data, out_file)
    print 'Done. :)'
    
def main():
    in_file, out_file = get_io_files()
    if in_file:
        convert(in_file, out_file)
    else:
        print 'Invalid parameters'
        print 'usage: python converter.py -i INPUT_CSV [-o OUTPUT_JSON]'

if __name__ == "__main__":
    main()

