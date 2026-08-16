import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class BoxPlot:

    def __init__(self, column: pd.Series):
        self.column = column

    def _stats(self):
        """
        Calculate statistics required for the box plot.

        Calculated metrics:

        - Q1
        - Median
        - Q3
        - Mean
        - Lower Outlier Bound
        - Upper Outlier Bound
        - Left Whisker
        - Right Whisker
        - Outlier Values
        """

        numbers = self.column

        # -----------------------------
        # Quartiles
        # -----------------------------
        q1 = numbers.quantile(0.25)
        median = numbers.median()
        q3 = numbers.quantile(0.75)

        # -----------------------------
        # Interquartile Range
        # -----------------------------
        iqr = q3 - q1

        # -----------------------------
        # Outlier Detection Bounds
        # -----------------------------
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        # -----------------------------
        # Outliers
        # -----------------------------
        outliers = numbers[
            (numbers < lower) |
            (numbers > upper)
            ]

        # -----------------------------
        # Whiskers
        # -----------------------------
        non_outlier_values = numbers[
            (numbers >= lower) &
            (numbers <= upper)
            ]

        left_whisker = (
            non_outlier_values.min()
            if not non_outlier_values.empty
            else None
        )

        right_whisker = (
            non_outlier_values.max()
            if not non_outlier_values.empty
            else None
        )

        return {
            "Q1": q1,
            "Median": median,
            "Q3": q3,
            "Mean": numbers.mean(),
            "Lower": lower,
            "Upper": upper,
            "Left Whisker": left_whisker,
            "Right Whisker": right_whisker,
            "Outliers": outliers
        }

    def draw(self):

        column = self.column
        stats = self._stats()

        fig, ax = plt.subplots(
            figsize=(15, 6),
            dpi=200
        )

        # ==========================
        # Box Plot
        # ==========================
        sns.boxplot(
            x=column,
            ax=ax
        )

        # ==========================
        # Lower Bound
        # ==========================
        ax.axvline(
            stats["Lower"],
            color="blue",
            linestyle="--",
            label=f"Lower Bound = {stats['Lower']:.2f}"
        )

        ax.text(
            stats["Lower"],
            -0.25,
            f"Lower\n{stats['Lower']:.2f}",
            ha="center",
            va="top",
            fontsize=8,
            color="blue",
            backgroundcolor="white"
        )

        # ==========================
        # Upper Bound
        # ==========================
        ax.axvline(
            stats["Upper"],
            color="blue",
            linestyle="--",
            label=f"Upper Bound = {stats['Upper']:.2f}"
        )

        ax.text(
            stats["Upper"],
            -0.25,
            f"Upper\n{stats['Upper']:.2f}",
            ha="center",
            va="top",
            fontsize=8,
            color="blue",
            backgroundcolor="white"
        )

        # ==========================
        # Q1
        # ==========================
        ax.plot(
            [],
            [],
            color="blue",
            linestyle="None",
            marker="|",
            markersize=10,
            label=f"Q1 = {stats['Q1']:.2f}"
        )

        ax.text(
            stats["Q1"],
            0,
            f"Q1\n{stats['Q1']:.2f}",
            ha="center",
            va="center",
            fontsize=7,
            color="blue",
            fontweight="bold",
            backgroundcolor="white"
        )

        # ==========================
        # Median
        # ==========================
        ax.axvline(
            stats["Median"],
            color="red",
            linestyle="-",
            label=f"Median = {stats['Median']:.2f}"
        )

        ax.text(
            stats["Median"],
            0,
            f"Median\n{stats['Median']:.2f}",
            ha="center",
            va="center",
            fontsize=7,
            color="red",
            fontweight="bold",
            backgroundcolor="white"
        )

        # ==========================
        # Q3
        # ==========================
        ax.plot(
            [],
            [],
            color="blue",
            linestyle="None",
            marker="|",
            markersize=10,
            label=f"Q3 = {stats['Q3']:.2f}"
        )

        ax.text(
            stats["Q3"],
            0,
            f"Q3\n{stats['Q3']:.2f}",
            ha="center",
            va="center",
            fontsize=7,
            color="blue",
            fontweight="bold",
            backgroundcolor="white"
        )

        # ==========================
        # Mean
        # ==========================
        ax.axvline(
            stats["Mean"],
            color="purple",
            linestyle="-.",
            label=f"Mean = {stats['Mean']:.2f}"
        )

        ax.text(
            stats["Mean"],
            0.25,
            f"Mean\n{stats['Mean']:.2f}",
            ha="center",
            va="bottom",
            fontsize=8,
            color="purple",
            backgroundcolor="white"
        )

        # ==========================
        # Whiskers
        # ==========================
        if (
                stats["Left Whisker"] is not None and
                stats["Right Whisker"] is not None
        ):

            ax.plot(
                [],
                [],
                color="green",
                linestyle="None",
                marker="_",
                markersize=10,
                label=(
                    f"Whiskers = "
                    f"{stats['Left Whisker']:.2f} / "
                    f"{stats['Right Whisker']:.2f}"
                )
            )

            for value, name in [
                (stats["Left Whisker"], "Left Whisker"),
                (stats["Right Whisker"], "Right Whisker")
            ]:
                ax.text(
                    value,
                    -0.08,
                    f"{name}\n{value:.2f}",
                    ha="center",
                    va="top",
                    fontsize=7,
                    color="green",
                    backgroundcolor="white"
                )

        # ==========================
        # Outliers
        # ==========================
        if not stats["Outliers"].empty:

            for value in stats["Outliers"]:
                ax.text(
                    value,
                    0.05,
                    f"Outlier\n{value:.2f}",
                    ha="center",
                    va="bottom",
                    fontsize=7,
                    color="red",
                    backgroundcolor="white"
                )

            ax.plot(
                [],
                [],
                color="red",
                linestyle="None",
                marker="o",
                label=f"Outliers = {len(stats['Outliers'])}"
            )

        ax.set_title(
            f"Box Plot Analysis - {column.name}"
        )

        ax.set_xlabel(column.name)

        ax.grid(True)

        ax.legend()

        plt.show()
