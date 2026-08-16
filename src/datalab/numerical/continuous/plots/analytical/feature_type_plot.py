import matplotlib.pyplot as plt
import pandas as pd


class FeatureTypePlot:

    def __init__(self, column: pd.Series):
        self.column = column

    def _stats(self):
        """
        Calculate statistics required for feature type detection.

        Calculated metrics:

        - Unique Count
        - Total Count
        - Unique Ratio
        - Feature Type
        """

        numbers = self.column.dropna()

        unique_count = numbers.nunique()
        total_count = len(numbers)

        unique_ratio = (
            unique_count / total_count
            if total_count > 0
            else 0
        )

        # -----------------------------
        # Feature Type
        # -----------------------------
        if unique_ratio > 0.95:

            feature_type = "Identifier"

        elif unique_count <= 10:

            feature_type = "Categorical Numerical"

        elif (
            numbers.astype(int) == numbers
        ).all():

            feature_type = "Discrete Numerical"

        else:

            feature_type = "Continuous Numerical"

        return {
            "Unique Count": unique_count,
            "Total Count": total_count,
            "Unique Ratio": unique_ratio,
            "Feature Type": feature_type
        }

    def draw(self):

        stats = self._stats()

        feature_type = stats["Feature Type"]

        feature_types = [
            "Identifier",
            "Categorical Numerical",
            "Discrete Numerical",
            "Continuous Numerical"
        ]

        # ==========================
        # Figure
        # ==========================
        fig, ax = plt.subplots(
            figsize=(15, 5),
            dpi=200
        )

        # ==========================
        # Feature Type Status
        # ==========================
        for index, current_type in enumerate(feature_types):

            is_detected = current_type == feature_type

            ax.scatter(
                index,
                0,
                s=180 if is_detected else 100,
                color="steelblue" if is_detected else "lightgray",
                edgecolor="black",
                linewidth=1
            )

            ax.text(
                index,
                0,
                "●" if is_detected else "○",
                ha="center",
                va="center",
                fontsize=14,
                color="white" if is_detected else "gray",
                fontweight="bold"
            )

            ax.text(
                index,
                -0.18,
                current_type,
                ha="center",
                va="top",
                fontsize=9,
                fontweight="bold" if is_detected else "normal",
                color="steelblue" if is_detected else "black",
                backgroundcolor="white"
            )

        # ==========================
        # Statistics
        # ==========================
        ax.text(
            0.02,
            0.95,
            (
                f"Detected Type: {feature_type}\n"
                f"Unique Values: {stats['Unique Count']}\n"
                f"Unique Ratio: {stats['Unique Ratio']:.2%}"
            ),
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=9,
            backgroundcolor="white"
        )

        # ==========================
        # Legend
        # ==========================
        ax.scatter(
            [],
            [],
            s=100,
            color="steelblue",
            edgecolor="black",
            label=f"Detected: {feature_type}"
        )

        ax.scatter(
            [],
            [],
            s=100,
            color="lightgray",
            edgecolor="black",
            label="Not Detected"
        )

        # ==========================
        # Labels
        # ==========================
        ax.set_title(
            f"Feature Type - {self.column.name}"
        )

        ax.set_xlabel("")

        ax.set_ylabel("")

        ax.set_xticks([])

        ax.set_yticks([])

        ax.set_ylim(
            -0.35,
            0.35
        )

        # ==========================
        # Grid
        # ==========================
        ax.grid(
            axis="x",
            alpha=0.2
        )

        # ==========================
        # Legend
        # ==========================
        ax.legend()

        # ==========================
        # Layout
        # ==========================
        plt.tight_layout()

        plt.show()