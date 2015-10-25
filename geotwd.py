#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


a = 6378.137  # km
f = 1/298.257222101  # GRS80
lon0 = 121
N0 = 0  # km
E0 = 250  # km
k0 = 0.9999
n = f / (2 - f)
A = a / (1 + n) * (1 + math.pow(n, 2) / 4 + math.pow(n, 4) / 64)
a1 = n / 2 - math.pow(n, 2) * 2 / 3 + math.pow(n, 3) * 5 / 16
a2 = math.pow(n, 2) * 13 / 48 - math.pow(n, 3) * 3 / 5
a3 = math.pow(n, 3) * 61 / 240
b1 = n / 2 - math.pow(n, 2) * 2 / 3 + math.pow(n, 3) * 37 / 96
b2 = math.pow(n, 2) / 48 + math.pow(n, 3) / 15
b3 = math.pow(n, 3) * 17 / 480
d1 = 2 * n - math.pow(n, 2) * 2 / 3 - 2 * math.pow(n, 3)
d2 = math.pow(n, 2) * 7 / 3 - math.pow(n, 3) * 8 / 5
d3 = math.pow(n, 3) * 56 / 15


def to_wgs84(x, y, twd67=False):
    '''
    The formula is based on
    "https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system"
    '''

    if twd67:
        x, y = twd67_to_twd97(x, y)

    x /= 1000.0  # m to km
    y /= 1000.0  # m to km

    xi = (y - N0) / (k0 * A)
    eta = (x - E0) / (k0 * A)
    xip = (xi -
           b1 * math.sin(2 * xi) * math.cosh(2 * eta) -
           b2 * math.sin(4 * xi) * math.cosh(4 * eta) -
           b3 * math.sin(6 * xi) * math.cosh(6 * eta))
    etap = (eta -
            b1 * math.cos(2 * xi) * math.sinh(2 * eta) -
            b2 * math.cos(4 * xi) * math.sinh(4 * eta) -
            b3 * math.cos(6 * xi) * math.sinh(6 * eta))
    chi = math.asin(math.sin(xip) / math.cosh(etap))
    lat = math.degrees(
            chi +
            d1 * math.sin(2 * chi) +
            d2 * math.sin(4 * chi) +
            d3 * math.sin(6 * chi))
    lon = lon0 + math.degrees(
            math.atan(math.sinh(etap) / math.cos(xip)))

    return (lat, lon)

def twd67_to_twd97(x67, y67):
    '''
    The formula is based on
    "http://wiki.osgeo.org/wiki/Taiwan_datums"
    The max errors is 2m
    '''

    A = 0.00001549
    B = 0.000006521
    x97 = x67 + 807.8 + A * x67 + B * y67
    y97 = y67 - 248.6 + A * y67 + B * x67

    return x97, y97

