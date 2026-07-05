[app]

# ---------------------------------
# App
# ---------------------------------
title = MaCuz
package.name = macuz
package.domain = org.macuz

version = 1.0.0

# ---------------------------------
# Source
# ---------------------------------
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,ttf
source.exclude_dirs = .git,.github,__pycache__,.venv,venv,build,bin
source.exclude_patterns = *.pyc,*.pyo

# ---------------------------------
# Requirements
# ---------------------------------
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,plyer

# ---------------------------------
# Screen
# ---------------------------------
orientation = portrait
fullscreen = 0

# ---------------------------------
# Android
# ---------------------------------
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

android.permissions = INTERNET

android.accept_sdk_license = True
android.enable_androidx = True

# ---------------------------------
# Bootstrap
# ---------------------------------
p4a.bootstrap = sdl2

# ---------------------------------
# Logging
# ---------------------------------
log_level = 2

# ---------------------------------
# Buildozer
# ---------------------------------
[buildozer]

warn_on_root = 0