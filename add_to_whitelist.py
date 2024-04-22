import wmi
import json
import os

# Beyaz listeyi temsil eden JSON dosyası
whitelist_file = "whitelist.json"

# Beyaz listeyi yüklemek için fonksiyon
def load_whitelist():
    if os.path.exists(whitelist_file):
        with open(whitelist_file, "r") as f:
            return set(json.load(f))
    else:
        return set()

# Beyaz listeyi kaydetmek için fonksiyon
def save_whitelist(whitelist):
    with open(whitelist_file, "w") as f:
        json.dump(list(whitelist), f)

# Beyaz listeye yeni bir cihaz eklemek için fonksiyon
def add_to_whitelist(device_id):
    whitelist = load_whitelist()
    whitelist.add(device_id)
    save_whitelist(whitelist)
    print(f"{device_id} beyaz listeye eklendi.")

# Beyaz listeden bir cihazı kaldırmak için fonksiyon
def remove_from_whitelist(device_id):
    whitelist = load_whitelist()
    if device_id in whitelist:
        whitelist.remove(device_id)
        save_whitelist(whitelist)
        print(f"{device_id} beyaz listeden kaldırıldı.")
    else:
        print(f"{device_id} beyaz listede bulunamadı.")

# Mevcut USB cihazlarını listelemek için fonksiyon
def list_usb_devices():
    c = wmi.WMI()
    devices = []
    for usb in c.Win32_USBHub():
        devices.append(usb.DeviceID)
    return devices

# Takılı USB cihazlarını beyaz listeye eklemek için fonksiyon
def add_connected_usb_to_whitelist():
    devices = list_usb_devices()
    if not devices:
        print("Hiçbir USB cihazı takılı değil.")
        return

    print("Şu anda takılı olan USB cihazları:")
    for idx, device in enumerate(devices, 1):
        print(f"{idx}. {device}")

    try:
        choice = int(input("Beyaz listeye eklemek için bir cihaz seçin (sayı girin): "))
        if 1 <= choice <= len(devices):
            selected_device = devices[choice - 1]
            add_to_whitelist(selected_device)
        else:
            print("Geçersiz seçim.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

# Takılı USB cihazlarını beyaz listeden kaldırmak için fonksiyon
def remove_connected_usb_from_whitelist():
    devices = list_usb_devices()
    if not devices:
        print("Hiçbir USB cihazı takılı değil.")
        return

    print("Şu anda takılı olan USB cihazları:")
    for idx, device in enumerate(devices, 1):
        print(f"{idx}. {device}")

    try:
        choice = int(input("Beyaz listeden kaldırmak için bir cihaz seçin (sayı girin): "))
        if 1 <= choice <= len(devices):
            selected_device = devices[choice - 1]
            remove_from_whitelist(selected_device)
        else:
            print("Geçersiz seçim.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

# CLI ile kullanıcıya seçenekler sunmak için örnek
if __name__ == "__main__":
    while True:
        print("\n1. Mevcut USB cihazlarını listele ve beyaz listeye ekle")
        print("2. Mevcut USB cihazlarını listele ve beyaz listeden kaldır")
        print("3. Beyaz listeyi görüntüle")
        print("4. Çıkış")
        choice = input("Bir seçim yapın: ")

        if choice == "1":
            add_connected_usb_to_whitelist()
        elif choice == "2":
            remove_connected_usb_from_whitelist()
        elif choice == "3":
            whitelist = load_whitelist()
            print("Beyaz liste:", whitelist)
        elif choice == "4":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
