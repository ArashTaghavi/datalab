import matplotlib.pyplot as plt
import pandas as pd


class MissingValuePlot:

    def __init__(self, column: pd.Series):
        self.column = column

    def _stats(self):
        """
        Calculate statistics required for the missing value plot.

        Calculated metrics:

        - Missing Count
        - Existing Count
        """

        missing = self.column.isna().sum()
        existing = len(self.column) - missing

        return {
            "Missing": missing,
            "Existing": existing
        }

    def draw(self):
        stats = self._stats()

        labels = [
            "Existing",
            "Missing"
        ]

        values = [
            stats["Existing"],
            stats["Missing"]
        ]

        colors = [
            "green",
            "red"
        ]

        # ==========================
        # Font Settings
        # ==========================
        title_fontsize = 10
        label_fontsize = 8

        # ==========================
        # Figure
        # ==========================
        fig, ax = plt.subplots(
            figsize=(15, 5),
            dpi=200
        )

        # ==========================
        # Donut Chart
        # ==========================
        wedges, texts, autotexts = ax.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=lambda pct: f"{pct:.1f}%",
            startangle=90,
            counterclock=False,
            wedgeprops={
                "width": 0.4,
                "edgecolor": "white"
            },
            textprops={
                "fontsize": label_fontsize
            }
        )

        # ==========================
        # Percentage Labels
        # ==========================
        for autotext in autotexts:
            autotext.set_fontsize(label_fontsize)
            autotext.set_fontweight("bold")

        # ==========================
        # Center Information
        # ==========================
        total = stats["Existing"] + stats["Missing"]

        ax.text(
            0,
            0,
            f"Total\n{total}",
            ha="center",
            va="center",
            fontsize=label_fontsize,
            fontweight="bold"
        )

        # ==========================
        # Title
        # ==========================
        ax.set_title(
            f"Missing Value Analysis - {self.column.name}",
            fontsize=title_fontsize
        )

        # ==========================
        # Legend
        # ==========================
        ax.legend(
            wedges,
            [
                f"Existing = {stats['Existing']}",
                f"Missing = {stats['Missing']}"
            ],
            loc="center left",
            bbox_to_anchor=(1, 0.5),
            fontsize=label_fontsize
        )

        # ==========================
        # Layout
        # ==========================
        plt.tight_layout()

        plt.show()
