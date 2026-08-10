import numpy as np
import pandas as pd


class OutlierDistributionDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # Base Distribution
        # =====================================================

        base = rng.normal(loc=170, scale=8, size=1000)

        # =====================================================
        # 1. No Outliers
        # =====================================================

        no_outliers = pd.DataFrame({"value": base.copy()})

        # =====================================================
        # 2. Few Outliers
        # =====================================================

        few_outliers = pd.DataFrame({"value": base.copy()})

        few_outliers.loc[[997, 998, 999], "value"] = [
            205,
            215,
            225,
        ]

        # =====================================================
        # 3. Many Outliers
        # =====================================================

        many_outliers = pd.DataFrame({"value": base.copy()})

        many_outliers.loc[
            [990, 991, 992, 993, 994, 995, 996, 997, 998, 999], "value"
        ] = [
            195,
            198,
            201,
            204,
            207,
            210,
            213,
            216,
            219,
            222,
        ]

        # =====================================================
        # 4. Symmetric Outliers
        # =====================================================

        symmetric_outliers = pd.DataFrame({"value": base.copy()})

        symmetric_outliers.loc[[990, 991, 992, 993, 994], "value"] = [
            135,
            140,
            145,
            150,
            155,
        ]

        symmetric_outliers.loc[[995, 996, 997, 998, 999], "value"] = [
            185,
            190,
            195,
            200,
            205,
        ]

        # =====================================================
        # 5. One Extreme Outlier
        # =====================================================

        one_extreme_outlier = pd.DataFrame({"value": base.copy()})

        one_extreme_outlier.loc[999, "value"] = 300

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [
            no_outliers["value"],
            few_outliers["value"],
            many_outliers["value"],
            symmetric_outliers["value"],
            one_extreme_outlier["value"],
        ]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = [
            "No Outliers",
            "Few Outliers",
            "Many Outliers",
            "Symmetric Outliers",
            "One Extreme Outlier",
        ]
