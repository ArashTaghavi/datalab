import pandas as pd


class NormalBoxPlotStatistics:
    def __init__(self, columns, titles) -> None:
        self.columns = columns
        self.titles = titles

    def statistics(self):
        return pd.DataFrame(
            {
                "Dataset": self.titles,
                "Min": [column.min() for column in self.columns],
                "Q1": [column.quantile(0.25) for column in self.columns],
                "Median": [column.median() for column in self.columns],
                "Mean": [column.mean() for column in self.columns],
                "Q3": [column.quantile(0.75) for column in self.columns],
                "Max": [column.max() for column in self.columns],
                "IQR": [
                    column.quantile(0.75) - column.quantile(0.25)
                    for column in self.columns
                ],
                "Box Width": [
                    column.quantile(0.75) - column.quantile(0.25)
                    for column in self.columns
                ],
            }
        )
