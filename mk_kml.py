#!/usr/bin python

import numpy as np
import os
import sys
import simplekml

#=========================================================================================
if len(sys.argv) < 3:
    print "      "
    print "USAGE: python mk_kml.py stations_list_file ouput_kml_file"
    print "      "
    sys.exit()
#=========================================================================================

sta_list = np.loadtxt(sys.argv[1],dtype=[('staname','S14'),('stalat','S5'),
                                 ('stalon','S6')], skiprows=0, usecols=[0,1,2])
kml = simplekml.Kml()

for i in range(len(sta_list)):
    sta =  sta_list[i][0]
    lat =  sta_list[i][1]
    lon =  sta_list[i][2]
    pnt = kml.newpoint(name=sta, coords=[(lon,lat)])
    pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/firedept.png'
#  http://kml4earth.appspot.com/icons.html
kml.save(sys.argv[2])
