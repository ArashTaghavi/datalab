import numpy as np
import pandas as pd


class ZeroInflatedDistributionDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # 1. Low Zero Inflation
        # =====================================================

        low_zero_inflation = pd.DataFrame(
            {
                "value": np.where(
                    rng.random(1000) < 0.10,
                    0,
                    rng.normal(loc=170, scale=8, size=1000),
                )
            }
        )

        # =====================================================
        # 2. Moderate Zero Inflation
        # =====================================================

        moderate_zero_inflation = pd.DataFrame(
            {
                "value": np.where(
                    rng.random(1000) < 0.30,
                    0,
                    rng.normal(loc=170, scale=8, size=1000),
                )
            }
        )

        # =====================================================
        # 3. High Zero Inflation
        # =====================================================

        high_zero_inflation = pd.DataFrame(
            {
                "value": np.where(
                    rng.random(1000) < 0.50,
                    0,
                    rng.normal(loc=170, scale=8, size=1000),
                )
            }
        )

        # =====================================================
        # 4. Extreme Zero Inflation
        # =====================================================

        extreme_zero_inflation = pd.DataFrame(
            {
                "value": np.where(
                    rng.random(1000) < 0.70,
                    0,
                    rng.normal(loc=170, scale=8, size=1000),
                )
            }
        )

        # =====================================================
        # 5. Zero Inflation + Outliers
        # =====================================================

        zero_inflation_outliers = pd.DataFrame(
            {
                "value": np.where(
                    rng.random(1000) < 0.50,
                    0,
                    rng.normal(loc=170, scale=8, size=1000),
                )
            }
        )

        zero_inflation_outliers.loc[[995, 996, 997, 998, 999], "value"] = [
            220,
            235,
            250,
            270,
            300,
        ]

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [
            low_zero_inflation["value"],
            moderate_zero_inflation["value"],
            high_zero_inflation["value"],
            extreme_zero_inflation["value"],
            zero_inflation_outliers["value"],
        ]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = [
            "Low Zero Inflation",
            "Moderate Zero Inflation",
            "High Zero Inflation",
            "Extreme Zero Inflation",
            "Zero Inflation + Outliers",
        ]
