import numpy as np
import pandas as pd


class InfiniteDistributionDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # Base Distribution
        # =====================================================

        base = rng.normal(loc=170, scale=8, size=1000)

        # =====================================================
        # 1. No Infinite Values
        # =====================================================

        no_infinite = pd.DataFrame({"value": base.copy()})

        # =====================================================
        # 2. Few Positive Infinite Values
        # =====================================================

        few_positive_infinite = pd.DataFrame({"value": base.copy()})

        few_positive_infinite.loc[[997, 998, 999], "value"] = np.inf

        # =====================================================
        # 3. Few Negative Infinite Values
        # =====================================================

        few_negative_infinite = pd.DataFrame({"value": base.copy()})

        few_negative_infinite.loc[[997, 998, 999], "value"] = -np.inf

        # =====================================================
        # 4. Positive and Negative Infinite Values
        # =====================================================

        positive_negative_infinite = pd.DataFrame({"value": base.copy()})

        positive_negative_infinite.loc[[996, 997], "value"] = np.inf

        positive_negative_infinite.loc[[998, 999], "value"] = -np.inf

        # =====================================================
        # 5. Many Infinite Values
        # =====================================================

        many_infinite = pd.DataFrame({"value": base.copy()})

        many_infinite.loc[np.arange(980, 990), "value"] = np.inf

        many_infinite.loc[np.arange(990, 1000), "value"] = -np.inf

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [
            no_infinite["value"],
            few_positive_infinite["value"],
            few_negative_infinite["value"],
            positive_negative_infinite["value"],
            many_infinite["value"],
        ]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = [
            "No Infinite Values",
            "Few Positive Infinite Values",
            "Few Negative Infinite Values",
            "Positive + Negative Infinite Values",
            "Many Infinite Values",
        ]
