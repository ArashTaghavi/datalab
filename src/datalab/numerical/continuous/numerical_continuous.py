from .statistics import (
    NormalDistributionPlotStatistics,
    NormalBoxPlotStatistics,
    NormalViolinPlotStatistics,
    NormalCDFPlotStatistics,
    NormalQQPlotStatistics,
    NormalMeanStdStatistics,
)
from .plots.comparative import DistributionPlot, BoxPlot, ViolinPlot, CDFPlot, QQPlot, MeanStdPlot


class NumericalContinuous:
    def __init__(self, dataset) -> None:
        self.columns = dataset.columns
        self.titles = dataset.titles

    def distribution(self):
        DistributionPlot(columns=self.columns, titles=self.titles).draw()

        return NormalDistributionPlotStatistics(
            columns=self.columns, titles=self.titles
        ).statistics()

    def box_plot(self):
        BoxPlot(columns=self.columns, titles=self.titles).draw()

        return NormalBoxPlotStatistics(
            columns=self.columns, titles=self.titles
        ).statistics()

    def violin_plot(self):
        ViolinPlot(columns=self.columns, titles=self.titles).draw()

        return NormalViolinPlotStatistics(
            columns=self.columns, titles=self.titles
        ).statistics()

    def cdf_plot(self):
        CDFPlot(columns=self.columns, titles=self.titles).draw()

        return NormalCDFPlotStatistics(
            columns=self.columns, titles=self.titles
        ).statistics()

    def qq_plot(self):
        QQPlot(columns=self.columns, titles=self.titles).draw()

        return NormalQQPlotStatistics(
            columns=self.columns, titles=self.titles
        ).statistics()

    def mean_std_plot(self):
        MeanStdPlot(columns=self.columns, titles=self.titles).draw()

        return NormalMeanStdStatistics(
            columns=self.columns, titles=self.titles
        ).statistics()
