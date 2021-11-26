import pandas as pd
from rich_dataframe import prettify
#To add rich output to your application
from rich import print, style
from rich_tools import df_to_table
from rich.console import Console
console = Console()
from rich.syntax import Syntax

## Data frame formatting with rich
churn_df = pd.read_csv("Customer_Churn.csv")
##Convert DataFrame into a rich Table 
table = df_to_table(churn_df.head())
print("Dataframe to table",table)

## prettifying the table contents
prettify(churn_df.head(10))

##Console print with Rich
console.print("This is a", "sample!", style="bold blue")
console.print("[i]Where there is[i] a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].",style="bold red")

## Syntax highlighting with rich
code='''
"""function to check for columns with only two values"""
def check_valuecount_log():
    binary_cols = []
    for col in churn_df.columns:
        if churn_df[col].value_counts().shape[0] == 2:
         binary_cols.append(col)
'''    
syntax= Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)

## Logging with rich
def check_valuecount_log():
    binary_cols = []
    for col in churn_df.columns:
        if churn_df[col].value_counts().shape[0] == 2:
         binary_cols.append(col)
    
    console.log("The columns with two values are",binary_cols, log_locals=True)

check_valuecount_log()


