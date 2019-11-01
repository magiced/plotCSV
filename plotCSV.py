import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
import sys
import argparse
import time
import csv
import ntpath

"""
# plotCSV.py

Ed Bisdee
2019-08-29

This can be used as a module or a standalone script to plot any csv file using
the python matplot lib library. It's faster and can take bigger files than Excel
so can be very useful if you have a lot of data you wint to plot in a hurry.

## Instructions
command line:
python plotCSV.py filename 2 3
    # Parameters
    # 1: filename,
    # 2: True/False, Is the first row a header? Default:  True
    # 3: True/False, Should the first column be used as the x axis? Default: True

## TODO

add header of author date and instructions

add a number of lines to ignore in case of a big header or watermark at the top of the csv

ignore the x lines of a file header 0 to x number of lines

allow import of all cols by numpy on line 48

check format of input string, and if not correct iso format, convert to iso date format

make use of and naming of first column boolean consistent

### DONE

if the first column is a time column, use it as the x axis
else plot it as a series

modfiy first column behaviour so if you plot it, the script plots all number sequentially,
if not, it assumes the first column is a time string, and uses that as the x axis values

2 time formats:
+ ISO8601 YYYY-MM-DDTHH:MM:SS.SSSSSS '2019-08-21T14:25:58.005146' as supplied by datetime.datetime.now().isoformat()
+ seconds (relative or epoch, who cares?)
matplotlib takes these dates in no probs

## Known Issues
When plotting data with gaps (in particular a single series plot), the script 
will only plot x-axis values which have a corresponding y axis value. This may 
mean that the x-axis is not a consistent scale.

"""

def plot_csv(csv_in, b_header=True, b_first_col_time = True):
    data = []
    timestamps = []
    #use numpy genfrom text to open csv file
    #use headers as series titles
    #mask for gappy data e.g faultMask = np.isfinite(fault)
    #plot the graph with the filename as the title and the headers as labels

    if b_first_col_time:
        # import data
        csvNP = np.genfromtxt(csv_in, delimiter=',')

        # re-import csv first column only as a numpy string array to allow the gapmask
        # to be used on the timestamp column
        csvSTR = np.genfromtxt(csv_in, delimiter=',', dtype=str, usecols=(0))
        # for lines in csvData:
        #     timestamps.append(lines[0])
        timestamps = csvSTR
    else:
        csvNP = np.genfromtxt(csv_in, delimiter=',')


    csvFile = open(csv_in)
    csvReader = csv.reader(csvFile)
    csvData = list(csvReader)

    #If there is a file header Open and read the first line of the csv to label the series
    if b_header:
        readFile = open(csv_in)
        headers = readFile.readline().strip().split(',')
        readFile.close()
    else:
        headers = 0

    fig, ax1 = plt.subplots()

    # If the first column is a timestamp or a date or other useless data, ignore it
    if b_first_col_time:
        print("Using the first column as the x axis...")
        for column in range(1,len(csvNP[0])):
            print("col {} of {}".format(column,len(csvNP[0])))
            data = csvNP[:,column]
            gapMask = np.isfinite(data)

            if b_header:
                # ax1.plot(timestamps,data, label=headers[column])
                ax1.plot(timestamps[gapMask],data[gapMask], label=headers[column])
            else:
                ax1.plot(timestamps[gapMask],data[gapMask])
                # ax1.plot(timestamps,data)
    else:
        print("Plotting all the columns...")
        #this generates an x value so that gappy data will appear in the correct place
        x = np.arange(0,csvNP.shape[0],1)

        for column in range(len(csvNP[0])):
            data = csvNP[:,column]
            gapMask= np.isfinite(data)
            
            if b_header:
                ax1.plot(x[gapMask],data[gapMask], label=headers[column])
            else:
                ax1.plot(x[gapMask],data[gapMask])

    print("Show Header and Legend...")
    if b_header:
        #create legend
        ax1.legend()

    # https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format
    plt.title(ntpath.basename(csv_in))
    
    plt.setp(ax1.get_xticklabels(), rotation=90, ha='right') #turns x axis labels 90 degrees round
    # plt.gcf().autofmt_xdate()

    print("Show Plot...")
    plt.show()
    # outpath = csv_in[:-4] + '.svg'
    # fig.savefig(outpath)
    # print("File saved as " + outpath)
    print("Finished")

if __name__ == '__main__':
        plot_csv(sys.argv[1])
        # plot_csv("C:\\_CODE\\pythonPlotting\\rawadctest2.csv")