import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import entropy


class EntropyPlot:

    def __init__(self, columns: list[pd.Series], titles: list[str]):
        self.columns = columns
        self.titles = titles

    def draw(self):

        if len(self.columns) != len(self.titles):
            raise ValueError("The number of columns must match the number of titles.")

        # ---------------------------------
        # Prepare data
        # ---------------------------------
        data = []

        for column, title in zip(self.columns, self.titles):

            values = column.dropna()

            probabilities = values.value_counts(normalize=True)

            entropy_value = entropy(probabilities, base=2)

            data.append({"Column": title, "Entropy": entropy_value})

        data = pd.DataFrame(data)

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, ax = plt.subplots(figsize=(14, 7), dpi=200)

        sns.barplot(data=data, x="Column", y="Entropy", color="steelblue", ax=ax)

        # ---------------------------------
        # Labels
        # ---------------------------------
        ax.set_title("Categorical Entropy Comparison", fontsize=12)

        ax.set_xlabel("Column", fontsize=10)

        ax.set_ylabel("Entropy (bits)", fontsize=10)

        # ---------------------------------
        # Grid
        # ---------------------------------
        ax.grid(True, axis="y", alpha=0.3)

        plt.xticks(rotation=90, fontsize=9)

        plt.yticks(fontsize=9)

        plt.tight_layout()

        plt.show()
