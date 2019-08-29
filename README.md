# plotCSV.py

Ed Bisdee
2019-08-29

This can be used as a module or a standalone script to plot any csv file using
the python matplot lib library. It's faster and can take bigger files than Excel
so can be very useful if you have a lot of data you want to plot in a hurry, or if you need to automate plotting.

## Prerequisites

You will need the Matplotlib and Numpy libraries. install them with

    pip install matplotlib
    pip install numpy

## Instructions

### Module

    import plotCSV
    plotCSV.plot_csv(csv_in, b_header, b_first_col_time)

csv_in: path of csv file
b_header: True = show the first line as a legend
b_first_col_time: True = the first column is the x-axis of the plot
False = plot the first column as a line, and plot the data sequentially

### Command line

    python plotCSV.py --file "C:\docs\kittehs.csv" --no-header --skip-first-col

## TODO

+ add a number of lines to ignore in case of a big header or watermark at the top of the csv
+ ignore the x lines of a file header 0 to x number of lines
+ allow import of all cols by numpy on line 48
+ check format of input string, and if not correct iso format, convert to iso date format
+ make use of and naming of first column boolean consistent

### DONE

+ add header of author date and instructions
+ if the first column is a time column, use it as the x axis
else plot it as a series

+ modfiy first column behaviour so if you plot it, the script plots all number sequentially,
if not, it assumes the first column is a time string, and uses that as the x axis values

+ 2 time formats:
    + ISO8601 YYYY-MM-DDTHH:MM:SS.SSSSSS '2019-08-21T14:25:58.005146' as supplied by datetime.datetime.now().isoformat()
    + seconds (relative or epoch, who cares?) - matplotlib takes these dates in no probs

## Known Issues

When plotting data with gaps (in particular a single series plot), the script will only plot x-axis values which have a corresponding y axis value. This may mean that the x-axis is not a consistent scale.