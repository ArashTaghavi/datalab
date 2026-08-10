import numpy as np
import pandas as pd


class MultimodalDistributionDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # 1. Unimodal
        # =====================================================

        unimodal = pd.DataFrame({"value": rng.normal(loc=170, scale=8, size=1000)})

        # =====================================================
        # 2. Bimodal - Balanced
        # =====================================================

        bimodal_balanced = pd.DataFrame(
            {
                "value": np.concatenate(
                    [
                        rng.normal(loc=155, scale=5, size=500),
                        rng.normal(loc=185, scale=5, size=500),
                    ]
                )
            }
        )

        # =====================================================
        # 3. Bimodal - Imbalanced
        # =====================================================

        bimodal_imbalanced = pd.DataFrame(
            {
                "value": np.concatenate(
                    [
                        rng.normal(loc=160, scale=5, size=750),
                        rng.normal(loc=190, scale=5, size=250),
                    ]
                )
            }
        )

        # =====================================================
        # 4. Trimodal
        # =====================================================

        trimodal = pd.DataFrame(
            {
                "value": np.concatenate(
                    [
                        rng.normal(loc=150, scale=4, size=350),
                        rng.normal(loc=170, scale=4, size=350),
                        rng.normal(loc=190, scale=4, size=300),
                    ]
                )
            }
        )

        # =====================================================
        # 5. Overlapping Modes
        # =====================================================

        overlapping_modes = pd.DataFrame(
            {
                "value": np.concatenate(
                    [
                        rng.normal(loc=160, scale=8, size=500),
                        rng.normal(loc=175, scale=8, size=500),
                    ]
                )
            }
        )

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [
            unimodal["value"],
            bimodal_balanced["value"],
            bimodal_imbalanced["value"],
            trimodal["value"],
            overlapping_modes["value"],
        ]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = [
            "Unimodal",
            "Bimodal - Balanced",
            "Bimodal - Imbalanced",
            "Trimodal",
            "Overlapping Modes",
        ]
