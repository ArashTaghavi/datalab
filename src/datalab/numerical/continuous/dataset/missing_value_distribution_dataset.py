import numpy as np
import pandas as pd


class MissingValueDistributionDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # Base Distribution
        # =====================================================

        base = rng.normal(loc=170, scale=8, size=1000)

        # =====================================================
        # 1. No Missing Values
        # =====================================================

        no_missing = pd.DataFrame({"value": base.copy()})

        # =====================================================
        # 2. Few Missing Values
        # =====================================================

        few_missing = pd.DataFrame({"value": base.copy()})

        few_missing.loc[[997, 998, 999], "value"] = np.nan

        # =====================================================
        # 3. Moderate Missing Values
        # =====================================================

        moderate_missing = pd.DataFrame({"value": base.copy()})

        moderate_missing.loc[np.arange(900, 1000), "value"] = np.nan

        # =====================================================
        # 4. Many Missing Values
        # =====================================================

        many_missing = pd.DataFrame({"value": base.copy()})

        many_missing.loc[np.arange(500, 1000), "value"] = np.nan

        # =====================================================
        # 5. Extreme Missing Values
        # =====================================================

        extreme_missing = pd.DataFrame({"value": base.copy()})

        extreme_missing.loc[np.arange(100, 1000), "value"] = np.nan

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [
            no_missing["value"],
            few_missing["value"],
            moderate_missing["value"],
            many_missing["value"],
            extreme_missing["value"],
        ]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = [
            "No Missing Values",
            "Few Missing Values",
            "Moderate Missing Values",
            "Many Missing Values",
            "Extreme Missing Values",
        ]
