# test_mock_analyse.py
import analyse


def test_appel_regression_lineaire(mocker):
    fake_a, fake_b = 3.14, 1.59
    mock_reg = mocker.patch('analyse.regression_lineaire', return_value=(fake_a, fake_b))
    
    x = [1, 2, 3]
    y = [2, 4, 6]
    a, b = analyse.regression_lineaire(x, y)

    mock_reg.assert_called_once_with(x, y)

    assert a == fake_a
    assert b == fake_b