import matplotlib.pyplot as plt
import pandas as pd
import squarify


class TreemapPlot:

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

            subset = data[data["Column"] == title].copy()

            # ---------------------------------
            # Percentage
            # ---------------------------------
            total = subset["Count"].sum()

            subset["Percentage"] = subset["Count"] / total * 100

            # ---------------------------------
            # Labels
            # ---------------------------------
            labels = [
                f"{category}\n" f"Count: {count}\n" f"{percentage:.1f}%"
                for category, count, percentage in zip(
                    subset["Category"], subset["Count"], subset["Percentage"]
                )
            ]

            # ---------------------------------
            # Colors
            # ---------------------------------
            colors = plt.cm.tab20(range(len(subset)))

            # ---------------------------------
            # Treemap
            # ---------------------------------
            squarify.plot(
                sizes=subset["Count"].values,
                label=labels,
                color=colors,
                alpha=0.8,
                ax=ax,
                text_kwargs={"fontsize": 9},
            )

            ax.set_title(title, fontsize=12)

            ax.axis("off")

        # ---------------------------------
        # Labels
        # ---------------------------------
        fig.suptitle("Category Distribution - Treemap", fontsize=12)

        # ---------------------------------
        # Layout
        # ---------------------------------
        plt.tight_layout()

        plt.show()
