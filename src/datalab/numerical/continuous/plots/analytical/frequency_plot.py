import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class FrequencyPlot:

    def __init__(self, column: pd.Series):
        self.column = column

    def _stats(self):
        """
        Calculate statistics required for the frequency plot.

        Returns
        -------
        pd.Series
            Frequency of each unique value.
        """

        numbers = self.column.dropna()

        frequency = (
            numbers
            .value_counts()
            .sort_index()
        )

        return frequency

    def draw(self):
        frequency = self._stats()

        # ==========================
        # Figure
        # ==========================
        fig, ax = plt.subplots(
            figsize=(15, 5),
            dpi=200
        )

        # ==========================
        # Frequency Plot
        # ==========================
        sns.barplot(
            x=frequency.index.astype(str),
            y=frequency.values,
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
                fontsize=8
            )

        # ==========================
        # Labels
        # ==========================
        ax.set_title(
            f"Value Frequency - {self.column.name}"
        )

        ax.set_xlabel(
            "Value"
        )

        ax.set_ylabel(
            "Frequency"
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
            label="Frequency"
        )

        ax.legend()

        # ==========================
        # Layout
        # ==========================
        plt.tight_layout()

        plt.show()
