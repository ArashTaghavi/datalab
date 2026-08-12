import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class CardinalityPlot:

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

            cardinality = column.dropna().nunique()

            data.append({"Column": title, "Cardinality": cardinality})

        data = pd.DataFrame(data)

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, ax = plt.subplots(figsize=(14, 7), dpi=200)

        sns.barplot(data=data, x="Column", y="Cardinality", color="steelblue", ax=ax)

        # ---------------------------------
        # Value Labels
        # ---------------------------------
        for container in ax.containers:

            ax.bar_label(container, fmt="%.0f", fontsize=9, padding=3)

        # ---------------------------------
        # Labels
        # ---------------------------------
        ax.set_title("Categorical Cardinality Comparison", fontsize=12)

        ax.set_xlabel("Column", fontsize=10)

        ax.set_ylabel("Number of Unique Values", fontsize=10)

        # ---------------------------------
        # Grid
        # ---------------------------------
        ax.grid(True, axis="y", alpha=0.3)

        # ---------------------------------
        # Ticks
        # ---------------------------------
        plt.xticks(rotation=90, fontsize=9)

        plt.yticks(fontsize=9)

        # ---------------------------------
        # Layout
        # ---------------------------------
        plt.tight_layout()

        plt.show()
