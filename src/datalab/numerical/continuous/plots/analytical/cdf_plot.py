import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class CDFPlot:

    def __init__(self, column: pd.Series):
        self.column = column

    def _stats(self):
        """
        Calculate statistics required for the CDF plot.

        Calculated metrics:

        - P50
        - P90
        - P99
        """

        numbers = self.column.dropna()

        return {
            "P50": np.percentile(numbers, 50),
            "P90": np.percentile(numbers, 90),
            "P99": np.percentile(numbers, 99)
        }

    def draw(self):
        numbers = (
            self.column
            .dropna()
            .sort_values()
        )

        stats = self._stats()

        # ==========================
        # Figure
        # ==========================
        fig, ax = plt.subplots(
            figsize=(15, 5),
            dpi=200
        )

        # ==========================
        # CDF
        # ==========================
        y = (
                np.arange(1, len(numbers) + 1)
                / len(numbers)
        )

        ax.plot(
            numbers,
            y,
            color="blue",
            linewidth=2,
            label="CDF"
        )

        # ==========================
        # Percentiles
        # ==========================
        percentile_config = [
            ("P50", "green"),
            ("P90", "orange"),
            ("P99", "red")
        ]

        for name, color in percentile_config:
            value = stats[name]

            ax.axvline(
                value,
                color=color,
                linestyle="--",
                label=f"{name} = {value:.2f}"
            )

            ax.text(
                value,
                0.95 if name == "P50"
                else 0.80 if name == "P90"
                else 0.65,
                f"{name}\n{value:.2f}",
                color=color,
                fontsize=8,
                ha="center",
                va="top",
                rotation=90,
                backgroundcolor="white"
            )

        # ==========================
        # Labels
        # ==========================
        ax.set_title(
            f"CDF Analysis - {self.column.name}"
        )

        ax.set_xlabel(
            self.column.name
        )

        ax.set_ylabel(
            "Cumulative Probability"
        )

        # ==========================
        # Limits
        # ==========================
        ax.set_ylim(
            0,
            1
        )

        # ==========================
        # Grid & Legend
        # ==========================
        ax.grid(True)

        ax.legend()

        # ==========================
        # Layout
        # ==========================
        plt.tight_layout()

        plt.show()
