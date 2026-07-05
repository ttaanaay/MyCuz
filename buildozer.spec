[app]

title = MaCuz
package.name = macuz
package.domain = org.macuz

version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,ttf
source.exclude_dirs = .git,.github,__pycache__,.venv,venv,build,bin
source.exclude_patterns = *.pyc,*.pyo

requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow==11.2.1,plyer==2.1.0

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 26b
android.archs = arm64-v8a

android.permissions = INTERNET

android.accept_sdk_license = True
android.enable_androidx = True

p4a.bootstrap = sdl2

log_level = 2

[buildozer]

warn_on_root = 0