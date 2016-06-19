import argparse
import subprocess
import sys
import os


def create_project(project_name, target_id, project_path, package_name, activity_class_name):
    subprocess.call([os.path.join(os.environ["ANDROID_HOME"], "tools", "android"),
                     "create",
                     "project",
                     "-n",
                     project_name,
                     "-t",
                     str(target_id),
                     "-p",
                     project_path,
                    "-k",
                    package_name,
                     "-a",
                     activity_class_name
                     ],
                    timeout=30)
    os.mkdir(os.path.join(project_path, "obj"))


def parse_args():
    parser = argparse.ArgumentParser(description='Process create project arguments.')
    parser.add_argument('--name', "-n",
                        dest='project_name',
                        required=True,
                        help='The name of your android project')
    parser.add_argument("--target", "-t",
                        dest='target_id',
                        required=True,
                        help="The target id, use android list target to get available ones")
    parser.add_argument("--path", "-p",
                        dest="project_path",
                        required=True,
                        help="The path of your project")
    parser.add_argument("--package", "-k",
                        dest="package_name",
                        required=True,
                        help="The package name")
    parser.add_argument("--activity", "-a",
                        dest="activity",
                        required=True,
                        help="Name of the default Activity that is created.")

    return parser.parse_args(sys.argv[2:])


def run():
    args = parse_args()
    create_project(args.project_name,
                   args.target_id,
                   args.project_path,
                   args.package_name,
                   args.activity)