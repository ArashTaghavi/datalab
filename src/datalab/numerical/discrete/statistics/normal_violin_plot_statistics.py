import numpy as np
import pandas as pd


class DiscreteStatistics:

    def __init__(self, columns, titles) -> None:
        self.columns = columns
        self.titles = titles

    def statistics(self):
        results = []

        for column, title in zip(self.columns, self.titles):

            values = column.dropna().to_numpy()

            unique_values, frequencies = np.unique(values, return_counts=True)

            max_frequency_index = np.argmax(frequencies)

            results.append(
                {
                    "Dataset": title,
                    # Range
                    "Min": values.min(),
                    "Max": values.max(),
                    "Range": values.max() - values.min(),
                    # Unique Values
                    "Unique Values": len(unique_values),
                    # Central Tendency
                    "Mean": values.mean(),
                    "Median": np.median(values),
                    "Std": values.std(),
                    # Frequency
                    "Most Frequent Value": unique_values[max_frequency_index],
                    "Max Frequency": frequencies[max_frequency_index],
                    # Frequency Concentration
                    "Most Frequent %": (
                        frequencies[max_frequency_index] / len(values) * 100
                    ),
                }
            )

        return pd.DataFrame(results)
