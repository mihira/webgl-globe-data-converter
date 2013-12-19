WebGL Globe Data Converter
==========================

**WebGL Globe Data Converter** converts `CSV` data to [WebGL Globe](https://github.com/dataarts/webgl-globe) `JSON` format
----
WebGL Globe Data Converter uses [python-geohash module](https://code.google.com/p/python-geohash/) to create the groups using 4 as precision value.

## CSV file format
The input `CSV` file should contain 2 columns containing latitude and longitude of the points to be grouped.
Ex.:
```
+----------+-----------+
| latitude | longitude |
+----------+-----------+
|  45.5968 |   5.89587 |
|  47.6677 |   -2.7678 |
|   33.629 |   117.002 |
|  25.7823 |   -80.289 |
|  35.7765 |   140.315 |
| -37.8808 |   145.031 |
|  21.0186 |   105.848 |
|  5.97003 |   116.075 |
|  47.2138 |   -1.5569 |
| -23.5191 |  -46.6551 |
+----------+-----------+
```

## Output JSON format
The output file will contain `JSON` on the following format:
```javascript
[
["*",
[ latitude, longitude, magnitude, latitude, longitude, magnitude, ... ]
]
]
```

## Basic Usage
```shell
python converter.py -i INPUT_CSV [-o OUTPUT_JSON]
```
if no OUTPUT_JSON file is specified 'data.json' will be set by default

### Contributing
Pull requests, questions, suggestions are always welcome. Feel free to contribute! :)