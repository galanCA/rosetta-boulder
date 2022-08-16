from multipledispatch import dispatch
import numpy as np
import pandas as pd
import sys
sys.path.insert(0,'./data')

class Rosetta:
    #@dispatch(None)
    def __init__(self) -> None:
        self.__extract_data('./data/cf-ff-data.csv')

    # Overload the constructor
    #@dispatch(None, str)
    #def __init__(self, file) -> None:
    #    self.__extract_data(file)

    def __extract_data(self, file) -> None:
        # Load the data
        data = pd.read_csv(file, delimiter=",")

        # Clean the data
        self.data = data.loc[:120,:"W' PER KG BODY MASS"]
