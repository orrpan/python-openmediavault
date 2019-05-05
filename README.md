# Python API for Openmediavault [![Build Status](https://travis-ci.org/orrpan/python-openmediavault.svg?branch=master)](https://travis-ci.org/orrpan/python-openmediavault)

Based on [python-synology](https://github.com/StaticCube/python-synology) by [FG van Zeelst StaticCube](https://github.com/StaticCube/)

-----
## Installation
```sh
git clone https://github.com/orrpan/python-openmediavault.git
cd python-openmediavault
[sudo] pip install setup.py
```
-----
## Usage

### Module
------

You can import the module as `Openmediavault`.

```python

from Openmediavault import Openmediavault

print("Creating Valid API")
api = Openmediavault("10.0.10.3", "443", "admin", "nunpam-fydRoh-ragho0", True)


print("=== Utilisation ===")
print("Hostname:   " + str(api.utilisation.hostname))
print("Uptime:     " + str(api.utilisation.up_time))
print("CPU Load:   " + str(api.utilisation.cpu_total_load) + " %")
print("CPU 1 min   " + str(api.utilisation.cpu_1min_load) + " %")
print("CPU 5 min   " + str(api.utilisation.cpu_5min_load) + " %")
print("CPU 15 min  " + str(api.utilisation.cpu_15min_load) + " %")
print("Memory Use: " + str(api.utilisation.memory_real_usage) + " %")


print("=== Storage ===")
volumes = api.storage.volumes
for volume in volumes:
    print("ID:          " + str(volume))
    print("Status:      " + str(api.storage.volume_status(volume)))
    print("Device type: " + str(api.storage.volume_device_type(volume)))
    print("Mounted:     " + str(api.storage._volume_mounted(volume)))
    print("Total size:  " + str(api.storage.volume_size_total(volume)))
    print("Used:        " + str(api.storage.volume_size_used(volume)))
    print("Used %:      " + str(api.storage.volume_percentage_used(volume))
          + "%")
    print("Temp avg     " + str(api.storage.volume_disk_temp_avg(volume)))
    print("Temp max     " + str(api.storage.volume_disk_temp_max(volume)))
    print("\n")

raids = api.storage.raids
for raid in raids:
    print("ID:          " + str(raid))
    print("raid name:   " + str(api.storage.raid_name(raid)))
    print("raid devices:" + str(api.storage.raid_devices(raid)))
    print("\n")

disks = api.storage.disks
for disk in disks:
    print("ID:          " + str(disk))
    print("Name:        " + str(api.storage.disk_name(disk)))
    print("S-Status:    " + str(api.storage.disk_smart_status(disk)))
    print("Temp:        " + str(api.storage.disk_temp(disk)))
    print("\n")

fans = api.health.fan
for fan in fans:
    print("ID           " + str(fan))
    print("Fan speed    " + str(api.health.fan_value(fan)))

temps = api.health.temp
for temp in temps:
    print("ID           " + str(temp))
    print("Temperature  " + str(api.health.temp_value(temp)))


api._logout()

```

## Credits / Special Thanks
- https://github.com/StaticCube (forked from)
- https://github.com/florianeinfalt
- https://github.com/tchellomello
