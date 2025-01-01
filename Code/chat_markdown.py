import pandas as pd 

from tne.TNE import TNE
from tabulate import tabulate


if __name__ == "__main__":
    if type(PROCESS_INPUT) is pd.DataFrame:
        result = tabulate(PROCESS_INPUT, headers="keys", tablefmt="pipe", showindex=False)
    elif type(PROCESS_INPUT) is str:
        result = PROCESS_INPUT 
    else:
        result = "None"