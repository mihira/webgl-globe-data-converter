#!/usr/bin/env python

import geohash

PRECISION = 4

class Position:
    def __init__(self, lat, lon):
        self._geohash = geohash.encode(float(lat), float(lon), precision=PRECISION)
        pos = geohash.decode(self._geohash)
        self._lat = pos[0]
        self._lon = pos[1]
        self._hash = hash(self._geohash)

    def __repr__(self):
        lat_str = ('%f' % self._lat).rstrip('0').rstrip('.')
        lon_str = ('%f' % self._lon).rstrip('0').rstrip('.')
        return '%s,%s' % (lat_str, lon_str)

    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __hash__(self):
        return self._hash

class DataPoint:
    def __init__(self, pos, magnitude):
        self.pos = pos
        self.magnitude = magnitude

    def __repr__(self):
        return ('%s,%.6f' % (self.pos, self.magnitude)).rstrip('0').rstrip('.')