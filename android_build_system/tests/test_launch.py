import pytest
import mock

from android_build_system.tasks.launch import ensure_has_apk


class TestEnsureHasApk():

    def test_has(self):
        with mock.patch("android_build_system.tasks.launch.os.path.isfile",
                        new=mock.Mock(return_value=True)):
            ensure_has_apk()

    def test_not_have(self):
        with mock.patch("android_build_system.tasks.launch.os.path.isfile",
                        new=mock.Mock(return_value=False)):
            with pytest.raises(SystemExit):
                ensure_has_apk()
