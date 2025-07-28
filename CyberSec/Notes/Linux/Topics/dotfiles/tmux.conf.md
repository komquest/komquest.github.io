set-option -g display-panes-time 5000
set-option -g status-style 'bg=color0,fg=magenta'
set-option -g mouse on
set-option -g set-clipboard external 

set -g pane-border-style 'fg=yellow'
set -g pane-active-border-style 'fg=magenta'

#Make sure backspace works
set-option -g default-terminal "screen-256color"
set-option -ga terminal-overrides ',*:Tc'