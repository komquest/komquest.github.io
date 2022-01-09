# Start vim with certain Vars Enabled:

```
vim -c "set hlsearch" -c "set wrap" -c "set mouse=a" -c "set syntax=pcap
```
# Enable Paste:

```
:set paste

```

# Parse JSON from stdinput

``` 
:%!jq .
:set syntax=json
```

# Select Line or Lines
Just insert capital V

# Copy lines

```
[n]yy LINE
p
```

# Display Line Numbers and scroll to end of file
```
set number
:$
```

# Disable line numbers/enable:

```
set number
set number!
```

# Insert Mode Commands:
```
Ctrl-J = New line
Ctrl-U = Delete Current line
Ctrl-W = Delete Word before Curser 
Ctrl-T/D = Insert or delete shift width (tab) to a line
Ctrl-V = Insert Non-Digit Character (use u{hex} to insert any hex value)
Ctrl-E/Y = Insert text below/above cursor
Ctrl-O = Insert Command, then go back to insert mode
```

# Enable Mouse Interaction (xterm or gui)
```
:set mouse=a
:set mouse=
```

# Vimrc Basic File:

```
colorscheme desert
set wrap!
syntax enable
set nohlsearch
set mouse=a
```


```
set hls
set ic
set is
set nu
set noswf
```

# Show whitespaces
```
set list
set nolist
```

# Find and Replace
```
:%s/unix/linux/g
```
