import sys

import pytest, mock

from android_build_system.tasks.project_creation import create_project, parse_args


def test_create_project_folder_exist():
    with mock.patch("os.path.exists", new=mock.Mock(return_value=True)):
        with pytest.raises(SystemExit):
            create_project("", "", "", "", "")


class TestArgParse():

    def setup_method(self, method):
        self.sysargv = sys.argv

    def teardown_method(self, method):
        sys.argv = self.sysargv

    def _test_missing(self):
        with pytest.raises(SystemExit):
            parse_args()

    def test_missing_name(self):
        sys.argv = "abs create -t 23 -p hellop -k com.p -a Hello".split()
        self._test_missing()

    def test_missing_target(self):
        sys.argv = "abs create -n hello -p hellop -k com.p -a Hello".split()
        self._test_missing()

    def test_missing_path(self):
        sys.argv = "abs create -n hello -k com.p -a Hello".split()
        self._test_missing()

    def test_missing_package(self):
        sys.argv = "abs create -n hello -t 23 -p hellop -a Hello".split()
        self._test_missing()

    def test_missing_package(self):
        sys.argv = "abs create -n hello -t 23 -p hellop -k com.p".split()
        self._test_missing()

    def test_whole(self):
         sys.argv = "abs create -n hello -t 23 -p hellop -k com.p -a Hello".split()
         parse_args()