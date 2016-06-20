import os

import pytest

from android_build_system.utils import ensure_at_project_dir


class TestEnsureAtProjectDir():

    @classmethod
    def setup_class(cls):
        cls.helper = os.path.join(os.path.dirname(__file__), "helpers")

    def setup_method(self, method):
        self._current_dir = os.getcwd()

    def teardown_method(self, method):
        os.chdir(self._current_dir)

    def test_at_project_dir(self):
        os.chdir(os.path.join(self.helper, "mock-project-dir"))
        ensure_at_project_dir()

    def test_not_at_project_dir(self):
        os.chdir(os.path.join(self.helper, "mock-non-project-dir"))
        with pytest.raises(SystemExit):
            ensure_at_project_dir()