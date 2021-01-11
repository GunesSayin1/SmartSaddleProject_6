import os, math
import pandas as pd

import matplotlib.pyplot as plt



class BalanceDataProcessor():
    """
    Load in the data from a csv file.
    Process it
    Return it in differnt formats so it can be displayed
    """

    def __init__(self, sizeInitalOrientationCalc = 10, badPostureThreshold = 15):
        self.readText()
        self.balanceDataDF = self._get_pandas_dataFframe_from_csv()
        self.sizeInitalOrientationCalc = sizeInitalOrientationCalc # The amount of rows the function _calcInitalOrientation will use to take the average
        self.badPostureThreshold = badPostureThreshold

        self.initalOrientationX, self.initalOrientationY = self._calc_inita_orientation()

        self._calc_crientation_change()
        self.score = self._calc_score()


    def __str__(self):
        """
        Return the data loaded as a pandas DataFrame as a string
        """
        return self.balanceDataDF.to_string()


    def _get_pandas_dataFframe_from_csv(self):
        """
        Read the data csv file as a Pandas DataFrame
        It expects that the collumns are in the order of 'timestamp', 'x orientation' and 'y orientation'
        And that the first row is the collumn names
        """
        csvnew = self.readText()
        if not os.path.isfile(csvnew):
            raise FileNotFoundError(f"Could not find {csvnew}")
    
        try:

            dataFrame = pd.read_csv(csvnew)
        except:
            raise Exception(f"Something went wrong trying to read {csvnew} as a Pandas dataframe")

        assert len(dataFrame.columns) == 3 , f"Expected the csv file to have 3 collumns in the order of 'timestamp', 'x orientation' and 'y orientation'. Found {len(dataFrame.columns)} collumns"

        dataFrame.columns = ['timestamp', 'x', 'y'] # Rename the collumns

        return dataFrame


    def _calc_inita_orientation(self):
        dataDF = self.balanceDataDF.head(self.sizeInitalOrientationCalc) # Get the first n amount of rows
        
        xMean = dataDF['x'].mean()
        yMean = dataDF['y'].mean()

        return xMean, yMean


    def _calc_crientation_change(self):
        self.balanceDataDF['xChange'] = self.balanceDataDF['x'] - self.initalOrientationX
        self.balanceDataDF['yChange'] = self.balanceDataDF['y'] - self.initalOrientationY


    def get_balance_data(self):
        return self.balanceDataDF

    def get_score(self):
        return self.score


    def _calc_score(self):
        score = 0

        for index, row in self.balanceDataDF.iterrows():
            
            change = math.sqrt((row['xChange']**2) + (row['yChange']**2))

            if change > self.badPostureThreshold:
                score -= 1
            else:
                score += 1

        return score


    # Some functions to display the data with Matplotlib
    def displayXChangeTime(self):
        plt.plot(self.balanceDataDF['timestamp'], self.balanceDataDF['xChange'])
        plt.show()


    def displayYChangeTime(self):
        plt.plot(self.balanceDataDF['timestamp'], self.balanceDataDF['yChange'])
        plt.show()

    def readText(self):
        with open("copy.txt", "r") as file:
            csvnew = file.read()
            return csvnew
            file.close

