import os
import pandas as pd

import matplotlib.pyplot as plt



class BalanceDataProcessor():
    """
    Load in the data from a csv file.
    Process it
    Return it in differnt formats so it can be displayed
    """

    def __init__(self, dataFilePath='data.csv', sizeInitalOrientationCalc= 10):

        self.balanceDataDF = self._getPandasDataFrameFromCSV(dataFilePath)
        self.sizeInitalOrientationCalc = sizeInitalOrientationCalc #The amount of rows the function _calcInitalOrientation will use to take the average of

        self.initalOrientationX, self.initalOrientationY = self._calcInitalOrientation()

        self._calcOrientationChange()


    def __str__(self):
        """
        Return the data loaded as a pandas DataFrame as a string
        """
        return self.balanceDataDF.to_string()


    def _getPandasDataFrameFromCSV(self, csvFilePath):
        """
        Read the data csv file as a Pandas DataFrame
        It expects that the collumns are in the order of 'timestamp', 'x orientation' and 'y orientation'
        And that the first row is the collumn names
        """

        if not os.path.isfile(csvFilePath):
            raise FileNotFoundError(f"Could not find {csvFilePath}")
    
        try:
            dataFrame = pd.read_csv(csvFilePath)
        except:
            raise Exception(f"Something went wrong trying to read {csvFilePath} as a Pandas dataframe")

        assert len(dataFrame.columns) == 4 , f"Expected the csv file to have 3 collumns in the order of 'timestamp', 'x orientation' and 'y orientation'. Found {len(dataFrame.columns)} collumns"

        dataFrame.columns = ['timestamp', 'x', 'y','z'] #Rename the collumns

        return dataFrame


    def _calcInitalOrientation(self):
        dataDF = self.balanceDataDF.head(self.sizeInitalOrientationCalc) #Get the first n amount of rows
        
        xMean = dataDF['x'].mean()
        yMean = dataDF['y'].mean()

        return xMean, yMean


    def _calcOrientationChange(self):
        self.balanceDataDF['xChange'] = self.balanceDataDF['x'] - self.initalOrientationX
        self.balanceDataDF['yChange'] = self.balanceDataDF['y'] - self.initalOrientationY


    #Some functions to display the data with Matplotlib
    def displayXChangeTime(self):
        plt.plot(self.balanceDataDF['timestamp'], self.balanceDataDF['xChange'])
        plt.show()


    def displayYChangeTime(self):
        plt.plot(self.balanceDataDF['timestamp'], self.balanceDataDF['yChange'])
        plt.show()


    def displayHeatmap(self):
        pass #TODO =