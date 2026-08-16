import pandas as pd

from .plots.analytical import (
    HistogramPlot,
    BoxPlot,
    ViolinPlot,
    CDFPlot,
    DensityPlot,
    FeatureTypePlot,
    FrequencyPlot,
    MissingValuePlot,
    QQPlot,
    TransformationPlot,
    BinningPlot,
)


class NumericalContinuousAnalytical:
    def __init__(self, column: pd.Series):
        self.column = column

    def help(self):

        column = self.column.dropna()

        unique_count = column.nunique()
        total_count = len(column)

        # =====================================================
        # Feature Type Detection
        # =====================================================

        if total_count == 0:

            feature_type = "Empty Numerical Feature"

        elif unique_count <= 10:

            feature_type = "Categorical Numerical Feature"

        elif (column.astype(int) == column).all():

            feature_type = "Discrete Numerical Feature"

        else:

            feature_type = "Continuous Numerical Feature"

        # =====================================================
        # Help
        # =====================================================

        print("=" * 60)

        print(f"Feature: {self.column.name}")
        print(f"Type:    {feature_type}")

        print("=" * 60)

        # =====================================================
        # Empty
        # =====================================================

        if feature_type == "Empty Numerical Feature":
            print("\nNo analysis methods are available.")
            return

        # =====================================================
        # Categorical Numerical
        # =====================================================

        if feature_type == "Categorical Numerical Feature":

            print("\nStatistics:")
            print("  ✓ general_information()")
            print("  ✓ value_range()")
            print("  ✓ central_tendency()")
            print("  ✓ dispersion()")
            print("  ✓ percentiles()")
            print("  ✓ outliers()")
            print("  ✓ data_quality()")

            print("\nCharts:")
            print("  ✓ frequency()")
            print("  ✓ missing_value()")
            print("  ✓ feature_type()")

        # =====================================================
        # Discrete Numerical
        # =====================================================

        elif feature_type == "Discrete Numerical Feature":

            print("\nStatistics:")
            print("  ✓ general_information()")
            print("  ✓ value_range()")
            print("  ✓ central_tendency()")
            print("  ✓ dispersion()")
            print("  ✓ distribution()")
            print("  ✓ percentiles()")
            print("  ✓ outliers()")
            print("  ✓ data_quality()")

            print("\nCharts:")
            print("  ✓ frequency()")
            print("  ✓ histogram()")
            print("  ✓ box()")
            print("  ✓ cdf()")
            print("  ✓ binning()")
            print("  ✓ missing_value()")
            print("  ✓ feature_type()")

        # =====================================================
        # Continuous Numerical
        # =====================================================

        elif feature_type == "Continuous Numerical Feature":

            print("\nStatistics:")
            print("  ✓ general_information()")
            print("  ✓ value_range()")
            print("  ✓ central_tendency()")
            print("  ✓ dispersion()")
            print("  ✓ distribution()")
            print("  ✓ percentiles()")
            print("  ✓ outliers()")
            print("  ✓ data_quality()")

            print("\nCharts:")
            print("  ✓ histogram()")
            print("  ✓ box()")
            print("  ✓ cdf()")
            print("  ✓ density()")
            print("  ✓ qq_plot()")
            print("  ✓ binning()")
            print("  ✓ transformation()")
            print("  ✓ missing_value()")
            print("  ✓ feature_type()")

        print("\n" + "=" * 60)

    def histogram_plot(self, bins=15):
        return HistogramPlot(column=self.column).draw(bins=bins)

    def box_plot(self):
        return BoxPlot(column=self.column).draw()

    def violin_plot(self):
        return ViolinPlot(column=self.column).draw()

    def cdf_plot(self):
        return CDFPlot(column=self.column).draw()

    def density_plot(self):
        return DensityPlot(column=self.column).draw()

    def feature_type_plot(self):
        return FeatureTypePlot(column=self.column).draw()

    def frequency_plot(self):
        return FrequencyPlot(column=self.column).draw()

    def missing_value_plot(self):
        return MissingValuePlot(column=self.column).draw()

    def qq_plot_plot(self):
        return QQPlot(column=self.column).draw()

    def transformation_plot(self):
        return TransformationPlot(column=self.column).draw()

    def binning_plot(self, bins=10):
        return BinningPlot(column=self.column, bins=bins).draw()
