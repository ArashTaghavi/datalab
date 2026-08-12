import numpy as np
import pandas as pd


class DiscreteDistributionDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # 1. Few Unique Values
        # =====================================================

        few_unique = pd.DataFrame({"count": rng.integers(low=1, high=6, size=1000)})

        # =====================================================
        # 2. Many Unique Values
        # =====================================================

        many_unique = pd.DataFrame({"count": rng.integers(low=1, high=21, size=1000)})

        # =====================================================
        # 3. Imbalanced Frequency
        # =====================================================

        imbalanced = pd.DataFrame(
            {
                "count": rng.choice(
                    [1, 2, 3, 4, 5], size=1000, p=[0.55, 0.25, 0.12, 0.06, 0.02]
                )
            }
        )

        # =====================================================
        # 4. Shifted Values
        # =====================================================

        shifted_values = pd.DataFrame(
            {"count": rng.integers(low=101, high=121, size=1000)}
        )

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [
            few_unique["count"],
            many_unique["count"],
            imbalanced["count"],
            shifted_values["count"],
        ]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = [
            "Few Unique Values",
            "Many Unique Values",
            "Imbalanced Frequency",
            "Shifted Values",
        ]
