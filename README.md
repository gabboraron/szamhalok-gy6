# GY6
## Mininet

> tetszőleges mennyiségő `host`ot, `switch`et, `router`t lehet beállítani amiben kapunk egy virtuális hálózatot

- virtuális gép
- `networks` a jelszó
- `home/miniedit.py`
- `OVS switch`et át kell írni `linux bridge-é`
- `sudo` joggal kell futatni a generált python fájlokat
- `tcpdump -i any` így az összes interfacet tcp dumpoljuk.
- `sh prctl show macs`

Python debug: `pdb lib` ammihez a `pdp settrace` el tudunk hozzányúlni.
