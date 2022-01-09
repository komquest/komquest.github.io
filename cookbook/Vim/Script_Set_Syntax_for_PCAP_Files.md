# Note These scripts only work if the pcap file uses the "-A" flag

# New Version
--> Create a file in "~/.vim/syntax/pcap.vim

```
"set syntax=pcap
""06:04:26.229664

syn match pcapTime "[0-2][0-9]:[0-6][0-9]:[0-6][0-9].*$"

if version >= 508 || !exists("did_abc_syn_inits")
  if version < 508
    let did_abc_syn_inits = 1
    command -nargs=+ HiLink hi link <args>
  else
    command -nargs=+ HiLink hi def link <args>
  endif

  HiLink pcapTime        Type

  delcommand HiLink
endif

let b:current_syntax = "pcap"
```

