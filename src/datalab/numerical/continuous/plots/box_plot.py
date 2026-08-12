import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class BoxPlot:

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

            for value in values:
                data.append({"Value": value, "Distribution": title})

        data = pd.DataFrame(data)

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, ax = plt.subplots(figsize=(14, 7), dpi=200)

        sns.boxplot(data=data, x="Distribution", y="Value", color="steelblue", ax=ax)

        # ---------------------------------
        # Labels
        # ---------------------------------
        ax.set_title("Distribution Comparison - Boxplot", fontsize=12)

        ax.set_xlabel("Distribution", fontsize=10)

        ax.set_ylabel("Value", fontsize=10)

        # ---------------------------------
        # Grid
        # ---------------------------------
        ax.grid(True, axis="y", alpha=0.3)

        plt.xticks(rotation=90, fontsize=9)

        plt.yticks(fontsize=9)

        plt.tight_layout()

        plt.show()
