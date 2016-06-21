* For users:

    * This tool is a command line for creating, compiling, packaging and launching android app
    
    * Prerequisites:
    
        * Android SDK installed
            You can get them from https://developer.android.com/studio/index.html#downloads
            You don't need to install Android Studio, "Get just the command line tools"
            After installation, please set ANDROID_HOME as system environment, it should be
            the root dir of the command line tools folder
            
        * Install additional tools from Android SDK manager
            - You can find the command "android" under ANDROID_HOME/tools
            - launch "android"
            - make sure you have "Build-tools" and platform-tools installed
            - select some system images to install and make sure 'android list target' is not empty
            
        * JDK is installed
            You can get them via https://java.com/en/download/
            After installation, please make sure the bin folder is in system path, you can do a
            'java' to check that
            
        * Python 33 is installed
            - You can get it via https://www.python.org/downloads/release/python-335/
            - Add the installation folder to system path, you can test by type 
               python
            - Add the installation_folder/scripts to system path
            - You are also recommended to install virtualenv
            
    * Install this tool
    
        - Run the following command from this folder:
            PYTHON33_BIN setup.py install (PYTHON33_BIN is the python binary you installed)
        - if you put PYTHON33_INSTALLATION_PATH/scripts in system path or you are using virtualenv, you can now run
            abs
        - otherwise, you should run PYTHON33_INSTALLATION_PATH/scripts/abs


* For Developers:

    - The tests are written with pytest, you should run
    - install all packages needed
        ```
        pip install -r requirement.txt
        ```
    - Run unit tests
        ```
        python33 -m pytest android_build_system/tests/
        ```