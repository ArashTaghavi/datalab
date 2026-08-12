import numpy as np
import pandas as pd


class CategoricalOrdinalDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # Categories
        # =====================================================

        values = rng.choice(
            [
                "Very Poor",
                "Poor",
                "Below Average",
                "Average",
                "Above Average",
                "Good",
                "Very Good",
                "Excellent",
            ],
            size=100,
            p=[
                0.03,
                0.07,
                0.10,
                0.20,
                0.18,
                0.18,
                0.15,
                0.09,
            ],
        ).astype(object)

        # =====================================================
        # Missing Values
        # =====================================================

        missing_indices = rng.choice(100, size=8, replace=False)

        values[missing_indices] = np.nan

        # =====================================================
        # DataFrame
        # =====================================================

        self.data = pd.DataFrame({"satisfaction": values})

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [self.data["satisfaction"]]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = ["Satisfaction"]

        # =====================================================
        # Ordinal Order
        # =====================================================

        self.orders = [
            [
                "Very Poor",
                "Poor",
                "Below Average",
                "Average",
                "Above Average",
                "Good",
                "Very Good",
                "Excellent",
            ]
        ]
