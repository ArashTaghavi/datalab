import numpy as np
import pandas as pd


class SkewedDistributionDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # Base Distribution
        # =====================================================

        base = rng.normal(loc=170, scale=8, size=1000)

        # =====================================================
        # 1. Mild Right Skew
        # =====================================================

        mild_right_skew = pd.DataFrame(
            {"value": (base + np.maximum(base - 170, 0) * 0.3)}
        )

        # =====================================================
        # 2. Moderate Right Skew
        # =====================================================

        moderate_right_skew = pd.DataFrame(
            {"value": (base + np.maximum(base - 170, 0) * 0.7)}
        )

        # =====================================================
        # 3. Strong Right Skew
        # =====================================================

        strong_right_skew = pd.DataFrame(
            {"value": (base + np.maximum(base - 170, 0) * 1.2)}
        )

        # =====================================================
        # 4. Extreme Right Skew
        # =====================================================

        extreme_right_skew = pd.DataFrame(
            {"value": (base + np.maximum(base - 170, 0) * 2.0)}
        )

        # =====================================================
        # 5. Right Skew + Outliers
        # =====================================================

        right_skew_outliers = pd.DataFrame(
            {"value": (base + np.maximum(base - 170, 0) * 0.7)}
        )

        right_skew_outliers.loc[[95, 96, 97, 98, 99], "value"] = [
            210,
            220,
            230,
            245,
            260,
        ]

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [
            mild_right_skew["value"],
            moderate_right_skew["value"],
            strong_right_skew["value"],
            extreme_right_skew["value"],
            right_skew_outliers["value"],
        ]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = [
            "Mild Right Skew",
            "Moderate Right Skew",
            "Strong Right Skew",
            "Extreme Right Skew",
            "Right Skew + Outliers",
        ]
