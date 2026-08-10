import numpy as np
import pandas as pd

from scipy.stats import norm


class NormalQQPlotStatistics:

    def __init__(self, columns, titles) -> None:
        self.columns = columns
        self.titles = titles

    def statistics(self):
        results = []

        for column in self.columns:

            values = column.dropna().to_numpy()

            values = np.sort(values)

            n = len(values)

            probabilities = (np.arange(1, n + 1) - 0.5) / n

            theoretical = norm.ppf(probabilities)

            slope, intercept = np.polyfit(
                theoretical,
                values,
                1,
            )

            predicted = intercept + slope * theoretical

            residuals = values - predicted

            correlation = np.corrcoef(
                theoretical,
                values,
            )[0, 1]

            results.append(
                {
                    "Correlation": correlation,
                    "R²": correlation**2,
                    "RMSE": np.sqrt(np.mean(residuals**2)),
                    "Max Absolute Deviation": np.max(np.abs(residuals)),
                    "Mean": values.mean(),
                    "Std": values.std(),
                }
            )

        return pd.DataFrame(
            {
                "Dataset": self.titles,
                **{key: [result[key] for result in results] for key in results[0]},
            }
        )
