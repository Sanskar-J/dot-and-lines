[app]

# (str) Title of your application
title = Dots and Boxes

# (str) Package name
package.name = dotsandboxes

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (source.dir) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pillow

# (str) Supported orientations
# Valid values: landscape, sensorLandscape, portrait or sensorPortrait
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_SERVICE [,NAME2:ENTRY_TO_SERVICE2] [...]

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of 'red', 'blue', 'green', 'black', 'white', 'gray', 'cyan', 'magenta', 'yellow', 'lightgray', 'darkgray', 'lightgrey', 'darkgrey', 'aqua', 'fuchsia', 'lime', 'maroon', 'navy', 'olive', 'purple', 'silver', 'teal'.
android.presplash_bgcolor = #FFFFFF

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 30

# (str) Android NDK version to use
#android.ndk = 25c

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android app theme, default is ok for Kivy-based app
# android.theme = "@android:style/Theme.NoTitleBar"

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a,armeabi-v7a

# (int) overrides automatic versionCode generation
# android.version_code = 1

# (list) pattern matched against the intent filters possible actions
# android.actions = MAIN

# (list) List of service to declare
#android.services = NAME:ENTRYPOINT_TO_SERVICE [,NAME2:ENTRY_TO_SERVICE2] [...]

# (bool) allows AndroidManifest.xml generation without INTERNET permission,
# android.allow_backup = True

# (str) XML for custom backup agent. Check [here](https://developer.android.com/guide/topics/data/backup) for more info.
# android.backup_agent = MyBackupAgent

# (str) XML to override permissions manifest generation
# android.manifest_additions =

# (str) XML to override res/xml/config.xml `<domain-config>` generation.
# android.domain_config_additions =

# (bool) Indicate if the application should be fullscreen or not
# android.fullscreen = True

# (str) Presplash message
android.presplash = Dots and Boxes

# (str) Icon and presplash for the Android app are not include in the template by default.
# Place your android icon inside your source directory named ic_launcher.png.
# The Android launcher icon is generically named ``ic_launcher.png``, but we seek O.png files too.

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

#
# Python for android (p4a) specific
#

# (str) python for android API level to use
#p4a.api = 31

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port = 5000

#
# tests
#
#android.junit_install_dir = .buildozer/android/platform/build-<arch>/build/outputs/apk

#
# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
# android.port = 5000

# Control passing the --useLegacyTooling flag to Android's apkbuilder
# android.release_artifact = apk

#
# iOS specific
#

# (bool) Whether or not to sign the code
ios.codesign_allowed = False
