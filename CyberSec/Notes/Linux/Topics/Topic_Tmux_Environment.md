# PIN: See Notebook for more configs!


# Tmux cheat sheet

https://gist.github.com/henrik/1967800

# Tmux does network sockets as follows:

```
/// Create session
tmux -S /tmp/shareds new -s sharedsession
/// Change ownership to group
chgrp mutual_group_name /tmp/shareds
/// Run this in other user or ssh session to attach yourself
tmux -S /tmp/shareds attach -t sharedsession
```

Sessions are saved as actual files, kinda like named pipes

# Tmux Logging Plugin:
https://github.com/tmux-plugins/tmux-logging

--> This is a great way to save your work or at least keep track of it!

# Sample tmux config:
https://gist.github.com/faroit/ee545a2cec29f5fcc26edb6fe415cfe0

# my current tmux config file:

```
set-option -g prefix C-a
set -g mouse on
set-window-option -g window-size largest
# setw -g mouse on
```

all this does is change my prefix, sets mouse mode on and makes sure my largest windows size is always preserved.

# tmux window/pane commands

```
list-clients
list-sessions
list-windows
list-panes


-->Attach to session to duplicate windows:
attach-session -r -t "target session"
(r is optional, stands for read only)

-->remove all clients except yourself
detach-client -a -t {yourname}

split-window [-h]

select-layout 
--> even horizontal/vertical
--> main horizontal/vertical
--> tiled

-->capture contents of a pane to writeout to sdout
capture-pane -p -t {pane}

select-window -t {target window}

--> Make it so that if multiple sessions have different window sizes, the largest session with always have its size preserved:
set-window-option -t {target} window-size largest

```
 
# Copy text and write to file the easy way"

1) tmux a
2) ^b [
3) ^ space
4) move cursor with arrow keys and/or pageup/pagedown keys
5) ^ w
6) ^b ]
7) ^b:
8) save-buffer ~/out_file

Explanations:
2) enters copy mode
3) starts the selection
5) copies to buffer (0)
6) ends copy mode
7) enters tmux command line mode
8) use this command to save buffer (0) to file ~/out_file, specify with option [ -b buffer-index ] if needed, tmux command list-buffer will show the buffer list

# See all buffers and numbers:

C-b #

# or show a particular buffer
tmux show-buffer -b n

```
   show-buffer [-b buffer-name]
                   (alias: showb)
             Display the contents of the specified buffer.
```

# dump buffer n to file
tmux save-buffer -b n foo.txt
--> this doesn't seem to work on my box, so workaround:

```
tmux show-buffer [-b buffer-name] > output.txt

```

# Delete buffers:
--> one at a time

```
deleteb
```

--> All

```
deleteb -b *

```

# List Buffers

```
tmux list-buffers
```
