import sys


MODULE_NAMES = set(sys.modules.keys())


def time_import_iris():
    assert 'iris' not in sys.modules
    import iris
    teardown()


def teardown():
    names = sys.modules.keys()
    for name in names:
        if name not in MODULE_NAMES:
            del sys.modules[name]
