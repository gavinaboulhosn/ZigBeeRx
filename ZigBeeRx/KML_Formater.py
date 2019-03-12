import os
name = 'data.kml'


def kml_name(newname):
    global name
    name = newname + '.kml'
    return 0


def kml_gen(i, lon, lat, alt=0, scale=1, icon='1'):


    if float(lon) >0:
        lon = str(float(lon)*-1)

    if icon == '1':
        icon = 'default.png'  # sets icon to default color when no path for a color graded icon is available.

    if os.path.isfile(name) == 0:  # Creates kml data file and adds starting code if it does not exist.
        new_kml = open(name, "w+")
        new_kml.write('<?xml version="1.0" encoding="UTF-8"?>\r')
        new_kml.write('<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">\r')
        new_kml.write('    <Document id="1">\r')
        new_kml.close()
        print('new file "%s" has been made' % name)
    else:
        with open(name, 'rb+') as filehandle:  # removes last 2 lines of kml headers so new data points can be added.
            filehandle.seek(-22, os.SEEK_END)
            filehandle.truncate()

    kml = open(name, "a+")

    kml.write('       <Style id="%d">\r' % (i + 1))
    kml.write('            <IconStyle id="10">\r')
    kml.write('                <colorMode>normal</colorMode>\r')
    kml.write('                <scale>%d</scale>\r' % scale)
    kml.write('                <heading>0</heading>\r')
    kml.write('                <Icon id="%d">\r' % (i + 2))
    kml.write('                    <href>%s</href>\r' % icon)
    kml.write('                </Icon>\r')
    kml.write('            </IconStyle>\r')
    kml.write('        </Style>\r')

    kml.write('		<Placemark id="18">\r')
    kml.write('            <description>none</description>\r')
    kml.write('            <styleUrl>#%d</styleUrl>\r' % (i + 1))
    kml.write('            <Point id="17">\r')
    kml.write('                <coordinates>%s,%s,%s</coordinates>\r' % (lon, lat, alt))
    kml.write('                <altitudeMode>relativeToGround</altitudeMode>\r')
    kml.write('            </Point>\r')
    kml.write('        </Placemark>\r')
    kml.write('    </Document>\r')
    kml.write('</kml>\r')

    kml.close()

    print('point # %d at %s , %s , %s has been added' % (i,lon,lat,alt))

    return 0


if __name__ == '__main__':
    pass