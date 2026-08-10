import pandas as pd


class NormalMeanStdStatistics:

    def __init__(self, columns, titles) -> None:
        self.columns = columns
        self.titles = titles

    def statistics(self):
        return pd.DataFrame(
            {
                "Dataset": self.titles,
                "Mean": [column.dropna().mean() for column in self.columns],
                "Std": [column.dropna().std() for column in self.columns],
                "Mean - Std": [
                    column.dropna().mean() - column.dropna().std()
                    for column in self.columns
                ],
                "Mean + Std": [
                    column.dropna().mean() + column.dropna().std()
                    for column in self.columns
                ],
            }
        )
