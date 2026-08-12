import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class FrequencyPlot:

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

            frequency = values.value_counts().sort_index()

            for value, count in frequency.items():
                data.append({"Value": value, "Frequency": count, "Distribution": title})

        data = pd.DataFrame(data)

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, ax = plt.subplots(figsize=(14, 7), dpi=200)

        sns.barplot(data=data, x="Value", y="Frequency", hue="Distribution", ax=ax)

        # ---------------------------------
        # Labels
        # ---------------------------------
        ax.set_title("Distribution Comparison - Frequency", fontsize=12)

        ax.set_xlabel("Value", fontsize=10)

        ax.set_ylabel("Frequency", fontsize=10)

        # ---------------------------------
        # Grid
        # ---------------------------------
        ax.grid(True, axis="y", alpha=0.3)

        plt.xticks(fontsize=9)

        plt.yticks(fontsize=9)

        plt.tight_layout()

        plt.show()
