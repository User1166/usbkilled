import wmi
import time
import json
from datetime import datetime
from funct import cikarildi, eklendi, izin_verilen

# Beyaz listeyi temsil eden JSON dosyası
whitelist_file = "whitelist.json"

# Beyaz listeyi yüklemek için fonksiyon
def load_whitelist():
    with open(whitelist_file, "r") as f:
        return set(json.load(f))

# USB cihazlarının izlenmesi ve beyaz liste kontrolü
def monitor_usb_devices():
    c = wmi.WMI()

    # Mevcut USB cihazlarını al
    usb_devices = set()
    for usb in c.Win32_USBHub():
        usb_devices.add(usb.DeviceID)

    print("USB cihazları izleniyor...")

    # Beyaz liste kontrolü ve özel komut çalıştırmak için fonksiyon
    def run_custom_command_if_whitelisted(device_ids):
        whitelist = load_whitelist()
        if any(device in whitelist for device in device_ids):
            # Beyaz listede olan cihazlar için özel komut
            izin_verilen()  # Beyaz listede olan cihaz takıldığında çalışır
            print("Beyaz listede olan USB cihazı takıldı:", device_ids)
            return True  # Beyaz listeye uygun olduğu için diğer kontrolü atlar
        return False  # Beyaz listeye uygun değil

    # Log dosyasına olayları yazmak için fonksiyon
    def log_usb_event(event_type, device_ids):
        log_file = "log.txt"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as f:
            if event_type == "added":
                f.write(f"{timestamp} - USB cihazı eklendi: {device_ids}\n")
            elif event_type == "removed":
                f.write(f"{timestamp} - USB cihazı çıkarıldı: {device_ids}\n")

    try:
        while True:
            # Mevcut USB cihazlarını kontrol et
            current_usb_devices = set()
            for usb in c.Win32_USBHub():
                current_usb_devices.add(usb.DeviceID)

            # Cihaz değişikliklerini kontrol et
            if usb_devices != current_usb_devices:
                # Çıkarılan cihazlar
                removed = usb_devices - current_usb_devices
                if removed:
                    log_usb_event("removed", removed)  # Çıkarılan cihazları logla
                    if not run_custom_command_if_whitelisted(removed):
                        cikarildi()  # Beyaz listede değilse çalışır

                # Eklenen cihazlar
                added = current_usb_devices - usb_devices
                if added:
                    if not run_custom_command_if_whitelisted(added):
                        log_usb_event("added", added)  # Beyaz listede değilse logla ve eklenen() çalıştır
                        eklendi()

                # Cihaz listesini güncelle
                usb_devices = current_usb_devices

            time.sleep(2)  # İzleme aralığı

    except KeyboardInterrupt:
        print("İzleme sonlandırıldı.")

# Ana betiği çalıştırmak için fonksiyon
if __name__ == "__main__":
    monitor_usb_devices()
