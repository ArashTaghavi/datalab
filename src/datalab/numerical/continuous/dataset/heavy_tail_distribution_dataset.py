import numpy as np
import pandas as pd


class HeavyTailDistributionDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # 1. Mild Heavy Tail
        # =====================================================

        mild_heavy_tail = pd.DataFrame(
            {"value": 170 + 8 * rng.standard_t(df=15, size=1000)}
        )

        # =====================================================
        # 2. Moderate Heavy Tail
        # =====================================================

        moderate_heavy_tail = pd.DataFrame(
            {"value": 170 + 8 * rng.standard_t(df=8, size=1000)}
        )

        # =====================================================
        # 3. Strong Heavy Tail
        # =====================================================

        strong_heavy_tail = pd.DataFrame(
            {"value": 170 + 8 * rng.standard_t(df=5, size=1000)}
        )

        # =====================================================
        # 4. Extreme Heavy Tail
        # =====================================================

        extreme_heavy_tail = pd.DataFrame(
            {"value": 170 + 8 * rng.standard_t(df=3, size=1000)}
        )

        # =====================================================
        # 5. Heavy Tail + Outliers
        # =====================================================

        heavy_tail_outliers = pd.DataFrame(
            {"value": 170 + 8 * rng.standard_t(df=8, size=1000)}
        )

        heavy_tail_outliers.loc[[995, 996, 997, 998, 999], "value"] = [
            215,
            225,
            240,
            255,
            275,
        ]

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [
            mild_heavy_tail["value"],
            moderate_heavy_tail["value"],
            strong_heavy_tail["value"],
            extreme_heavy_tail["value"],
            heavy_tail_outliers["value"],
        ]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = [
            "Mild Heavy Tail",
            "Moderate Heavy Tail",
            "Strong Heavy Tail",
            "Extreme Heavy Tail",
            "Heavy Tail + Outliers",
        ]
