[app]
# Nama dan paket aplikasi
title = Yt_dlp
package.name = ytdlpapp
package.domain = org.theneodev

# Direktori sumber dan ekstensi yang disertakan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Versi aplikasi
version = 0.1

# Persyaratan aplikasi (pastikan menambahkan yt_dlp)
requirements = python3,kivy,yt_dlp

# Izin-izin Android yang dibutuhkan
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# File entry point
entrypoint = main.py
