import csv
import sys
rawData = []
ScanReports = []
message = []
with open('run.csv') as file_obj:
   # Create reader object by passing the file
    # object to DictReader method
    run_csv = csv.DictReader(file_obj)

    #It read all the data from the 'data' row
    for row in run_csv:
        #print(row['data'])

        #read data as hex
        rawData.append(row['data'])

        #read data as integer
        #rawData.append(int(row['data'],0))

    #print(rawData)

    rawDataLen = len(rawData)
    print('length of rawData %d' % rawDataLen)
    HeaderofEvent = '0xA0'
    rawCounter = 0
    #for rawconter in range(0,rawDataLen,1):
    original_stdout = sys.stdout # Save a reference to the original standard output
    with open('Advertisement.txt', 'w') as g:
    #     sys.stdout = f # Change the standard output to the file we created.
        while (rawCounter <= rawDataLen):

            try:
                HeaderofEventIndex = rawData.index(HeaderofEvent)
            except:
                break
            #print(HeaderofEventIndex)
            EventLenght = int(rawData[HeaderofEventIndex+1],0)
            #print(EventLenght)

            try:
                for i in range(HeaderofEventIndex, HeaderofEventIndex + EventLenght + 4, 1):
                    message.append(rawData[i])
                    rawData[i] = 0
            except:
                break
            sys.stdout = g
            print (message)
            print("\n\r")
            sys.stdout = original_stdout

            ScanReports.append(message)
            message.clear()
            #for i in range(HeaderofEventIndex, HeaderofEventIndex + EventLenght + 4, 1):
            #    print("removing", rawData[i])
            #    del rawData[i]

            #print("raw Data left \n\r")
            #print(rawData)
            rawCounter = HeaderofEventIndex + EventLenght + 4
            #print("rawCounter = %d"% rawCounter)



with open('rawDataLeft.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(rawData)
    sys.stdout = original_stdout # Reset the standard output to its original value


    #print("Total raw Data left \n\r")
    #print(rawData)
    #print(ScanReports)

    ScanReportsLen = len(ScanReports)
    print('Total Number of correct Advertisements %d' % ScanReportsLen)

    #for Adv in range(ScanReportsLen):
    #    print(ScanReports[Adv])


    #print(rawData.index('0xA0'))
