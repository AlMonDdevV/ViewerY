#!/usr/bin/env python3

import subprocess
import platform
import psutil

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode().strip()
    except:
        return "Unknown"

def section(title):
    print("\n" + "=" * 12 + f" {title} " + "=" * 12)

def get_cpu():
    return run("grep -m 1 'model name' /proc/cpuinfo | cut -d ':' -f2").strip()

def get_gpu():
    nvidia = run("nvidia-smi --query-gpu=name --format=csv,noheader")
    if nvidia != "Unknown":
        return nvidia
    return run("lspci | grep -i vga | cut -d ':' -f3").strip()

def get_ram():
    mem = psutil.virtual_memory()
    return f"{round(mem.used/1e9,1)}GB / {round(mem.total/1e9,1)}GB"

def get_disk():
    disk = psutil.disk_usage("/")
    return f"{round(disk.used/1e9,1)}GB / {round(disk.total/1e9,1)}GB"

def get_uptime():
    return run("uptime -p")

def get_distro():
    try:
        return open("/etc/os-release").read().split('=')[1].split('\n')[0].replace('"','')
    except:
        return "Unknown"

ascii_art = r"""
+=============================================+
|__     __ _                           __   __|
|\ \   / /(_)  ___ __      __ ___  _ __\ \ / /|
| \ \ / / | | / _ \\ \ /\ / // _ \| '__|\ V / |
|  \ V /  | ||  __/ \ V  V /|  __/| |    | |  |
|   \_/   |_| \___|  \_/\_/  \___||_|    |_|  |
+=============================================+
"""

def main():
    print(ascii_art)
    print("ViewerY System Info")

    section("SYSTEM")
    print(f"OS      : {get_distro()}")
    print(f"Kernel  : {platform.release()}")
    print(f"Uptime  : {get_uptime()}")

    section("CPU")
    print(get_cpu())

    section("GPU")
    print(get_gpu())

    section("MEMORY")
    print(get_ram())

    section("DISK")
    print(get_disk())

if __name__ == "__main__":
    main()
