from abc import ABC, abstractmethod


class Plot(ABC):

    @abstractmethod
    def draw(self):
        pass
