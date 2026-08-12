import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class ParetoPlot:

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

            cumulative_percentage = counts.cumsum() / counts.sum() * 100

            for category, count in counts.items():
                data.append(
                    {
                        "Category": category,
                        "Count": count,
                        "Cumulative Percentage": cumulative_percentage[category],
                        "Column": title,
                    }
                )

        data = pd.DataFrame(data)

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, ax = plt.subplots(figsize=(14, 7), dpi=200)

        sns.barplot(data=data, x="Category", y="Count", hue="Column", ax=ax)

        # ---------------------------------
        # Cumulative percentage
        # ---------------------------------
        ax2 = ax.twinx()

        for title in self.titles:

            subset = data[data["Column"] == title]

            ax2.plot(
                range(len(subset)),
                subset["Cumulative Percentage"],
                marker="o",
                label=title,
            )

        # ---------------------------------
        # Labels
        # ---------------------------------
        ax.set_title("Pareto Analysis - Categorical Distribution", fontsize=12)

        ax.set_xlabel("Category", fontsize=10)

        ax.set_ylabel("Count", fontsize=10)

        ax2.set_ylabel("Cumulative Percentage (%)", fontsize=10)

        # ---------------------------------
        # Grid
        # ---------------------------------
        ax.grid(True, axis="y", alpha=0.3)

        ax2.set_ylim(0, 105)

        # ---------------------------------
        # Ticks
        # ---------------------------------
        plt.xticks(rotation=90, fontsize=9)

        plt.yticks(fontsize=9)

        ax2.tick_params(axis="y", labelsize=9)

        plt.tight_layout()

        plt.show()
