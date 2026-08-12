from ..core.plots import (
    CardinalityPlot,
    CountPlot,
    CumulativeFrequencyPlot,
    EntropyPlot,
    FrequencyPlot,
    LengthPlot,
    MissingValuePlot,
    ParetoPlot,
    PiePlot,
    RareCategoryPlot,
    TopCategoryPlot,
    TreemapPlot,
)


class CategoricalNominal:

    def __init__(self, dataset) -> None:
        self.columns = dataset.columns
        self.titles = dataset.titles

    def cardinality_plot(self):
        CardinalityPlot(columns=self.columns, titles=self.titles).draw()

    def count_plot(self):
        CountPlot(columns=self.columns, titles=self.titles).draw()

    def cumulative_frequency_plot(self):
        CumulativeFrequencyPlot(columns=self.columns, titles=self.titles).draw()

    def entropy_plot(self):
        EntropyPlot(columns=self.columns, titles=self.titles).draw()

    def frequency_plot(self):
        FrequencyPlot(columns=self.columns, titles=self.titles).draw()

    def length_plot(self):
        LengthPlot(columns=self.columns, titles=self.titles).draw()

    def missing_value_plot(self):
        MissingValuePlot(columns=self.columns, titles=self.titles).draw()

    def pareto_plot(self):
        ParetoPlot(columns=self.columns, titles=self.titles).draw()

    def pie_plot(self):
        PiePlot(columns=self.columns, titles=self.titles).draw()

    def rare_category_plot(self):
        RareCategoryPlot(columns=self.columns, titles=self.titles).draw()

    def top_category_plot(self):
        TopCategoryPlot(columns=self.columns, titles=self.titles).draw()

    def treemap_plot(self):
        TreemapPlot(columns=self.columns, titles=self.titles).draw()
