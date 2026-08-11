import numpy as np
import pandas as pd


class NoisyDistributionDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # Base Distribution
        # =====================================================

        base = rng.normal(
            loc=170,
            scale=8,
            size=1000
        )

        # =====================================================
        # 1. No Noise
        # =====================================================

        no_noise = pd.DataFrame({
            "value": base.copy()
        })

        # =====================================================
        # 2. Mild Noise
        # =====================================================

        mild_noise = pd.DataFrame({
            "value": base + rng.normal(
                loc=0,
                scale=1,
                size=1000
            )
        })

        # =====================================================
        # 3. Moderate Noise
        # =====================================================

        moderate_noise = pd.DataFrame({
            "value": base + rng.normal(
                loc=0,
                scale=4,
                size=1000
            )
        })

        # =====================================================
        # 4. Strong Noise
        # =====================================================

        strong_noise = pd.DataFrame({
            "value": base + rng.normal(
                loc=0,
                scale=8,
                size=1000
            )
        })

        # =====================================================
        # 5. Extreme Noise
        # =====================================================

        extreme_noise = pd.DataFrame({
            "value": base + rng.normal(
                loc=0,
                scale=16,
                size=1000
            )
        })

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [
            no_noise["value"],
            mild_noise["value"],
            moderate_noise["value"],
            strong_noise["value"],
            extreme_noise["value"],
        ]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = [
            "No Noise",
            "Mild Noise",
            "Moderate Noise",
            "Strong Noise",
            "Extreme Noise",
        ]