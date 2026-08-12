import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde


class NormalViolinPlotStatistics:

    def __init__(self, columns, titles) -> None:
        self.columns = columns
        self.titles = titles

    def statistics(self):
        results = []

        for column, title in zip(self.columns, self.titles):

            values = column.dropna().to_numpy()

            kde = gaussian_kde(values)

            x = np.linspace(values.min(), values.max(), 1000)

            density = kde(x)

            peak_index = np.argmax(density)

            results.append(
                {
                    "Dataset": title,
                    # Spread
                    "Min": values.min(),
                    "Max": values.max(),
                    "Range": values.max() - values.min(),
                    "Std": values.std(),
                    # Central spread
                    "Q1": np.quantile(values, 0.25),
                    "Q3": np.quantile(values, 0.75),
                    "IQR": (np.quantile(values, 0.75) - np.quantile(values, 0.25)),
                    # Shape / Density
                    "Peak Density Value": x[peak_index],
                    "Peak Density": density[peak_index],
                }
            )

        return pd.DataFrame(results)
