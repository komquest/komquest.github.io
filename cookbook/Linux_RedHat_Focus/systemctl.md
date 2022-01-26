# View services
```
systemctl | grep ".service" | vi -

```

# Change System Run level to 3, then back to 5

```
systemctl set-default multi-user.target
systemctl set-default graphical.target
```
