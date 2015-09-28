from igc import Parser
from kml import Kml

def main():
    parser = Parser()
    igc = parser.parse('2015-08-13-Lai_Alv.igc')

    kml = Kml()
    for record in igc.records:
        kml.add_point(igc.date, record)
    kml.create('test.kml')


if __name__ == '__main__':
    main()
