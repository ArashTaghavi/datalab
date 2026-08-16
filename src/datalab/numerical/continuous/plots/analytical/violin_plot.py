import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class ViolinPlot:

    def __init__(self, column: pd.Series):
        self.column = column

    def _stats(self):
        """
        Calculate statistics required for the violin plot.

        Calculated metrics:

        - Q1
        - Median
        - Q3
        - Mean
        - IQR
        - Lower Outlier Bound
        - Upper Outlier Bound
        - Left Whisker
        - Right Whisker
        - Outlier Values
        """

        numbers = self.column.dropna()

        # =============================
        # Quartiles
        # =============================
        q1 = numbers.quantile(0.25)
        median = numbers.median()
        q3 = numbers.quantile(0.75)

        # =============================
        # Interquartile Range
        # =============================
        iqr = q3 - q1

        # =============================
        # Outlier Detection Bounds
        # =============================
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        # =============================
        # Outliers
        # =============================
        outliers = numbers[(numbers < lower) | (numbers > upper)]

        # =============================
        # Non-Outlier Values
        # =============================
        non_outlier_values = numbers[(numbers >= lower) & (numbers <= upper)]

        # =============================
        # Whiskers
        # =============================
        left_whisker = (
            non_outlier_values.min() if not non_outlier_values.empty else None
        )

        right_whisker = (
            non_outlier_values.max() if not non_outlier_values.empty else None
        )

        return {
            "Q1": q1,
            "Median": median,
            "Q3": q3,
            "Mean": numbers.mean(),
            "IQR": iqr,
            "Lower": lower,
            "Upper": upper,
            "Left Whisker": left_whisker,
            "Right Whisker": right_whisker,
            "Outliers": outliers,
        }

    def draw(self):

        column = self.column.dropna()
        stats = self._stats()

        fig, ax = plt.subplots(figsize=(15, 7), dpi=200)

        # ==========================
        # Violin Plot
        # ==========================
        sns.violinplot(x=column, ax=ax, inner=None)

        # ==========================
        # Q1
        # ==========================
        ax.axvline(
            stats["Q1"],
            color="blue",
            linestyle="--",
            alpha=0.7,
            label=f"Q1 = {stats['Q1']:.2f}",
        )

        ax.text(
            stats["Q1"],
            0.38,
            f"Q1\n{stats['Q1']:.2f}",
            ha="center",
            va="bottom",
            fontsize=8,
            color="blue",
            fontweight="bold",
            backgroundcolor="white",
        )

        # ==========================
        # Median
        # ==========================
        ax.axvline(
            stats["Median"],
            color="red",
            linestyle="-",
            linewidth=1.5,
            label=f"Median = {stats['Median']:.2f}",
        )

        ax.text(
            stats["Median"],
            0.45,
            f"Median\n{stats['Median']:.2f}",
            ha="center",
            va="bottom",
            fontsize=8,
            color="red",
            fontweight="bold",
            backgroundcolor="white",
        )

        # ==========================
        # Q3
        # ==========================
        ax.axvline(
            stats["Q3"],
            color="blue",
            linestyle="--",
            alpha=0.7,
            label=f"Q3 = {stats['Q3']:.2f}",
        )

        ax.text(
            stats["Q3"],
            0.38,
            f"Q3\n{stats['Q3']:.2f}",
            ha="center",
            va="bottom",
            fontsize=8,
            color="blue",
            fontweight="bold",
            backgroundcolor="white",
        )

        # ==========================
        # Mean
        # ==========================
        ax.axvline(
            stats["Mean"],
            color="purple",
            linestyle="-.",
            linewidth=1.5,
            label=f"Mean = {stats['Mean']:.2f}",
        )

        ax.text(
            stats["Mean"],
            -0.45,
            f"Mean\n{stats['Mean']:.2f}",
            ha="center",
            va="top",
            fontsize=8,
            color="purple",
            fontweight="bold",
            backgroundcolor="white",
        )

        # ==========================
        # Lower Bound
        # ==========================
        ax.axvline(
            stats["Lower"],
            color="blue",
            linestyle=":",
            alpha=0.8,
            label=f"Lower Bound = {stats['Lower']:.2f}",
        )

        ax.text(
            stats["Lower"],
            -0.35,
            f"Lower Bound\n{stats['Lower']:.2f}",
            ha="center",
            va="top",
            fontsize=7,
            color="blue",
            backgroundcolor="white",
        )

        # ==========================
        # Upper Bound
        # ==========================
        ax.axvline(
            stats["Upper"],
            color="blue",
            linestyle=":",
            alpha=0.8,
            label=f"Upper Bound = {stats['Upper']:.2f}",
        )

        ax.text(
            stats["Upper"],
            -0.35,
            f"Upper Bound\n{stats['Upper']:.2f}",
            ha="center",
            va="top",
            fontsize=7,
            color="blue",
            backgroundcolor="white",
        )

        # ==========================
        # Whiskers
        # ==========================
        if stats["Left Whisker"] is not None and stats["Right Whisker"] is not None:

            # Left whisker
            ax.plot(stats["Left Whisker"], 0, marker="|", markersize=14, color="green")

            # Right whisker
            ax.plot(stats["Right Whisker"], 0, marker="|", markersize=14, color="green")

            # Horizontal whisker line
            ax.plot(
                [stats["Left Whisker"], stats["Right Whisker"]],
                [0, 0],
                color="green",
                linewidth=1,
            )

            ax.text(
                stats["Left Whisker"],
                -0.15,
                f"Left Whisker\n{stats['Left Whisker']:.2f}",
                ha="center",
                va="top",
                fontsize=7,
                color="green",
                backgroundcolor="white",
            )

            ax.text(
                stats["Right Whisker"],
                -0.15,
                f"Right Whisker\n{stats['Right Whisker']:.2f}",
                ha="center",
                va="top",
                fontsize=7,
                color="green",
                backgroundcolor="white",
            )

            # Legend
            ax.plot(
                [],
                [],
                color="green",
                marker="|",
                linestyle="-",
                label=(
                    f"Whiskers = "
                    f"{stats['Left Whisker']:.2f} / "
                    f"{stats['Right Whisker']:.2f}"
                ),
            )

        # ==========================
        # Outliers
        # ==========================
        if not stats["Outliers"].empty:

            for value in stats["Outliers"]:

                ax.scatter(value, 0, color="red", s=25, zorder=10)

                ax.text(
                    value,
                    0.12,
                    f"Outlier\n{value:.2f}",
                    ha="center",
                    va="bottom",
                    fontsize=7,
                    color="red",
                    backgroundcolor="white",
                )

            ax.plot(
                [],
                [],
                color="red",
                marker="o",
                linestyle="None",
                label=f"Outliers = {len(stats['Outliers'])}",
            )

        # ==========================
        # Labels
        # ==========================
        ax.set_title(f"Violin Plot Analysis - {column.name}")

        ax.set_xlabel(column.name)

        ax.set_yticks([])

        ax.grid(True, axis="x", alpha=0.3)

        ax.legend(loc="upper right")

        plt.tight_layout()
        plt.show()
