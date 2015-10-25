#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from geotwd import to_wgs84, twd67_to_twd97


class TestGeoTwd(unittest.TestCase):
    '''
    Test data is from "http://wiki.osgeo.org/wiki/Taiwan_datums/Test_points"
    '''

    def test_N325(self):
        _lat = 25.18746219
        _lon = 121.57764439
        _x97 = 308219.274 
        _y97 = 2786666.378 
        _x67 = 307388.449
        _y67 = 2786870.260
        x97, y97 = twd67_to_twd97(_x67, _y67)
        self.assertLessEqual(abs(_x97 - x97), 2.0)
        self.assertLessEqual(abs(_y97 - y97), 2.0)
        lat97, lon97 = to_wgs84(_x97, _y97)
        self.assertLessEqual(abs(lat97 - _lat), 0.000001)
        self.assertLessEqual(abs(lon97 - _lon), 0.000001)
        lat67, lon67 = to_wgs84(_x67, _y67, twd67=True)
        self.assertLessEqual(abs(lat67 - _lat), 0.000005)
        self.assertLessEqual(abs(lon67 - _lon), 0.000005)

    def test_N440(self):
        _lat = 25.12775292
        _lon = 121.54657344
        _x97 = 305114.476
        _y97 = 2780039.462
        _x67 = 304283.621
        _y67 = 2780243.430
        x97, y97 = twd67_to_twd97(_x67, _y67)
        self.assertLessEqual(abs(_x97 - x97), 2.0)
        self.assertLessEqual(abs(_y97 - y97), 2.0)
        lat97, lon97 = to_wgs84(_x97, _y97)
        self.assertLessEqual(abs(lat97 - _lat), 0.000001)
        self.assertLessEqual(abs(lon97 - _lon), 0.000001)
        lat67, lon67 = to_wgs84(_x67, _y67, twd67=True)
        self.assertLessEqual(abs(lat67 - _lat), 0.000005)
        self.assertLessEqual(abs(lon67 - _lon), 0.000005)

    def test_N364(self):
        _lat = 25.08427325
        _lon = 121.52929869
        _x97 = 303391.398
        _y97 = 2775216.428
        _x67 = 302560.609
        _y67 = 2775420.286
        x97, y97 = twd67_to_twd97(_x67, _y67)
        self.assertLessEqual(abs(_x97 - x97), 2.0)
        self.assertLessEqual(abs(_y97 - y97), 2.0)
        lat97, lon97 = to_wgs84(_x97, _y97)
        self.assertLessEqual(abs(lat97 - _lat), 0.000001)
        self.assertLessEqual(abs(lon97 - _lon), 0.000001)
        lat67, lon67 = to_wgs84(_x67, _y67, twd67=True)
        self.assertLessEqual(abs(lat67 - _lat), 0.000005)
        self.assertLessEqual(abs(lon67 - _lon), 0.000005)

    def test_N043(self):
        _lat = 24.99253256
        _lon = 121.54865692
        _x97 = 305385.322
        _y97 = 2765062.499
        _x67 = 304554.669
        _y67 = 2765266.653
        x97, y97 = twd67_to_twd97(_x67, _y67)
        self.assertLessEqual(abs(_x97 - x97), 2.0)
        self.assertLessEqual(abs(_y97 - y97), 2.0)
        lat97, lon97 = to_wgs84(_x97, _y97)
        self.assertLessEqual(abs(lat97 - _lat), 0.000001)
        self.assertLessEqual(abs(lon97 - _lon), 0.000001)
        lat67, lon67 = to_wgs84(_x67, _y67, twd67=True)
        self.assertLessEqual(abs(lat67 - _lat), 0.000005)
        self.assertLessEqual(abs(lon67 - _lon), 0.000005)

    def test_N395(self):
        _lat = 24.96684283
        _lon = 121.57448200
        _x97 = 308004.393
        _y97 = 2762227.769
        _x67 = 307173.808
        _y67 = 2762431.824
        x97, y97 = twd67_to_twd97(_x67, _y67)
        self.assertLessEqual(abs(_x97 - x97), 2.0)
        self.assertLessEqual(abs(_y97 - y97), 2.0)
        lat97, lon97 = to_wgs84(_x97, _y97)
        self.assertLessEqual(abs(lat97 - _lat), 0.000001)
        self.assertLessEqual(abs(lon97 - _lon), 0.000001)
        lat67, lon67 = to_wgs84(_x67, _y67, twd67=True)
        self.assertLessEqual(abs(lat67 - _lat), 0.000005)
        self.assertLessEqual(abs(lon67 - _lon), 0.000005)

    def test_N001(self):
        _lat = 25.17069939
        _lon = 121.55344419
        _x97 = 305787.783
        _y97 = 2784799.355
        _x67 = 304956.927
        _y67 = 2785003.304
        x97, y97 = twd67_to_twd97(_x67, _y67)
        self.assertLessEqual(abs(_x97 - x97), 2.0)
        self.assertLessEqual(abs(_y97 - y97), 2.0)
        lat97, lon97 = to_wgs84(_x97, _y97)
        self.assertLessEqual(abs(lat97 - _lat), 0.000001)
        self.assertLessEqual(abs(lon97 - _lon), 0.000001)
        lat67, lon67 = to_wgs84(_x67, _y67, twd67=True)
        self.assertLessEqual(abs(lat67 - _lat), 0.000005)
        self.assertLessEqual(abs(lon67 - _lon), 0.000005)

    def test_N321(self):
        _lat = 25.14823836
        _lon = 121.54311114
        _x97 = 304756.205
        _y97 = 2782307.164
        _x67 = 303925.309
        _y67 = 2782511.181
        x97, y97 = twd67_to_twd97(_x67, _y67)
        self.assertLessEqual(abs(_x97 - x97), 2.0)
        self.assertLessEqual(abs(_y97 - y97), 2.0)
        lat97, lon97 = to_wgs84(_x97, _y97)
        self.assertLessEqual(abs(lat97 - _lat), 0.000001)
        self.assertLessEqual(abs(lon97 - _lon), 0.000001)
        lat67, lon67 = to_wgs84(_x67, _y67, twd67=True)
        self.assertLessEqual(abs(lat67 - _lat), 0.000005)
        self.assertLessEqual(abs(lon67 - _lon), 0.000005)

    def test_N002(self):
        _lat = 25.14428017
        _lon = 121.47764808
        _x97 = 298157.700
        _y97 = 2781843.744
        _x67 = 297326.997
        _y67 = 2782047.730
        x97, y97 = twd67_to_twd97(_x67, _y67)
        self.assertLessEqual(abs(_x97 - x97), 2.0)
        self.assertLessEqual(abs(_y97 - y97), 2.0)
        lat97, lon97 = to_wgs84(_x97, _y97)
        self.assertLessEqual(abs(lat97 - _lat), 0.000001)
        self.assertLessEqual(abs(lon97 - _lon), 0.000001)
        lat67, lon67 = to_wgs84(_x67, _y67, twd67=True)
        self.assertLessEqual(abs(lat67 - _lat), 0.000005)
        self.assertLessEqual(abs(lon67 - _lon), 0.000005)

    def test_N773(self):
        _lat = 25.10553611
        _lon = 121.50978825
        _x97 = 301414.420
        _y97 = 2777564.066
        _x67 = 300583.562
        _y67 = 2777768.034
        x97, y97 = twd67_to_twd97(_x67, _y67)
        self.assertLessEqual(abs(_x97 - x97), 2.0)
        self.assertLessEqual(abs(_y97 - y97), 2.0)
        lat97, lon97 = to_wgs84(_x97, _y97)
        self.assertLessEqual(abs(lat97 - _lat), 0.000001)
        self.assertLessEqual(abs(lon97 - _lon), 0.000001)
        lat67, lon67 = to_wgs84(_x67, _y67, twd67=True)
        self.assertLessEqual(abs(lat67 - _lat), 0.000005)
        self.assertLessEqual(abs(lon67 - _lon), 0.000005)

    def test_N385(self):
        _lat = 25.01920575
        _lon = 121.56541161
        _x97 = 307064.370
        _y97 = 2768023.913
        _x67 = 306233.656
        _y67 = 2768228.005
        x97, y97 = twd67_to_twd97(_x67, _y67)
        self.assertLessEqual(abs(_x97 - x97), 2.0)
        self.assertLessEqual(abs(_y97 - y97), 2.0)
        lat97, lon97 = to_wgs84(_x97, _y97)
        self.assertLessEqual(abs(lat97 - _lat), 0.000001)
        self.assertLessEqual(abs(lon97 - _lon), 0.000001)
        lat67, lon67 = to_wgs84(_x67, _y67, twd67=True)
        self.assertLessEqual(abs(lat67 - _lat), 0.000005)
        self.assertLessEqual(abs(lon67 - _lon), 0.000005)


if __name__ == '__main__':
    unittest.main()
