# Stock-value-project-python

The structure of the project workflow is based on creating a user-friendly analytical tool for stock valuation over the next five years.

The project structure consists of modules, where all the logic takes place, and a main file that simply integrates the created functions into a whole.

The first created module is data_acquisition.py, which serves to:

    Retrieve valuation information from the Yahoo Finance API based on the stock ticker.
    Obtain benchmark data for comparison.

The second module is data_processing.py, which serves to:

    Process the acquired data from data_acquisition.py to create complete information and graphs.

The last module is pdf.py, which serves to:

    Compile all text structures, graphs, and photos into an attractive PDF file for easy manipulation of the results.

The main file only assembles all the logic together and also contains a list of modules and functions for their possible download if they are not yet installed.
