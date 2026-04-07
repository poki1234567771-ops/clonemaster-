[app]
title = clonemaster-
package.name = clonemaster
package.domain = org.clonemaster

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0

# Kivy 2.1.0 أكثر استقراراً مع buildozer 1.5
requirements = python3,kivy==2.1.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
