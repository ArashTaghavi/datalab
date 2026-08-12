from .statistics import DiscreteStatistics
from .plots import HistogramPlot, DotPlot, FrequencyPlot


class NumericalDiscrete:
    def __init__(self, dataset) -> None:
        self.columns = dataset.columns
        self.titles = dataset.titles

    def histogram(self):
        HistogramPlot(columns=self.columns, titles=self.titles).draw()

        return DiscreteStatistics(columns=self.columns, titles=self.titles).statistics()

    def dot_plot(self):
        DotPlot(columns=self.columns, titles=self.titles).draw()

    def frequency_plot(self):
        FrequencyPlot(columns=self.columns, titles=self.titles).draw()
