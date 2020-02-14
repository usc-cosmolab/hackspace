import pytest
import numpy as np
import matplotlib
from ..analysis import model, residuals, objective, get_best_fit
from ..data import load_lya_data, plot_pk, get_data_transfer_function
from ..conf import lcdm_params

example_abg = (0.02, 6, -5)


def test_load_ly_data():
    data = load_lya_data()
    assert len(data.x) == len(data.y) == len(data.y_unc)
    for arr in (data.x, data.y, data.y_unc):
        assert np.isfinite(arr).all()


@pytest.mark.parametrize("params", [None, lcdm_params])
def test_plot_pk(params):
    fig = plot_pk(params=params)
    assert isinstance(fig, matplotlib.figure.Figure)


def test_model():
    assert np.isfinite(model(10, *example_abg))


def test_residuals():
    data = load_lya_data()
    resid = residuals(example_abg, data)
    assert np.isfinite(resid).all()


def test_objective():
    data = load_lya_data()
    value = objective(example_abg, data)
    assert np.size(value) == 1
    assert np.isfinite(value)


def test_get_best_fit():
    for x in get_best_fit():
        assert np.isfinite(x)
