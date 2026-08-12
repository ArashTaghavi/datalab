import matplotlib.pyplot as plt
import pandas as pd


class PiePlot:

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

            counts = values.value_counts()

            for category, count in counts.items():
                data.append({"Category": category, "Count": count, "Column": title})

        data = pd.DataFrame(data)

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, axes = plt.subplots(1, len(self.columns), figsize=(14, 7), dpi=200)

        if len(self.columns) == 1:
            axes = [axes]

        for ax, title in zip(axes, self.titles):

            subset = data[data["Column"] == title]

            ax.pie(
                subset["Count"],
                labels=subset["Category"],
                autopct="%1.1f%%",
                startangle=90,
            )

            ax.set_title(title, fontsize=12)

        # ---------------------------------
        # Labels
        # ---------------------------------
        fig.suptitle("Category Proportion Distribution", fontsize=12)

        # ---------------------------------
        # Layout
        # ---------------------------------
        plt.tight_layout()

        plt.show()
