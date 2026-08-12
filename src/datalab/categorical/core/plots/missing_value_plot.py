import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class MissingValuePlot:

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

            missing_count = column.isna().sum()

            data.append({"Column": title, "Missing Values": missing_count})

        data = pd.DataFrame(data)

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, ax = plt.subplots(figsize=(14, 7), dpi=200)

        sns.barplot(data=data, x="Column", y="Missing Values", color="steelblue", ax=ax)

        # ---------------------------------
        # Labels
        # ---------------------------------
        ax.set_title("Missing Values Comparison", fontsize=12)

        ax.set_xlabel("Column", fontsize=10)

        ax.set_ylabel("Missing Values", fontsize=10)

        # ---------------------------------
        # Grid
        # ---------------------------------
        ax.grid(True, axis="y", alpha=0.3)

        plt.xticks(rotation=0, fontsize=9)

        plt.yticks(fontsize=9)

        plt.tight_layout()

        plt.show()
