import numpy as np
import pandas as pd


class UniformDistributionDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # 1. Narrow Uniform
        # =====================================================

        narrow_uniform = pd.DataFrame(
            {"value": rng.uniform(low=160, high=180, size=1000)}
        )

        # =====================================================
        # 2. Moderate Uniform
        # =====================================================

        moderate_uniform = pd.DataFrame(
            {"value": rng.uniform(low=150, high=190, size=1000)}
        )

        # =====================================================
        # 3. Wide Uniform
        # =====================================================

        wide_uniform = pd.DataFrame(
            {"value": rng.uniform(low=130, high=210, size=1000)}
        )

        # =====================================================
        # 4. Very Wide Uniform
        # =====================================================

        very_wide_uniform = pd.DataFrame(
            {"value": rng.uniform(low=100, high=240, size=1000)}
        )

        # =====================================================
        # 5. Shifted Uniform
        # =====================================================

        shifted_uniform = pd.DataFrame(
            {"value": rng.uniform(low=180, high=220, size=1000)}
        )

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [
            narrow_uniform["value"],
            moderate_uniform["value"],
            wide_uniform["value"],
            very_wide_uniform["value"],
            shifted_uniform["value"],
        ]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = [
            "Narrow Uniform",
            "Moderate Uniform",
            "Wide Uniform",
            "Very Wide Uniform",
            "Shifted Uniform",
        ]
