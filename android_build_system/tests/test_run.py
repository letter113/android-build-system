import pytest
import mock

from android_build_system.run import pre_check


class TestPreCheck():

    @mock.patch("android_build_system.pre_checks.env_check.CmdCheck.check",
                new=mock.Mock(return_value=True))
    @mock.patch("android_build_system.pre_checks.env_check.EnvCheck.check",
                new=mock.Mock(return_value=True))
    @mock.patch("android_build_system.pre_checks.env_check.AAPTCheck.check",
                new=mock.Mock(return_value=True))
    @mock.patch("android_build_system.pre_checks.env_check.ZIPALIGNCheck.check",
                new=mock.Mock(return_value=True))
    def test_all_passed(self):
        pre_check()

    @mock.patch("android_build_system.pre_checks.env_check.EnvCheck.check",
                new=mock.Mock(return_value=False))
    @mock.patch("android_build_system.pre_checks.env_check.AAPTCheck.check",
                new=mock.Mock(return_value=True))
    @mock.patch("android_build_system.pre_checks.env_check.ZIPALIGNCheck.check",
                new=mock.Mock(return_value=True))
    @mock.patch("android_build_system.pre_checks.env_check.CmdCheck.check",
                new=mock.Mock(return_value=True))
    def test_failed(self):
        with pytest.raises(SystemExit):
            pre_check()
