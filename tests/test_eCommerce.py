import unittest

import pytest

from pages.Search import Search
from tests.conftest import veg


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class SearchTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classofObjects(self):
        self.vg = Search(self.driver)

    @pytest.mark.run(order=1)
    def test_vegSearch(self):
        self.vg.searchGreen(self.veg)
