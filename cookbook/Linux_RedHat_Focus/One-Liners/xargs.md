# Copy a certain amount of folders based off of number:

```
ls  -1  |  head  -5  |  xargs  -i  cp -r  '{}'  dest/folder/

ls  -1  |  tail -5  |  xargs  -i  cp -r  '{}'  dest/folder/
```
