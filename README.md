# geo-twd
Conversion from x/y (TWD67 or TWD97) to lat/lon (WGS84).
The algorithms and parameters are based on [Universal Transverse Mercator coordinate
system](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system)
and [Taiwan datums](http://wiki.osgeo.org/wiki/Taiwan_datums).
The 2-degree transverse Mercator of TWD67 is transformed to TWD97 first then
transformed to latitude and longitude of WGS84.

# Installation
    $ pip install geotwd

# Sample codes
    >>> import geotwd
    >>> geotwd.to_wgs84(305787.783, 2784799.355)
    (25.170699408342106, 121.55344420780119)

    >>> geotwd.to_wgs84(304956.927, 2785003.304, twd67=True)
    (25.1707037238667, 121.55344252881788)

