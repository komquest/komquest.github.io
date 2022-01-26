## Get user namd and sid

```
wmic useraccount get name,sid
```

## Enmurate Installed Applications (Registry Installed)

```
wmic product get name, version, vendor
```

## Enmuate Hotfixes:

```
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

## Get Service start mode

```
wmic service where caption="Serviio" get name,caption,state,startmode
```