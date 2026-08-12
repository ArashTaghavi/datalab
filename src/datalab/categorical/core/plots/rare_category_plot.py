import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class RareCategoryPlot:

    def __init__(
        self, columns: list[pd.Series], titles: list[str], threshold: float = 0.05
    ):
        self.columns = columns
        self.titles = titles
        self.threshold = threshold

    def draw(self):

        if len(self.columns) != len(self.titles):
            raise ValueError("The number of columns must match the number of titles.")

        # ---------------------------------
        # Prepare data
        # ---------------------------------
        data = []

        for column, title in zip(self.columns, self.titles):

            values = column.dropna()

            frequencies = values.value_counts(normalize=True)

            rare_categories = frequencies[frequencies < self.threshold]

            for category, frequency in rare_categories.items():
                data.append(
                    {"Category": category, "Frequency": frequency, "Column": title}
                )

        data = pd.DataFrame(data)

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, ax = plt.subplots(figsize=(14, 7), dpi=200)

        if not data.empty:

            sns.barplot(data=data, x="Category", y="Frequency", hue="Column", ax=ax)

        # ---------------------------------
        # Labels
        # ---------------------------------
        ax.set_title(f"Rare Categories (Frequency < {self.threshold:.1%})", fontsize=12)

        ax.set_xlabel("Category", fontsize=10)

        ax.set_ylabel("Frequency", fontsize=10)

        # ---------------------------------
        # Grid
        # ---------------------------------
        ax.grid(True, axis="y", alpha=0.3)

        plt.xticks(rotation=45, fontsize=9)

        plt.yticks(fontsize=9)

        plt.tight_layout()

        plt.show()
