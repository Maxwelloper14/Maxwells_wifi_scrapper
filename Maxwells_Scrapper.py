import subprocess
import os

def scan_wifi_networks():
    print("Сканирование ближайших Wi-Fi сетей...")
    result = subprocess.run(['netsh', 'wlan', 'show', 'network'], capture_output=True, text=True)
    networks = result.stdout
    print(networks)

def show_connected_devices():
    print("Список подключенных устройств...")
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    devices = result.stdout
    print(devices)

def main():
    scan_wifi_networks()
    show_connected_devices()

