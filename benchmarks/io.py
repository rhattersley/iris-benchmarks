import iris
import iris.fileformats.pp


class PP(object):
    def time_load_small(self):
        iris.load('/data/local/dataZoo/PP/aPPglob1/global.pp')

    def time_load_colpex(self):
        iris.load('/data/local/dataZoo/PP/COLPEX/theta_and_orog.pp')

    def time_load_fields_colpex(self):
        iris.fileformats.pp.load(
            '/data/local/dataZoo/PP/COLPEX/theta_and_orog.pp')


class FFLoad(object):
    def time_ukv(self):
        iris.load('/data/local/dataZoo/Fields/ukvop/qwqv00.T+0')
