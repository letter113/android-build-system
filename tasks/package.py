import subprocess
import os

from .compile import get_android_jar_path


APP_PATH = {
    "unsigned": os.path.join("bin", "unsigned.apk"),
    "signed": os.path.join("bin", "signed.apk"),
    "zippped": os.path.join("bin", "final.apk")
}


def run():
    keystore="AndroidTest.keystore"
    _create_keystore(keystore)

    for _, app in APP_PATH.items():
        os.remove(app)

    _create_apk()
    _sign_apk(keystore)
    _zip_align_apk()


def _create_keystore(keystore_path):
    if os.path.isfile(keystore_path):
        return
    print("Generating keystore now")
    subprocess.call(
        ["keytool",
         "-genkeypair",
         "-validity", "10000",
         "-dname", "CN=company name, OU=organisational unit, O=organisation, L=location, S=state, C=country code",
         "-keystore", keystore_path,
         "-storepass", "password",
         "-keypass", "password",
         "-alias", "AndroidTestKey",
         "-keyalg", "RSA",
         "-v"],
        timeout=30
    )


def _create_apk():
    subprocess.call([
        "aapt",
        "package",
        "-v",
        "-f",
        "-M", "AndroidManifest.xml",
        "-S", "res",
        "-I", get_android_jar_path(),
        "-F", APP_PATH["unsigned"],
        "bin"],
        timeout=30)


def _sign_apk(keystore):
    subprocess.call([
        "jarsigner",
        "-verbose",
        "-keystore", "AndroidTest.keystore",
        "-storepass", "password",
        "-keypass", "password",
        "-signedjar", APP_PATH["signed"],
        APP_PATH["unsigned"],
        "AndroidTestKey"],
        timeout=30
    )


def _zip_align_apk():
    subprocess.call([
        "zipalign",
        "-v",
        "-f", "4",
        APP_PATH["signed"],
        APP_PATH["zippped"]],
    timeout=30)