import os
import shutil

from android_build_system.pre_checks.base import BaseCheck
from android_build_system.config import AAPT, ZIPALIGN


class EnvCheck(BaseCheck):
    def __init__(self):
        super().__init__("Env check")

    def _check(self):
        return os.environ.get("ANDROID_HOME", None) is not None


class AAPTCheck(BaseCheck):
    def __init__(self):
        super().__init__("Binary 'aapt' found")

    def _check(self):
        return AAPT is not None


class ZIPALIGNCheck(BaseCheck):
    def __init__(self):
        super().__init__("Binary 'zipalgn' found")

    def _check(self):
        return ZIPALIGN is not None


class CmdCheck(BaseCheck):
    def __init__(self, cmd):
        self.cmd = cmd
        self.message = "Command '{}' found".format(cmd)

    def _check(self):
        return shutil.which(self.cmd) is not None