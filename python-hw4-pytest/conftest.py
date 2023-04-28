def pytest_configure(config):
    config.addinivalue_line("markers", "arithmetic: mark test as arithmetic")
    config.addinivalue_line("markers", "strings: mark test as strings")




