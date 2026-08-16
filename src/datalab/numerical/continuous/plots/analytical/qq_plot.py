import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats


class QQPlot:

    def __init__(self, column: pd.Series):
        self.column = column

    def _stats(self):
        """
        Calculate statistics required for the QQ plot.

        Calculated metrics:

        - Theoretical Quantiles
        - Sample Quantiles
        - Reference Line
        """

        numbers = self.column.dropna()

        (
            theoretical_quantiles,
            sample_quantiles
        ), (
            slope,
            intercept,
            _
        ) = stats.probplot(
            numbers,
            dist="norm"
        )

        return {
            "Theoretical Quantiles": theoretical_quantiles,
            "Sample Quantiles": sample_quantiles,
            "Slope": slope,
            "Intercept": intercept
        }

    def draw(self):
        numbers = self.column.dropna()

        # ==========================
        # Figure
        # ==========================
        fig, ax = plt.subplots(
            figsize=(15, 5),
            dpi=200
        )

        # ==========================
        # QQ Plot
        # ==========================
        stats.probplot(
            numbers,
            dist="norm",
            plot=ax
        )

        # ==========================
        # Font Settings
        # ==========================
        title_fontsize = 10
        label_fontsize = 9

        # ==========================
        # Title
        # ==========================
        ax.set_title(
            f"QQ Plot - {self.column.name}",
            fontsize=title_fontsize
        )

        # ==========================
        # Axis Labels
        # ==========================
        ax.set_xlabel(
            "Theoretical Quantiles",
            fontsize=label_fontsize
        )

        ax.set_ylabel(
            "Sample Quantiles",
            fontsize=label_fontsize
        )

        # ==========================
        # Tick Labels
        # ==========================
        ax.tick_params(
            axis="both",
            labelsize=label_fontsize
        )

        # ==========================
        # Grid
        # ==========================
        ax.grid(
            alpha=0.3
        )

        # ==========================
        # Legend
        # ==========================
        ax.legend(
            ["Data", "Reference Line"],
            fontsize=label_fontsize
        )

        # ==========================
        # Layout
        # ==========================
        plt.tight_layout()

        plt.show()
