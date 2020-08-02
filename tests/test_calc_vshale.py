import petrophys
from math import isclose

from .utils import load_las, load_simple_data

class TestVShaleClass:
  def test_linear_simple(self):
    df = load_simple_data()
    vshale = petrophys.calc_vshale(df)

    assert isclose(vshale[400], 0, abs_tol=1e-4)
    assert isclose(vshale[400.5], 0.5, abs_tol=1e-4)
    assert isclose(vshale[401], 1, abs_tol=1e-4)


  def test_linear_las(self):
    df = load_las()
    vshale = petrophys.calc_vshale(df)

    assert isclose(vshale[500], 0.3872, abs_tol=1e-4)
    assert isclose(vshale[1000], 0.4217, abs_tol=1e-4)
    assert isclose(vshale[2000], 0.1484, abs_tol=1e-4)


  def test_larionov_older_simple(self):
    df = load_simple_data()
    vshale = petrophys.calc_vshale(df, method='larionov_older')

    assert isclose(vshale[400], 0, abs_tol=1e-4)
    assert isclose(vshale[400.5], 0.33, abs_tol=1e-4)
    assert isclose(vshale[401], 0.99, abs_tol=1e-4)


  def test_larionov_older_las(self):
    df = load_las()
    vshale = petrophys.calc_vshale(df, method='larionov_older')

    assert isclose(vshale[500], 0.2344, abs_tol=1e-4)
    assert isclose(vshale[1000], 0.2621, abs_tol=1e-4)
    assert isclose(vshale[2000], 0.0754, abs_tol=1e-4)


  def test_larionov_tertiary_simple(self):
    df = load_simple_data()
    vshale = petrophys.calc_vshale(df, method='larionov_tertiary')

    assert isclose(vshale[400], 0, abs_tol=1e-4)
    assert isclose(vshale[400.5], 0.2162, abs_tol=1e-4)
    assert isclose(vshale[401], 0.9957, abs_tol=1e-4)


  def test_larionov_tertiary_las(self):
    df = load_las()
    vshale = petrophys.calc_vshale(df, method='larionov_tertiary')

    assert isclose(vshale[500], 0.1410, abs_tol=1e-4)
    assert isclose(vshale[1000], 0.1618, abs_tol=1e-4)
    assert isclose(vshale[2000], 0.0384, abs_tol=1e-4)


  def test_steiber_simple(self):
    df = load_simple_data()
    vshale = petrophys.calc_vshale(df, method='steiber')

    assert isclose(vshale[400], 0, abs_tol=1e-4)
    assert isclose(vshale[400.5], 0.25, abs_tol=1e-4)
    assert isclose(vshale[401], 1, abs_tol=1e-4)


  def test_steiber_las(self):
    df = load_las()
    vshale = petrophys.calc_vshale(df, method='steiber')

    assert isclose(vshale[500], 0.1739, abs_tol=1e-4)
    assert isclose(vshale[1000], 0.1955, abs_tol=1e-4)
    assert isclose(vshale[2000], 0.0549, abs_tol=1e-4)


  def test_clavier_simple(self):
    df = load_simple_data()
    vshale = petrophys.calc_vshale(df, method='clavier')

    assert isclose(vshale[400], 0, abs_tol=1e-4)
    assert isclose(vshale[400.5], 0.3072, abs_tol=1e-4)
    assert isclose(vshale[401], 1, abs_tol=1e-4)


  def test_clavier_las(self):
    df = load_las()
    vshale = petrophys.calc_vshale(df, method='clavier')

    assert isclose(vshale[500], 0.2174, abs_tol=1e-4)
    assert isclose(vshale[1000], 0.2434, abs_tol=1e-4)
    assert isclose(vshale[2000], 0.0690, abs_tol=1e-4)
