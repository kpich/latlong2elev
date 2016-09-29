#!/usr/bin/env python

import argparse
import csv
import json
import requests
import time
import xml.etree.ElementTree as ET

BASE_URL = "https://maps.googleapis.com/maps/api/elevation/json"

def main():
  key = open(FLAGS_api_key, 'r').read().strip()
  csv_outf = open(FLAGS_out_csv, 'wb')
  csv_writer = csv.writer(csv_outf)
  with open(FLAGS_in_csv, 'r') as inf:
    reader = csv.reader(inf)
    for i,row in enumerate(reader):
      if i % 10 == 0:
        print 'processing row %d...' % i
        time.sleep(1)
      if i < 45:
        continue
      # longitude is before latitude in row.
      params = {"key": key, "locations": "%s,%s" % (row[1], row[0])}
      r = requests.get(BASE_URL, params=params)
      response_json = json.loads(r.text)
      print response_json
      csv_writer.writerow(row[:2] +
                          [str(response_json['results'][0]['elevation'])] +
                          [str(response_json['results'][0]['resolution'])] +
                          row[2:])
  csv_outf.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--api_key', type=str, required=True,
                      help="file with API key on single line")
  parser.add_argument('--in_csv', type=str, required=True,
                      help="input CSV file with points to query.")
  parser.add_argument('--out_csv', type=str, required=True,
                      help="place to stream csv.")
  args = parser.parse_args()
  for k,v in vars(args).items():
    globals()['FLAGS_%s' % k] = v
  main()
