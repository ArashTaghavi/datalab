import numpy as np
import pandas as pd


class NormalDistributionDataset:

    def __init__(self, seed=42):
        rng = np.random.default_rng(seed)

        # =====================================================
        # 1. Normal Distribution - Low Variance
        # =====================================================

        low_variance = pd.DataFrame(
            {"height": rng.normal(loc=170, scale=3, size=1000).astype(int)}
        )

        # =====================================================
        # 2. Normal Distribution - Moderate Variance
        # =====================================================

        moderate_variance = pd.DataFrame(
            {"height": rng.normal(loc=170, scale=10, size=1000).astype(int)}
        )

        # =====================================================
        # 3. Normal Distribution - High Variance
        # =====================================================

        high_variance = pd.DataFrame(
            {"height": rng.normal(loc=170, scale=20, size=1000).astype(int)}
        )

        # =====================================================
        # 4. Normal Distribution - Different Mean
        # =====================================================

        different_mean = pd.DataFrame(
            {"height": rng.normal(loc=185, scale=10, size=1000).astype(int)}
        )

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [
            low_variance["height"],
            moderate_variance["height"],
            high_variance["height"],
            different_mean["height"],
        ]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = [
            "Low Variance",
            "Medium Variance",
            "High Variance",
            "Shifted Mean",
        ]
