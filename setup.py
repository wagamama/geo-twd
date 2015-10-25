from setuptools import setup


setup(name = 'geotwd',
      version = '0.1',
      description = 'Conversion from x/y (TWD67 or TWD97) to lat/lon (WGS84)',
      keywords = 'twd67 twd97 wgs84 transform',
      url = 'https://github.com/wagamama/geo-twd',
      author = 'Yi-Lung (Bruce) Tsai',
      author_email = 'wagamama.tsai@gmail.com',
      license = 'MIT',
      packages = ['geotwd'],
      test_suite = 'nose.collector',
      tests_require = ['nose']
)
