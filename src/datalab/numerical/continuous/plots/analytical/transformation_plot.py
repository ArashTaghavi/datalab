import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import yeojohnson


class TransformationPlot:

    def __init__(
        self,
        column: pd.Series,
        method: str = "log"
    ):
        self.column = column
        self.method = method.lower()

    def _transform(self):
        """
        Apply the selected transformation.

        Supported methods:

        - log
        - log1p
        - yeo-johnson
        - none
        """

        numbers = self.column.dropna()

        # ==========================
        # No Transformation
        # ==========================
        if self.method == "none":

            return numbers.copy()

        # ==========================
        # Log Transformation
        # ==========================
        elif self.method == "log":

            if (numbers <= 0).any():
                raise ValueError(
                    "Log transformation requires all values to be greater than zero."
                )

            return np.log(numbers)

        # ==========================
        # Log1p Transformation
        # ==========================
        elif self.method == "log1p":

            if (numbers < 0).any():
                raise ValueError(
                    "Log1p transformation requires all values to be greater than or equal to zero."
                )

            return np.log1p(numbers)

        # ==========================
        # Yeo-Johnson Transformation
        # ==========================
        elif self.method in {"yeo-johnson", "yeojohnson"}:

            transformed, _ = yeojohnson(numbers)

            return pd.Series(
                transformed,
                index=numbers.index
            )

        # ==========================
        # Invalid Method
        # ==========================
        else:

            raise ValueError(
                f"Unsupported transformation method: {self.method}"
            )

    def _method_name(self):
        """
        Return a readable name for the selected transformation.
        """

        names = {
            "log": "Log Transformation",
            "log1p": "Log1p Transformation",
            "yeo-johnson": "Yeo-Johnson Transformation",
            "yeojohnson": "Yeo-Johnson Transformation",
            "none": "No Transformation"
        }

        return names[self.method]

    def _stats(self):
        """
        Calculate data required for the transformation plot.

        Returns
        -------
        dict
            Original and transformed numerical data.
        """

        original = self.column.dropna()

        transformed = self._transform()

        return {
            "Original": original,
            "Transformed": transformed,
            "Method": self._method_name()
        }

    def draw(self):
        """
        Plot the original and transformed distributions.
        """

        stats = self._stats()

        original = stats["Original"]
        transformed = stats["Transformed"]
        method = stats["Method"]

        # ==========================
        # Font Settings
        # ==========================
        title_fontsize = 10
        label_fontsize = 9

        # ==========================
        # Figure
        # ==========================
        fig, axes = plt.subplots(
            1,
            2,
            figsize=(15, 5),
            dpi=200
        )

        # ==========================
        # Original Distribution
        # ==========================
        sns.kdeplot(
            original,
            fill=True,
            color="steelblue",
            alpha=0.3,
            linewidth=2,
            ax=axes[0]
        )

        axes[0].set_title(
            "Original Distribution",
            fontsize=title_fontsize
        )

        axes[0].set_xlabel(
            self.column.name,
            fontsize=label_fontsize
        )

        axes[0].set_ylabel(
            "Density",
            fontsize=label_fontsize
        )

        # ==========================
        # Transformed Distribution
        # ==========================
        sns.kdeplot(
            transformed,
            fill=True,
            color="green",
            alpha=0.3,
            linewidth=2,
            ax=axes[1]
        )

        axes[1].set_title(
            f"After {method}",
            fontsize=title_fontsize
        )

        axes[1].set_xlabel(
            self.column.name,
            fontsize=label_fontsize
        )

        axes[1].set_ylabel(
            "Density",
            fontsize=label_fontsize
        )

        # ==========================
        # Axes Settings
        # ==========================
        for ax in axes:

            ax.tick_params(
                axis="both",
                labelsize=label_fontsize
            )

            ax.grid(
                alpha=0.3
            )

        # ==========================
        # Figure Title
        # ==========================
        fig.suptitle(
            f"Transformation Analysis - {self.column.name}",
            fontsize=title_fontsize
        )

        # ==========================
        # Layout
        # ==========================
        plt.tight_layout()

        plt.show()