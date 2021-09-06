import pytest
from Configuration.ConfiTest import init_driver

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass