#!/bin/sh

# created by smallkif 20171113 
# ARFCN Calculator

import sys

def CalculateARFCN():
    #Samsung (Android): *#*#197328640#*#* and *#0011#
    #Sony (Android): *#*#*386#*#* and *#*#*585*0000#*#* 
    #iPhone (all): *3001#12345#*
    #HTC (Android): *#*#7262626#*#*

    arg= ''

    if(len(sys.argv) > 1 ):
        arg = sys.argv[1]
    else:
        arg = raw_input("Enter Channel No.")

    channel_num = int(arg)

    #GSM450  259-293
    # UL = 450.6 + 0.2*(N-259)
    # DL = UL + 10 
    if( channel_num >= 259 and channel_num <= 293 ):
        ULFreq = 450.6 + 0.2 * (channel_num-259)
        DLFreq = ULFreq + 10
        print("GSM450 UL = {0}  DL = {1}".format(ULFreq,DLFreq))
    
    #GSM480 306-340
    # UL = 479+0.2*(N-306)
    # DL = UL + 10 
    if( channel_num >= 306 and channel_num <= 340 ):
            ULFreq = 479 + 0.2 * (channel_num-306)
            DLFreq = ULFreq + 10
            print("GSM480 UL = {0}  DL = {1}".format(ULFreq,DLFreq))

    #GSM750 438-511
    # UL = 747.2 + 0.2*(N-438)
    # DL = UL + 30 
    if( channel_num >= 438 and channel_num <= 511 ):
            ULFreq = 747.2 + 0.2 * (channel_num - 438)
            DLFreq = ULFreq + 30 
            print("GSM750 UL = {0}  DL = {1}".format(ULFreq,DLFreq))
    
    #GSM850 128-251
    # UL = 	824.2+0.2*(N-128)
    # DL = UL + 45
    if( channel_num >= 128 and channel_num <= 251 ):
            ULFreq =  	824.2+0.2*(channel_num-128)
            DLFreq = ULFreq + 45
            print("GSM850 UL = {0}  DL = {1}".format(ULFreq,DLFreq))

    #P-GSM 1 - 124
    # UL = 890+0.2*N
    # DL = UL + 45
    if( channel_num >= 1 and channel_num <= 124 ):
            ULFreq = 890 + 0.2 * channel_num
            DLFreq = ULFreq + 45
            print("P-GSM UL = {0}  DL = {1}".format(ULFreq,DLFreq))

    #E-GSM 975 - 1023
    # UL = 890+0.2*(N-1024)
    # DL = UL + 45
    if( channel_num >= 975 and channel_num <= 1023 ):
            ULFreq = 890 + 0.2 * (channel_num - 1024)
            DLFreq = ULFreq + 45
            print("E-GSM UL = {0}  DL = {1}".format(ULFreq, DLFreq))

    #GSM-R 955-1023
    # UL = 890+0.2*(N-1024)
    # DL = UL + 45
    if( channel_num >= 955 and channel_num <= 1023 ):
            ULFreq = 890 + 0.2 * ( channel_num - 1024 )
            DLFreq = ULFreq + 45
            print("GSM-R UL = {0}  DL = {1}".format(ULFreq, DLFreq))
    
    #DCS1800 512 - 885
    # UL = 	1710.2+0.2*(N-512)
    # DL = UL + 95
    if( channel_num >= 512 and channel_num <= 885 ):
            ULFreq =  1710.2 + 0.2 * ( channel_num - 512 )
            DLFreq = ULFreq + 95
            print("DCS1800 UL = {0}  DL = {1}".format(ULFreq, DLFreq))

    #PCS1900 512 - 810
    # UL = 1850.2 + 0.2*(N-512)
    # DL = UL + 80
    if( channel_num >= 512 and channel_num <= 810 ):
            ULFreq = 1850.2 + 0.2 * ( channel_num - 512 )
            DLFreq = ULFreq + 80
            print("PCS1900 UL = {0}  DL = {1}".format( ULFreq, DLFreq))

if __name__ == "__main__":
    
    print("Samsung (Android): *#*#197328640#*#* and *#0011#")
    print("Sony (Android): *#*#*386#*#* and *#*#*585*0000#*#*")
    print("iPhone (all): *3001#12345#*")
    print("HTC (Android): *#*#7262626#*#*")
    
    CalculateARFCN()