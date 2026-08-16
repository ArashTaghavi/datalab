import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class BinningPlot:

    def __init__(
            self,
            column: pd.Series,
            bins: int = 5
    ):
        self.column = column
        self.bins = bins

    def _stats(self):
        """
        Calculate statistics required for the binning plot.

        Calculated metrics:

        - Value Range
        - Count
        - Percentage
        """

        numbers = self.column.dropna()

        binned = pd.cut(
            numbers,
            bins=self.bins
        )

        frequency = (
            binned
            .value_counts()
            .sort_index()
        )

        percentage = (
                frequency /
                frequency.sum() *
                100
        )

        return pd.DataFrame({
            "Range": frequency.index.astype(str),
            "Count": frequency.values,
            "Percentage": percentage.values
        })

    def draw(self):
        data = self._stats()

        # ==========================
        # Font Settings
        # ==========================
        title_fontsize = 10
        label_fontsize = 9

        # ==========================
        # Figure
        # ==========================
        fig, ax = plt.subplots(
            figsize=(15, 5),
            dpi=200
        )

        # ==========================
        # Binning Plot
        # ==========================
        sns.barplot(
            data=data,
            x="Range",
            y="Percentage",
            color="steelblue",
            edgecolor="black",
            ax=ax
        )

        # ==========================
        # Value Labels
        # ==========================
        for container in ax.containers:
            ax.bar_label(
                container,
                fmt="%.1f%%",
                fontsize=label_fontsize
            )

        # ==========================
        # Labels
        # ==========================
        ax.set_title(
            f"Binning Analysis - {self.column.name}",
            fontsize=title_fontsize
        )

        ax.set_xlabel(
            "Value Range",
            fontsize=label_fontsize
        )

        ax.set_ylabel(
            "Percentage",
            fontsize=label_fontsize
        )

        # ==========================
        # Tick Labels
        # ==========================
        ax.tick_params(
            axis="both",
            labelsize=label_fontsize
        )

        plt.xticks(
            rotation=90
        )

        # ==========================
        # Grid
        # ==========================
        ax.grid(
            axis="y",
            alpha=0.3
        )

        # ==========================
        # Legend
        # ==========================
        ax.plot(
            [],
            [],
            color="steelblue",
            linewidth=8,
            label="Percentage"
        )

        ax.legend(
            fontsize=label_fontsize
        )

        # ==========================
        # Layout
        # ==========================
        plt.tight_layout()

        plt.show()
