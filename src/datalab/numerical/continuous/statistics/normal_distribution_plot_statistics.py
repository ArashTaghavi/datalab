import pandas as pd


class NormalDistributionPlotStatistics:
    def __init__(self, columns, titles) -> None:
        self.columns = columns
        self.titles = titles

    def statistics(self):
        return pd.DataFrame(
            {
                "Dataset": self.titles,
                "Min": [column.min() for column in self.columns],
                "Max": [column.max() for column in self.columns],
                "Mean": [column.mean() for column in self.columns],
                "Std": [column.std() for column in self.columns],
                "Percentage Within ±5 of Mean": [
                    (
                        (
                            (column >= column.mean() - 5)
                            & (column <= column.mean() + 5)
                        ).mean()
                        * 100
                    )
                    for column in self.columns
                ],
            }
        )
