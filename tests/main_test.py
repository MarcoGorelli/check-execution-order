import os

from check_execution_order import main


def test_main_bad(capsys):
    path = os.path.join('tests', 'data', 'bad.ipynb')
    ret = main((
        path,
    ))
    out, _ = capsys.readouterr()
    assert out == f'Cell 1 comes after 2 in file \'{path}\'\n'
    assert ret == 1


def test_main_good(capsys):
    path = os.path.join('tests', 'data', 'good.ipynb')
    ret = main((
        path,
    ))
    out, _ = capsys.readouterr()
    assert out == ''
    assert ret == 0


def test_main_arguable(capsys):
    '''Check that passes with strict=False and doesn't otherwise.'''
    path = os.path.join('tests', 'data', 'arguable.ipynb')
    ret = main((
        path,
    ))
    out, _ = capsys.readouterr()
    assert out == ''
    assert ret == 0
    ret = main(
        (
            path, '--strict',
        ),
    )
    out, _ = capsys.readouterr()
    assert out == f'Cell 3 comes after 1 in file \'{path}\'\n'
    assert ret == 1
