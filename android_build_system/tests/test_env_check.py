import os

import mock

from android_build_system.pre_checks.env_check import EnvCheck, AAPTCheck, ZIPALIGNCheck, CmdCheck


class TestEnvCheck():

    def setup_method(self, method):
        self.saved_env = os.environ

    def teardown_method(self, method):
        os.environ = self.saved_env

    def test_has_android_home(self):
       os.environ = {"ANDROID_HOME": "some-path"}
       assert EnvCheck().check() is True

    def test_has_no_android_home(self):
        os.environ = {"NOT_ANDROID_HOME": "some-path"}
        assert EnvCheck().check() is None


class TestAAPTCheck():

    def test_not_have_aapt(self):
        with mock.patch("android_build_system.pre_checks.env_check.AAPT", new=None):
            assert AAPTCheck().check() is None

    def test_has_aapt(self):
        with mock.patch("android_build_system.pre_checks.env_check.AAPT", new="aapt"):
            assert AAPTCheck().check() is True


class TestZIPALIGNCheck():

    def test_not_have(self):
        with mock.patch("android_build_system.pre_checks.env_check.ZIPALIGN", new=None):
            assert ZIPALIGNCheck().check() is None

    def test_has(self):
        with mock.patch("android_build_system.pre_checks.env_check.ZIPALIGN", new="aapt"):
            assert ZIPALIGNCheck().check() is True


class TestCmdCheck():

    def test_cmd_valid(self):
        with mock.patch("android_build_system.pre_checks.env_check.shutil.which",
                        new=mock.Mock(return_value="some-path")):
            assert CmdCheck("cmd").check() is True

    def test_cmd_not_valid(self):
        with mock.patch("android_build_system.pre_checks.env_check.shutil.which",
                        new=mock.Mock(return_value=None)):
            assert CmdCheck("cmd").check() is None