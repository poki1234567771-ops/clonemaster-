[app]
title = clonemaster-
package.name = clonemaster
package.domain = org.clonemaster

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0

requirements = python3,kivy==2.2.1,kivymd,pillow

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
android.archs = arm64-v8a

# تفعيل قبول الترخيص تلقائياً
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
