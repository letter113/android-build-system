import subprocess
import sys
import os
import json

from android_build_system.config import PROJECT_BUILD_CONFIG


def run_cmd(cmd, timeout=30, shell=False):
    print("##Running: ")
    print(" ".join(a for a in cmd))
    subprocess.call(cmd, timeout=timeout, shell=shell)


def ensure_at_project_dir():
    if not os.path.isfile("project.properties"):
        sys.exit("We could not locate project.properties, are you at the root of a project?")


def get_configs(task_name, pre_or_after):
    if not os.path.isfile(PROJECT_BUILD_CONFIG):
        print("Could not find {}, will skip".format(PROJECT_BUILD_CONFIG))
        return []

    with open(PROJECT_BUILD_CONFIG) as handler:
        configs = json.load(handler)
        return configs[task_name][pre_or_after]


def run_pre(task_name):
    for cmd in get_configs(task_name, "pre"):
        run_cmd(cmd, shell=True)


def run_after(task_name):
    for cmd in get_configs(task_name, "after"):
        run_cmd(cmd, shell=True)
