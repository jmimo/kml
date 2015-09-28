from collections import namedtuple

BRecord = namedtuple('BRecord', ['time', 'latitude', 'longitude', 'validity', 'alti_gps', 'alti_baro'])
Igc = namedtuple('Igc', ['date', 'records'])

class Parser:

    def __init__(self):
        pass

    def parse(self, file):
        b_records = list()
        for line in open(file, 'r'):
            if line.startswith('HFDTE'):
                date = self.date(line)
            elif line.startswith('B'):
                b_records.append(self.record(line))
        return Igc(date, b_records)


    def date(self, line):
        return line[5:]


    def record(self, line):
        return BRecord(line[1:7], self.convert_coordinate(line[7:15]), self.convert_coordinate(line[15:24]), line[24:25], line[25:30], line[30:35])

    def convert_coordinate(self, coordinate):
        if len(coordinate) == 8:
            latitude = float(coordinate[0:2]) + ((float(coordinate[2:4]) + (float(coordinate[4:7]) / 1000.0)) / 60.0)
            if coordinate[7:8] == 'S':
                latitude *= -1
            return latitude
        elif len(coordinate) == 9:
            longitude = float(coordinate[0:3]) + ((float(coordinate[3:5]) + (float(coordinate[5:8]) / 1000.0)) / 60.0)
            if coordinate[8:9] == 'W':
                longitude *= -1
            return longitude
        else:
            raise Exception('invalid coordinate value in: {}'.format(coordinate))
