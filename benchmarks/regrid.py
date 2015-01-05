from iris.experimental.regrid import (
    regrid_bilinear_rectilinear_src_and_grid,
    regrid_area_weighted_rectilinear_src_and_grid)


# Small cube regridding
def yx_cube(shape):
    import iris.coord_systems
    import iris.coords
    import iris.cube
    import numpy as np

    cube = iris.cube.Cube(np.arange(np.prod(shape),
                                    dtype=np.float32).reshape(shape))

    cs = iris.coord_systems.GeogCS(6371229)
    coord = iris.coords.DimCoord(points=np.linspace(-65, 65, shape[0]),
                                 standard_name='latitude',
                                 units='degrees',
                                 coord_system=cs)
    coord.guess_bounds()
    cube.add_dim_coord(coord, 0)
    coord = iris.coords.DimCoord(points=np.linspace(-140, 140, shape[1]),
                                 standard_name='longitude',
                                 units='degrees',
                                 coord_system=cs)
    coord.guess_bounds()
    cube.add_dim_coord(coord, 1)
    return cube


CUBE_2D_145x192 = yx_cube((145, 192))  # N96
CUBE_2D_325x432 = yx_cube((325, 432))  # N216
CUBE_2D_2160x4320 = yx_cube((2160, 4320))


def time_bilinear_325x432_to_145x196():
    regrid_bilinear_rectilinear_src_and_grid(CUBE_2D_325x432, CUBE_2D_145x192)


def time_area_weighted_325x432_to_145x192():
    regrid_area_weighted_rectilinear_src_and_grid(CUBE_2D_325x432,
                                                  CUBE_2D_145x192)

time_area_weighted_325x432_to_145x192.number = 1
time_area_weighted_325x432_to_145x192.repeat = 1
