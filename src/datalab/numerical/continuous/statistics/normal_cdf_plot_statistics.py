import numpy as np
import pandas as pd


class NormalCDFPlotStatistics:

    def __init__(self, columns, titles) -> None:
        self.columns = columns
        self.titles = titles

    def statistics(self):
        results = []

        for column, title in zip(self.columns, self.titles):

            values = column.dropna().to_numpy()

            results.append(
                {
                    "Dataset": title,
                    # Spread
                    "Min": values.min(),
                    "Max": values.max(),
                    "Range": values.max() - values.min(),
                    # Percentiles
                    "P10": np.quantile(values, 0.10),
                    "Q1": np.quantile(values, 0.25),
                    "Median": np.quantile(values, 0.50),
                    "Q3": np.quantile(values, 0.75),
                    "P90": np.quantile(values, 0.90),
                    # Central Range
                    "P10-P90 Range": (
                        np.quantile(values, 0.90) - np.quantile(values, 0.10)
                    ),
                }
            )

        return pd.DataFrame(results)
