import pytest

import rad

import numpy as np


def test_unit_length_of_angles():
    N_angles = 8
    quad = rad.quadrature(N_angles)

    assert quad.angles.size == N_angles


def test_negative_quadrature_error():
    #

    with pytest.raises(ValueError, match="degree must be a positive integer"):
        rad.quadrature(-2)


def test_normalization():
    N = 10

    x = np.random.random(10)
    quad = rad.quadrature(2)
    x = quad.normalization(x)

    # using all close cus these are floats!
    assert np.allclose(np.sum(x), 1.0)


if __name__ == "__main__":
    test_normalization()
    test_negative_quadrature_error()
