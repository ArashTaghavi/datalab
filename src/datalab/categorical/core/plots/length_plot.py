import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class LengthPlot:

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

            values = column.dropna().astype(str)

            for value in values:
                data.append({"Length": len(value), "Column": title})

        data = pd.DataFrame(data)

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, ax = plt.subplots(figsize=(14, 7), dpi=200)

        sns.histplot(
            data=data, x="Length", hue="Column", discrete=True, multiple="dodge", ax=ax
        )

        # ---------------------------------
        # Labels
        # ---------------------------------
        ax.set_title("Category Length Distribution", fontsize=12)

        ax.set_xlabel("String Length", fontsize=10)

        ax.set_ylabel("Count", fontsize=10)

        # ---------------------------------
        # Grid
        # ---------------------------------
        ax.grid(True, axis="y", alpha=0.3)

        plt.xticks(fontsize=9)

        plt.yticks(fontsize=9)

        plt.tight_layout()

        plt.show()
