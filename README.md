## latlong2elev: Get elevations from lat/long values using the google maps API.

This requires the `requests` library, which you can get by calling
```
pip install requests
```
on the command line.

An example invocation can be found in `call_get_elevations.sh`. Put a google
maps API key in a single line in the file specified by `--api_key`.

The input CSV should have longitude in the first column and latitude in the
second one. This script will produce an output csv with the elevation in the
third column and the resolution in the fourth (see
[here](https://developers.google.com/maps/documentation/elevation/intro#PointElevation)
for more info on what these mean).
