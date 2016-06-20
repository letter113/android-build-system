import os

import pytest

from android_build_system.utils import ensure_at_project_dir, get_configs


class TestUtils():

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

    def test_get_after_configs(self):
        os.chdir(os.path.join(self.helper, "mock-project-dir"))
        assert ["ls", "zip -h"] == get_configs("compile", "after")

    def test_get_empty_configs(self):
        os.chdir(os.path.join(self.helper, "mock-project-dir"))
        assert [] == get_configs("compile", "pre")

    def test_config_file_not_exist(self):
        os.chdir(os.path.join(self.helper, "mock-non-project-dir"))
        assert [] == get_configs("compile", "pre")