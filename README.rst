pyplotutil
==========

Data parsing and plotting utility based on numpy and matplotlib.

Getting started
---------------

Data parser loads a plain text data file and creates an object that can
access to each label by its symbol. Figure maker make it easy to define
plot function.

.. code:: python

    import pyplotutil

    Data = pyplotutil.Data
    Figure = pyplotutil.Figure


    class SampleFigure(Figure):
        def __init__(data):
            self.data = data

        def x_plot(self):
            self.plot(self.data.t, self.data.x)

        def y_plot(self):
            self.plot(self.data.t, self.data.y)


    if __name__ == '__main__':
        data = Data('results.dat', labels=['t', 'x', 'y'])
        pyplotutil.main(data)

