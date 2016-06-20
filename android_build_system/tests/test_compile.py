import os

import pytest, mock

from android_build_system.tasks.compile import (
    get_api_level,
    get_android_jar_path,
    _get_all_java_files
)


class TestGetApiLevel():

    @classmethod
    def setup_class(cls):
        cls.helper = os.path.join(os.path.dirname(__file__), "helpers")

    def setup_method(self, method):
        self._current_dir = os.getcwd()

    def teardown_method(self, method):
        os.chdir(self._current_dir)

    def test_get(self):
        os.chdir(os.path.join(self.helper, "mock-project-dir"))
        assert "23" == get_api_level()

    def test_file_broken(self):
        os.chdir(os.path.join(self.helper, "mock-broken-project-property"))
        with pytest.raises(Exception):
            get_api_level()


class TestGetAndroidJarPath:
    def test(self):
        with mock.patch("android_build_system.tasks.compile.get_api_level",
                          new=mock.Mock(return_value="7")):
            assert os.path.join(
                os.environ["ANDROID_HOME"], "platforms", "android-7", "android.jar"
            ) == get_android_jar_path()


class TestGetAllJavaFiles():
    @classmethod
    def setup_class(cls):
        cls.helper = os.path.join(os.path.dirname(__file__), "helpers")

    def setup_method(self, method):
        self._current_dir = os.getcwd()

    def teardown_method(self, method):
        os.chdir(self._current_dir)

    def test_get_files(self):
        os.chdir(os.path.join(self.helper, "mock-project-dir"))
        src_path = os.path.join(self.helper, "mock-project-dir", "src")
        found_files = _get_all_java_files()
        for java_file in [
            os.path.join(src_path, "ss", "sssss", "k.java"),
            os.path.join(src_path, "com", "p", "some.java"),
            os.path.join(src_path, "com", "p", "R.java"),
            os.path.join(src_path, "com", "p", "Hello.java")
        ]:
            assert java_file in found_files
        assert 4 == len(found_files)