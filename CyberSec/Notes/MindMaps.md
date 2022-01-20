##
> KVM and Xen have a smaller attack surface and are known to have a better isolation model, but I'm sure there are still plenty of exploits given enough resources.

KVM - the low-level kernel-level hypervisor - has a tiny attack surface and has been audited exhaustively. It's unlikely to have critical bugs in it.

When people talk about "KVM vulnerabilities", they're usually talking about vulnerabilities in QEMU, which implements the actual device emulation. QEMU has all of the attack surface, deals with low-level data shuffling, and is written in C. Even worse, most stock QEMU-KVM deployments simply run qemu as root with no extra sandboxing or MAC like SELinux/sVirt. It's very likely that a bunch of 0days exist for those environments.

This is why many cloud providers use KVM-the-kernel-module, but an in-house replacement for QEMU.

Fortunately, there's a growing ecosystem of QEMU replacements written in Rust:

- https://github.com/cloud-hypervisor/cloud-hypervisor

- https://github.com/firecracker-microvm/firecracker

- https://chromium.googlesource.com/chromiumos/platform/crosvm... (the Chrome OS VM runtime which Firecracker was forked from)

Google's gVisor - the sandbox that App Engine and Cloud Run uses - uses KVM as well: https://gvisor.dev/docs/

With an emulation layer written in a language like Rust, the trust boundary is much better.

As for VirtualBox in particular - that one should not be considered a trust boundary. Nobody is seriously using it in production, and it's regularly featured in CTF competitions as a fun exploitation target. 

##
The domain must not contain certain strings; ```the check for these strings is implemented via hashes```, so at this time the domain names that are block-listed are unknown

##
These are websites that use top-level domains (TLDs) managed by Emercoin, a blockchain company. ```Records for these domains are stored inside a blockchain and cannot be transferred to anyone else without the domain owner's cryptographic signature.```

"Notably, JokerStash was one of the original proponents of moving dark web services to Blockchain technology."

##
```This is why PAAS rocks```

Your apps run inside smart containers in a fully managed runtime environment, ```we handle everything critical for production — configuration, orchestration, load balancing, failovers, logging, security, and more.```

https://www.heroku.com/

##
Perhaps the most effective means of preventing ransomware outbreaks is to ```implement application controls, which ensure only approved binaries are allowed to execute in the environment.```


##
