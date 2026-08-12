import numpy as np
import pandas as pd


class CategoricalNominalDataset:

    def __init__(self, seed=42):

        rng = np.random.default_rng(seed)

        # =====================================================
        # Categories
        # =====================================================

        values = rng.choice(
            [
                "Tehran",
                "Tabriz",
                "Mashhad",
                "Isfahan",
                "Shiraz",
                "Rasht",
                "Ahvaz",
                "Qom",
                "Yazd",
                "Kerman",
                "Borujerd",
                "Arak",
            ],
            size=100,
            p=[
                0.25,
                0.15,
                0.12,
                0.10,
                0.08,
                0.06,
                0.05,
                0.04,
                0.03,
                0.02,
                0.08,
                0.02,
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

        self.data = pd.DataFrame({"city": values})

        # =====================================================
        # Columns
        # =====================================================

        self.columns = [self.data["city"]]

        # =====================================================
        # Titles
        # =====================================================

        self.titles = ["City"]
