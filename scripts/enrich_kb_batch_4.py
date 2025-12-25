#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knowledge Base Enrichment - Batch 4
Ajoute 15 nouvelles catégories (Networking, Virtualization, Development, Multimedia, System Management)
"""

import sys
import os

# Ajouter le chemin pour l'import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'v14_mvp'))

def add_batch_4_categories():
    """
    Ajoute 15 nouvelles catégories AVANT 'return kb' dans ai_knowledge_unified.py
    """

    batch_4_code = '''
        # =============================================================================
        # BATCH 4: NETWORKING, VIRTUALIZATION, DEVELOPMENT & MULTIMEDIA (15 catégories)
        # =============================================================================

        # NETWORKING_WIFI_OPTIMIZATION
        kb["networking_wifi_optimization"] = {
            "metadata": {
                "priority": 4,
                "tags": ["wifi", "networking", "performance", "optimization", "wireless"],
                "difficulty": "intermediate",
                "description": "WiFi channel optimization, band selection, driver tuning, interference reduction"
            },
            "tips": [
                {"content": "WiFi 6E (802.11ax): 6GHz band (160MHz channels), no legacy device interference, lower latency (<20ms), WPA3 only, requires WiFi 6E router + compatible device (2021+ laptops)", "keywords": ["wifi 6e", "6ghz", "802.11ax", "low latency"], "difficulty": "intermediate", "tags": ["wifi6e", "modern"], "related_tools": []},
                {"content": "2.4GHz vs 5GHz: 2.4GHz = longer range (penetrates walls), slower (300Mbps max), crowded (microwaves/bluetooth interfere), 5GHz = shorter range, faster (1300Mbps), less interference, use 5GHz if close to router", "keywords": ["2.4ghz", "5ghz", "band selection", "range"], "difficulty": "beginner", "tags": ["basics"], "related_tools": []},
                {"content": "Channel selection 2.4GHz: Use 1, 6, or 11 ONLY (non-overlapping), auto = bad (switches randomly), use WiFi Analyzer to find clearest channel, neighbors on 6 = you use 1 or 11", "keywords": ["channel", "2.4ghz", "1 6 11", "wifi analyzer"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": ["WiFi Analyzer", "inSSIDer"]},
                {"content": "Channel selection 5GHz: More channels (36-165), DFS channels (52-144) = auto-switch if radar detected, use 36/40/44/48 or 149-165 (non-DFS) for stable connection, 80/160MHz width for speed", "keywords": ["5ghz channels", "dfs", "channel width"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": ["WiFi Analyzer"]},
                {"content": "Channel width: 20MHz = stable/long range, 40MHz = 2x speed (2.4GHz max), 80MHz = 4x speed (5GHz recommended), 160MHz = 8x speed (WiFi 6/6E only, short range), wider = faster but shorter range", "keywords": ["channel width", "20mhz", "40mhz", "80mhz", "160mhz"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "WiFi driver updates: Intel WiFi (update via Intel Driver Support Assistant), Realtek (manufacturer website), Qualcomm/Broadcom (Windows Update or OEM site), new drivers fix drops/speed issues, rollback if unstable", "keywords": ["wifi driver", "intel", "realtek", "updates"], "difficulty": "beginner", "tags": ["drivers"], "related_tools": ["Intel Driver Assistant"]},
                {"content": "Router placement: Center of home, elevated (shelf/wall mount), away from metal/concrete, antennas vertical (horizontal devices) or 45° (mixed), avoid corners/closets, each wall = -5 to -10dBm signal loss", "keywords": ["router placement", "signal", "antenna", "positioning"], "difficulty": "beginner", "tags": ["basics"], "related_tools": []},
                {"content": "Interference sources: Microwave ovens (2.4GHz killer, -20dBm drop), Bluetooth (2.4GHz, minor), baby monitors, cordless phones, neighbors' WiFi (overlap), USB 3.0 devices (2.4GHz interference), switch to 5GHz if affected", "keywords": ["interference", "microwave", "bluetooth", "usb3"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "Power management: Windows Device Manager > Network Adapter > Power Management > UNCHECK 'Allow computer to turn off device' (prevents drops), 'Allow wake' OK, laptops may re-enable on updates", "keywords": ["power management", "wifi drops", "device manager"], "difficulty": "intermediate", "tags": ["windows", "stability"], "related_tools": []},
                {"content": "QoS (Quality of Service): Router setting, prioritize gaming/video traffic, WMM (WiFi Multimedia) enable, set gaming device MAC to high priority, reduces lag spikes but NOT bandwidth bottleneck fix", "keywords": ["qos", "wmm", "priority", "gaming"], "difficulty": "intermediate", "tags": ["gaming"], "related_tools": []},
                {"content": "Mesh WiFi vs repeaters: Mesh (Google WiFi, Eero, Deco) = seamless roaming, single SSID, wired backhaul best, repeaters = half speed (re-transmit), different SSID, cheap but laggy, mesh for whole-home coverage", "keywords": ["mesh wifi", "repeaters", "coverage", "backhaul"], "difficulty": "intermediate", "tags": ["mesh"], "related_tools": []},
                {"content": "WiFi 6 (802.11ax) features: OFDMA (multiple devices simultaneously), MU-MIMO 8x8, Target Wake Time (battery saving), 1024-QAM (faster speed), backward compatible, benefits in crowded networks (apartments)", "keywords": ["wifi 6", "802.11ax", "ofdma", "mu-mimo"], "difficulty": "advanced", "tags": ["wifi6", "modern"], "related_tools": []}
            ]
        }

        # NETWORKING_VPN_PROTOCOLS
        kb["networking_vpn_protocols"] = {
            "metadata": {
                "priority": 4,
                "tags": ["vpn", "security", "privacy", "networking", "encryption"],
                "difficulty": "intermediate",
                "description": "VPN protocols comparison: WireGuard, OpenVPN, IPSec, split tunneling, kill switch"
            },
            "tips": [
                {"content": "WireGuard: Modern protocol (2020), 4000 lines of code (vs OpenVPN 400k), faster (1000Mbps+ capable), lower latency, built into Linux 5.6+, UDP only, ChaCha20 encryption, best for speed + security", "keywords": ["wireguard", "modern", "fast", "chacha20"], "difficulty": "intermediate", "tags": ["wireguard", "modern"], "related_tools": ["WireGuard"]},
                {"content": "OpenVPN: Industry standard (2001), highly configurable, TCP/UDP modes, AES-256-GCM encryption, works on restrictive networks (TCP 443 = HTTPS), slower than WireGuard but more compatible, best for compatibility", "keywords": ["openvpn", "aes-256", "tcp", "udp", "compatible"], "difficulty": "intermediate", "tags": ["openvpn", "legacy"], "related_tools": ["OpenVPN"]},
                {"content": "OpenVPN TCP vs UDP: UDP = faster, lower latency (gaming/streaming), no retransmits, blocked on some networks, TCP = slower, reliable delivery, works on restrictive networks (port 443), use UDP unless blocked", "keywords": ["tcp", "udp", "openvpn", "port 443"], "difficulty": "intermediate", "tags": ["openvpn"], "related_tools": []},
                {"content": "IKEv2/IPSec: Fast (similar to WireGuard), auto-reconnect on network change (mobile friendly), native Windows/macOS/iOS, AES-256, MOBIKE protocol (seamless WiFi to cellular), good for mobile devices", "keywords": ["ikev2", "ipsec", "mobile", "reconnect"], "difficulty": "intermediate", "tags": ["mobile"], "related_tools": []},
                {"content": "Split tunneling: Route some traffic through VPN, rest direct (e.g., Netflix direct, torrents via VPN), reduces VPN load, faster local traffic, configure per-app (Windows/Android) or IP range, check VPN app settings", "keywords": ["split tunneling", "selective routing", "per-app"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": []},
                {"content": "Kill switch: Blocks internet if VPN drops (prevents IP leaks), firewall rule blocks non-VPN traffic, essential for privacy, built into most VPN apps, test by disconnecting VPN (should block internet)", "keywords": ["kill switch", "ip leak", "firewall", "privacy"], "difficulty": "intermediate", "tags": ["security"], "related_tools": []},
                {"content": "DNS leak protection: VPN connected but DNS queries go to ISP (leak real activity), fix: use VPN's DNS servers, Windows: Set DNS to VPN adapter, test: dnsleaktest.com, enable 'DNS leak protection' in VPN app", "keywords": ["dns leak", "privacy", "isp", "dnsleaktest"], "difficulty": "intermediate", "tags": ["security"], "related_tools": ["dnsleaktest.com"]},
                {"content": "VPN speed factors: Server distance (closer = faster), server load (overcrowded = slow), protocol (WireGuard > IKEv2 > OpenVPN UDP > TCP), encryption overhead (AES-256 = 10-20% slower), ISP throttling (VPN bypasses)", "keywords": ["speed", "latency", "server distance", "load"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "Multi-hop VPN: Double VPN (traffic through 2 servers), extra privacy (VPN provider can't see source + destination), slower (2x latency), overkill for most users, useful for high-risk activities only", "keywords": ["multi-hop", "double vpn", "privacy", "slow"], "difficulty": "advanced", "tags": ["privacy"], "related_tools": []},
                {"content": "Obfuscation: Disguises VPN traffic as HTTPS (bypasses VPN blocks), useful in China/Russia/schools, OpenVPN Scramble, Shadowsocks protocol, slower (extra encryption layer), enable if VPN blocked", "keywords": ["obfuscation", "shadowsocks", "china", "vpn block"], "difficulty": "advanced", "tags": ["censorship"], "related_tools": []},
                {"content": "No-logs policy: VPN provider doesn't store connection logs (IP, timestamps, traffic), audit required (PwC, Deloitte), jurisdiction matters (5/9/14 Eyes = avoid), check independent audits before trusting", "keywords": ["no-logs", "audit", "privacy", "jurisdiction"], "difficulty": "intermediate", "tags": ["privacy"], "related_tools": []},
                {"content": "Port forwarding: Opens port on VPN IP (for torrenting/gaming servers), not all VPNs support it, security risk (exposes service), useful for seeding torrents (better ratios), configure in VPN app if available", "keywords": ["port forwarding", "torrenting", "seeding"], "difficulty": "advanced", "tags": ["torrenting"], "related_tools": []}
            ]
        }

        # VIRTUALIZATION_VMWARE_WORKSTATION
        kb["virtualization_vmware_workstation"] = {
            "metadata": {
                "priority": 4,
                "tags": ["vmware", "virtualization", "vm", "workstation", "performance"],
                "difficulty": "intermediate",
                "description": "VMware Workstation Pro configuration, performance tuning, nested virtualization, snapshots"
            },
            "tips": [
                {"content": "VMware Workstation Pro vs Player: Pro = snapshots/clones/multiple VMs running, $200 lifetime, Player = free (personal use), single VM, no snapshots, Pro essential for testing/development", "keywords": ["workstation pro", "player", "license", "snapshots"], "difficulty": "beginner", "tags": ["licensing"], "related_tools": ["VMware Workstation"]},
                {"content": "CPU allocation: 1-2 cores per VM (Windows guest), 4+ cores for heavy workloads, NEVER allocate all host cores (leaves nothing for host), enable 'Virtualize Intel VT-x/EPT' for nested virtualization", "keywords": ["cpu cores", "allocation", "vt-x", "ept"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "RAM allocation: Windows 10 VM = 4GB min (8GB smooth), 2GB for Linux, leave 25% RAM for host OS, overcommit NOT recommended (swapping kills performance), adjust before starting VM", "keywords": ["ram", "memory", "allocation", "overcommit"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "VMware Tools: Essential guest additions, install after OS install, enables shared folders, copy/paste between host/guest, better graphics, time sync, auto-fit resolution, Update Tools menu in VM", "keywords": ["vmware tools", "guest additions", "shared folders"], "difficulty": "beginner", "tags": ["setup"], "related_tools": []},
                {"content": "Disk types: Preallocated = faster (no expansion overhead), uses full space immediately, Split files (2GB chunks) = portable but slower, Thin provisioned = grows on-demand (slower writes), preallocated for best perf", "keywords": ["disk", "preallocated", "thin provisioned", "vmdk"], "difficulty": "intermediate", "tags": ["storage"], "related_tools": []},
                {"content": "Snapshots: Instant VM state save (RAM + disk), revert to snapshot anytime, use BEFORE risky changes (updates/software installs), chain snapshots = slow, delete old snapshots (Snapshot Manager), max 10 snapshots", "keywords": ["snapshots", "rollback", "snapshot manager"], "difficulty": "intermediate", "tags": ["backup"], "related_tools": []},
                {"content": "Nested virtualization: Run VM inside VM (Hyper-V in VMware), enable 'Virtualize Intel VT-x/EPT' in CPU settings, requires host VT-x enabled in BIOS, slow (double virtualization overhead), useful for testing hypervisors", "keywords": ["nested virtualization", "vt-x", "hyper-v"], "difficulty": "advanced", "tags": ["advanced"], "related_tools": []},
                {"content": "Shared folders: Access host files from guest VM, enable in VM Settings > Options > Shared Folders, appears as network drive (Windows) or /mnt/hgfs (Linux), slower than local disk, useful for file transfer", "keywords": ["shared folders", "hgfs", "file transfer"], "difficulty": "beginner", "tags": ["setup"], "related_tools": []},
                {"content": "Network modes: NAT (default, VM shares host IP, outbound only), Bridged (VM gets own IP on network, inbound OK), Host-only (VM-host communication only, no internet), use Bridged for servers", "keywords": ["nat", "bridged", "host-only", "networking"], "difficulty": "intermediate", "tags": ["networking"], "related_tools": []},
                {"content": "3D acceleration: Enable for Windows guests (Settings > Display > Accelerate 3D graphics), allocate 2-4GB video memory, NOT for gaming (slow), OK for Aero/visual effects, Linux needs updated VMware Tools", "keywords": ["3d acceleration", "graphics", "aero"], "difficulty": "intermediate", "tags": ["graphics"], "related_tools": []},
                {"content": "Clones: Full clone = independent copy (slow create, portable), Linked clone = references parent VM (fast create, needs parent, smaller), use linked clones for testing variations, full clones for permanent copies", "keywords": ["clones", "full clone", "linked clone"], "difficulty": "intermediate", "tags": ["management"], "related_tools": []},
                {"content": "Performance optimization: Defragment/optimize virtual disk (VM Settings > Hard Disk > Defragment/Optimize), disable guest OS services (Superfetch, Search), SSD host = better performance, disable Windows animations in guest", "keywords": ["optimization", "defragment", "performance"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": []}
            ]
        }

        # VIRTUALIZATION_VIRTUALBOX
        kb["virtualization_virtualbox"] = {
            "metadata": {
                "priority": 4,
                "tags": ["virtualbox", "virtualization", "vm", "oracle", "open-source"],
                "difficulty": "intermediate",
                "description": "VirtualBox setup, Guest Additions, USB passthrough, snapshots, performance tuning"
            },
            "tips": [
                {"content": "VirtualBox vs VMware: VirtualBox = free (open-source), slower performance, better USB support, cross-platform, VMware = faster, polished, paid (Pro), use VirtualBox for casual use, VMware for professional", "keywords": ["virtualbox", "vmware", "comparison", "free"], "difficulty": "beginner", "tags": ["comparison"], "related_tools": ["VirtualBox", "VMware"]},
                {"content": "Guest Additions: Essential for VirtualBox, install AFTER OS install (Devices > Insert Guest Additions CD), enables shared folders, clipboard sharing, auto-resize, better graphics, update with VirtualBox updates", "keywords": ["guest additions", "shared folders", "clipboard"], "difficulty": "beginner", "tags": ["setup"], "related_tools": []},
                {"content": "CPU settings: Enable PAE/NX (Settings > System > Processor), allocate 50% of host cores max, enable VT-x/AMD-V in BIOS first (check with 'systeminfo' in Windows), 2 cores min for Windows guest", "keywords": ["cpu", "pae", "nx", "vt-x", "amd-v"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "RAM allocation: Windows 10 = 4GB min, green zone in slider = safe, red = risky (host swapping), dynamic allocation NOT recommended (enable 'Use Host I/O Cache' instead for dynamic-like behavior)", "keywords": ["ram", "memory", "allocation", "dynamic"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "USB passthrough: Requires Extension Pack (free download), Settings > USB > Enable USB 3.0 Controller, add USB filters for specific devices, Windows host may need USB driver in guest, useful for hardware dongles", "keywords": ["usb", "passthrough", "extension pack", "usb3"], "difficulty": "intermediate", "tags": ["usb"], "related_tools": []},
                {"content": "Extension Pack: Adds USB 3.0, RDP server, PXE boot, disk encryption, download from VirtualBox website (same version as VirtualBox), File > Preferences > Extensions > Add, required for USB 2.0/3.0", "keywords": ["extension pack", "usb3", "rdp"], "difficulty": "beginner", "tags": ["setup"], "related_tools": []},
                {"content": "Snapshots: Similar to VMware, right-click VM > Snapshots, tree view (multiple branches), restore snapshot = revert VM, saved states vs snapshots (saved = pause, snapshot = restore point), delete old to save space", "keywords": ["snapshots", "restore", "saved state"], "difficulty": "intermediate", "tags": ["backup"], "related_tools": []},
                {"content": "Shared folders: Settings > Shared Folders > Add, Auto-mount + Make Permanent (Windows guest shows as network drive), Linux guest needs 'sudo usermod -aG vboxsf $USER' (logout/login), slower than local disk", "keywords": ["shared folders", "vboxsf", "auto-mount"], "difficulty": "intermediate", "tags": ["setup"], "related_tools": []},
                {"content": "Disk types: VDI (VirtualBox native), VHD (Hyper-V compatible), VMDK (VMware compatible), dynamically allocated = grows (slower), fixed size = preallocated (faster), fixed for performance, dynamic for space saving", "keywords": ["vdi", "vhd", "vmdk", "dynamic", "fixed"], "difficulty": "intermediate", "tags": ["storage"], "related_tools": []},
                {"content": "3D acceleration: Settings > Display > Enable 3D Acceleration, 128-256MB video memory, unstable on some hosts (disable if glitches), requires Guest Additions, NOT for gaming (very slow), OK for desktop effects", "keywords": ["3d acceleration", "video memory", "guest additions"], "difficulty": "intermediate", "tags": ["graphics"], "related_tools": []},
                {"content": "Networking modes: NAT (default, outbound only), Bridged (own IP, inbound OK), Host-only (isolated, VM-host only), Internal (VMs only, no host), use Bridged for accessible servers, NAT for security", "keywords": ["nat", "bridged", "host-only", "internal"], "difficulty": "intermediate", "tags": ["networking"], "related_tools": []},
                {"content": "Performance tips: Enable VT-x/AMD-V + nested paging (BIOS), disable Floppy in boot order, use paravirtualization (Hyper-V for Windows guest, KVM for Linux), SSD host = major speedup, enable I/O APIC", "keywords": ["performance", "paravirtualization", "io apic"], "difficulty": "advanced", "tags": ["optimization"], "related_tools": []}
            ]
        }

        # WSL2_LINUX_WINDOWS
        kb["wsl2_linux_windows"] = {
            "metadata": {
                "priority": 4,
                "tags": ["wsl2", "linux", "windows", "development", "subsystem"],
                "difficulty": "intermediate",
                "description": "WSL2 setup, distro management, Docker integration, performance optimization, file access"
            },
            "tips": [
                {"content": "WSL2 vs WSL1: WSL2 = real Linux kernel (faster, full syscall compatibility, Docker works), WSL1 = translation layer (slower I/O, no Docker), use WSL2 (default since Windows 10 2004), wsl --set-version <distro> 2", "keywords": ["wsl2", "wsl1", "comparison", "docker"], "difficulty": "beginner", "tags": ["basics"], "related_tools": []},
                {"content": "Installation: Windows 11/10 2004+, 'wsl --install' (PowerShell admin), installs Ubuntu by default, enable Virtual Machine Platform (Windows Features), reboot required, set WSL2 default: wsl --set-default-version 2", "keywords": ["install", "wsl --install", "virtual machine platform"], "difficulty": "beginner", "tags": ["setup"], "related_tools": []},
                {"content": "Distro management: List installed 'wsl -l -v', install new 'wsl --install -d <distro>' (Ubuntu, Debian, Kali, Arch), uninstall 'wsl --unregister <distro>', set default 'wsl --set-default <distro>', Microsoft Store for GUI install", "keywords": ["distro", "ubuntu", "debian", "wsl -l"], "difficulty": "intermediate", "tags": ["management"], "related_tools": []},
                {"content": "Docker Desktop integration: Docker Desktop uses WSL2 backend (faster than Hyper-V), Settings > Resources > WSL Integration > Enable for distros, run 'docker' directly in WSL2 (no VM overhead), shared Docker daemon", "keywords": ["docker", "docker desktop", "integration"], "difficulty": "intermediate", "tags": ["docker"], "related_tools": ["Docker Desktop"]},
                {"content": "File access: Linux files in \\\\\\\\wsl$\\\\<distro>\\\\home\\\\<user> (Windows Explorer), SLOW from Windows (use /mnt/c/ in WSL instead), Windows files /mnt/c/ (fast), keep project files in Linux FS for speed (10x faster build times)", "keywords": ["file access", "wsl$", "/mnt/c/", "performance"], "difficulty": "intermediate", "tags": ["filesystem"], "related_tools": []},
                {"content": "Performance: Linux FS = native speed, Windows FS (/mnt/c/) = slow (network overhead), put code in ~/projects (WSL), NOT /mnt/c/, npm install 10x faster in WSL FS, git clone in WSL FS for speed", "keywords": ["performance", "filesystem", "linux fs", "speed"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "VS Code integration: Install 'WSL' extension, open folder in WSL ('code .' in WSL terminal or Remote Explorer), runs VS Code server in WSL (seamless), auto-detects WSL paths, best way to develop in WSL", "keywords": ["vscode", "wsl extension", "remote", "code ."], "difficulty": "intermediate", "tags": ["vscode"], "related_tools": ["VS Code"]},
                {"content": "Memory limit: WSL2 uses 50% RAM by default (8GB on 16GB system), create .wslconfig in user folder: [wsl2]\\nmemory=4GB\\nprocessors=2\\nswap=0, restart WSL 'wsl --shutdown'", "keywords": ["memory", "wslconfig", "ram limit", "wsl --shutdown"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": []},
                {"content": "Networking: WSL2 gets NAT IP (172.x.x.x), localhost forwards work (access WSL server at localhost:3000 from Windows), outbound internet works, inbound requires port proxy (netsh portproxy add), Windows 11 mirrored mode fixes this", "keywords": ["networking", "localhost", "nat", "port proxy"], "difficulty": "advanced", "tags": ["networking"], "related_tools": []},
                {"content": "systemd support: Windows 11 22H2+, /etc/wsl.conf: [boot]\\nsystemd=true, restart WSL 'wsl --shutdown', enables systemctl (services), Docker without Docker Desktop, snap packages, reboot to apply", "keywords": ["systemd", "systemctl", "wsl.conf", "services"], "difficulty": "intermediate", "tags": ["modern"], "related_tools": []},
                {"content": "Backup/export: Export distro 'wsl --export <distro> <file.tar>', import 'wsl --import <name> <install-location> <file.tar>', useful for backups or moving to new PC, doesn't preserve user (set manually)", "keywords": ["backup", "export", "import", "wsl --export"], "difficulty": "intermediate", "tags": ["backup"], "related_tools": []},
                {"content": "GUI apps (WSLg): Windows 11 built-in, run Linux GUI apps (Firefox, VS Code, gedit), 'sudo apt install firefox' then 'firefox' (appears in Windows), uses Wayland, no config needed, start menu shortcuts auto-created", "keywords": ["wslg", "gui apps", "wayland", "windows 11"], "difficulty": "beginner", "tags": ["gui"], "related_tools": []}
            ]
        }

        # DEVELOPMENT_GIT_WORKFLOW
        kb["development_git_workflow"] = {
            "metadata": {
                "priority": 4,
                "tags": ["git", "github", "version-control", "development", "workflow"],
                "difficulty": "intermediate",
                "description": "Git basics, branching strategies, commits, GitHub workflow, best practices"
            },
            "tips": [
                {"content": "Git basics: 'git init' (new repo), 'git clone <url>' (copy repo), 'git status' (see changes), 'git add .' (stage all), 'git commit -m \"message\"' (save), 'git push' (upload), 'git pull' (download + merge)", "keywords": ["git init", "clone", "status", "add", "commit", "push", "pull"], "difficulty": "beginner", "tags": ["basics"], "related_tools": ["Git"]},
                {"content": "Branching: 'git branch <name>' (create), 'git checkout <name>' (switch), 'git checkout -b <name>' (create + switch), 'git merge <branch>' (merge into current), 'git branch -d <name>' (delete), always branch for features", "keywords": ["branch", "checkout", "merge", "feature branch"], "difficulty": "intermediate", "tags": ["branching"], "related_tools": []},
                {"content": "Commit messages: Format 'type: short description\\n\\ndetailed explanation', types: feat (feature), fix (bug), docs, style, refactor, test, chore, use imperative ('add' not 'added'), <50 chars first line, detailed body if needed", "keywords": ["commit message", "conventional commits", "format"], "difficulty": "intermediate", "tags": ["best-practices"], "related_tools": []},
                {"content": "Git workflow: 1) Pull latest 'git pull origin main', 2) Create branch 'git checkout -b feature-x', 3) Make changes, 4) Stage 'git add .', 5) Commit 'git commit -m \"feat: add X\"', 6) Push 'git push origin feature-x', 7) Open PR on GitHub", "keywords": ["workflow", "pull request", "feature branch"], "difficulty": "intermediate", "tags": ["workflow"], "related_tools": ["GitHub"]},
                {"content": "Undoing changes: Unstage 'git reset <file>', discard changes 'git checkout -- <file>', undo last commit (keep changes) 'git reset HEAD~1', undo + discard 'git reset --hard HEAD~1', revert commit 'git revert <hash>' (safe for pushed)", "keywords": ["reset", "revert", "undo", "checkout"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "Stashing: Save work-in-progress 'git stash', restore 'git stash pop', list stashes 'git stash list', useful when switching branches mid-work, 'git stash apply' (keep stash) vs 'pop' (delete stash)", "keywords": ["stash", "git stash", "stash pop", "wip"], "difficulty": "intermediate", "tags": ["workflow"], "related_tools": []},
                {"content": "Merge conflicts: Occur when same file edited in 2 branches, 'git status' shows conflicts, edit files (keep <<<HEAD or >>>branch changes), 'git add <file>' after fixing, 'git commit' to finish merge, use merge tool for complex conflicts", "keywords": ["merge conflict", "conflict resolution", "git status"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": ["VS Code", "KDiff3"]},
                {"content": "GitHub Pull Requests: Fork > Clone > Branch > Commit > Push > Open PR, describe changes, link issues (#123), request reviewers, address feedback (new commits), squash merge (clean history) or merge commit (preserve history)", "keywords": ["pull request", "pr", "fork", "github"], "difficulty": "intermediate", "tags": ["github"], "related_tools": ["GitHub"]},
                {"content": ".gitignore: Ignore files (node_modules/, .env, *.log), create .gitignore in repo root, templates on github.com/github/gitignore, add BEFORE first commit (hard to remove after), use '!' to un-ignore specific files", "keywords": ["gitignore", "ignore files", "node_modules"], "difficulty": "beginner", "tags": ["setup"], "related_tools": []},
                {"content": "Rebasing: 'git rebase main' (replay commits on top of main), cleaner history than merge, NEVER rebase public/pushed branches (rewrites history), use for local cleanup before PR, 'git rebase -i' for interactive (squash commits)", "keywords": ["rebase", "git rebase", "interactive rebase", "squash"], "difficulty": "advanced", "tags": ["advanced"], "related_tools": []},
                {"content": "Viewing history: 'git log' (commits), 'git log --oneline' (compact), 'git log --graph --all' (visualize branches), 'git show <hash>' (commit details), 'git diff' (unstaged changes), 'git diff --staged' (staged changes)", "keywords": ["git log", "git diff", "git show", "history"], "difficulty": "beginner", "tags": ["basics"], "related_tools": []},
                {"content": "Remote management: 'git remote -v' (list remotes), 'git remote add <name> <url>' (add), 'git fetch <remote>' (download without merge), 'git pull' = fetch + merge, origin = default remote name, upstream for forks", "keywords": ["remote", "origin", "upstream", "fetch"], "difficulty": "intermediate", "tags": ["remotes"], "related_tools": []}
            ]
        }

        # DEVELOPMENT_VSCODE_SETUP
        kb["development_vscode_setup"] = {
            "metadata": {
                "priority": 4,
                "tags": ["vscode", "editor", "development", "extensions", "productivity"],
                "difficulty": "beginner",
                "description": "VS Code essential extensions, themes, debugging, keyboard shortcuts, settings"
            },
            "tips": [
                {"content": "Essential extensions: Python (ms-python.python), Pylance (fast IntelliSense), Prettier (code formatter), ESLint (JavaScript linting), GitLens (Git supercharged), Live Server (local dev server), Bracket Pair Colorizer, Auto Rename Tag", "keywords": ["extensions", "python", "prettier", "eslint", "gitlens"], "difficulty": "beginner", "tags": ["extensions"], "related_tools": ["VS Code"]},
                {"content": "Themes: Dark+ (default dark), One Dark Pro (popular), Dracula Official, Material Theme, Night Owl, Monokai Pro, install via Extensions (Ctrl+Shift+X), Ctrl+K Ctrl+T to change theme, File Icons: Material Icon Theme", "keywords": ["themes", "dark theme", "one dark pro", "icons"], "difficulty": "beginner", "tags": ["customization"], "related_tools": []},
                {"content": "Keyboard shortcuts: Ctrl+P (quick open file), Ctrl+Shift+P (command palette), Ctrl+` (toggle terminal), Ctrl+B (toggle sidebar), Ctrl+/ (comment), Alt+Up/Down (move line), Shift+Alt+Up/Down (copy line), F2 (rename symbol)", "keywords": ["shortcuts", "ctrl+p", "command palette", "productivity"], "difficulty": "beginner", "tags": ["productivity"], "related_tools": []},
                {"content": "Multi-cursor editing: Alt+Click (add cursor), Ctrl+Alt+Up/Down (add cursor above/below), Ctrl+D (select next occurrence), Ctrl+Shift+L (select all occurrences), Esc to exit, powerful for renaming variables", "keywords": ["multi-cursor", "ctrl+d", "select occurrences"], "difficulty": "intermediate", "tags": ["productivity"], "related_tools": []},
                {"content": "Integrated terminal: Ctrl+` to toggle, supports multiple terminals (+ button), split terminal (split icon), change shell (dropdown), PowerShell/CMD/Bash/WSL, run tasks directly, Ctrl+Shift+` for new terminal", "keywords": ["terminal", "integrated terminal", "ctrl+`", "wsl"], "difficulty": "beginner", "tags": ["terminal"], "related_tools": []},
                {"content": "Debugging Python: Set breakpoint (F9 or click left margin), F5 to start debug, F10 step over, F11 step into, F5 continue, Debug Console for expressions, launch.json for custom configs, auto-generates for Python projects", "keywords": ["debugging", "breakpoint", "f5", "python", "launch.json"], "difficulty": "intermediate", "tags": ["debugging"], "related_tools": []},
                {"content": "Settings Sync: Sign in with GitHub/Microsoft (Settings Sync icon), syncs settings/extensions/keybindings across devices, enable Settings Sync in menu, conflicts auto-resolved, useful for multiple PCs", "keywords": ["settings sync", "sync", "github", "cloud"], "difficulty": "beginner", "tags": ["sync"], "related_tools": []},
                {"content": "Workspace settings: .vscode/settings.json (project-specific), overrides user settings, useful for team configs (Python interpreter, linting rules), commit to git for team consistency, File > Preferences > Settings (Workspace tab)", "keywords": ["workspace", "settings.json", ".vscode", "team"], "difficulty": "intermediate", "tags": ["configuration"], "related_tools": []},
                {"content": "IntelliSense: Ctrl+Space (trigger suggestions), auto-complete for Python/JS/TS, Pylance for type hints, install language extension for support, .venv auto-detected for Python, restart if missing completions", "keywords": ["intellisense", "autocomplete", "pylance", "ctrl+space"], "difficulty": "beginner", "tags": ["productivity"], "related_tools": []},
                {"content": "Code formatting: Prettier (JS/TS/CSS), Black (Python), Shift+Alt+F to format file, 'Format on Save' in settings (recommended), .prettierrc or pyproject.toml for config, consistent code style across team", "keywords": ["formatting", "prettier", "black", "format on save"], "difficulty": "beginner", "tags": ["formatting"], "related_tools": ["Prettier", "Black"]},
                {"content": "Live Share: Collaborate in real-time (pair programming), install Live Share extension, share session (read-write or read-only), shared terminal/debugging/servers, free for up to 5 people, useful for remote help", "keywords": ["live share", "collaboration", "pair programming"], "difficulty": "intermediate", "tags": ["collaboration"], "related_tools": ["Live Share"]},
                {"content": "Zen Mode: Distraction-free coding (Ctrl+K Z), hides sidebar/status bar/tabs, Esc Esc to exit, useful for focus sessions, combine with full screen (F11), customizable in settings (Hide tabs, center layout)", "keywords": ["zen mode", "distraction-free", "focus", "ctrl+k z"], "difficulty": "beginner", "tags": ["productivity"], "related_tools": []}
            ]
        }

        # MULTIMEDIA_VIDEO_ENCODING
        kb["multimedia_video_encoding"] = {
            "metadata": {
                "priority": 3,
                "tags": ["video", "encoding", "codec", "h264", "h265", "av1", "multimedia"],
                "difficulty": "intermediate",
                "description": "Video codec comparison: H.264 vs H.265 vs AV1, bitrate, quality, hardware encoding"
            },
            "tips": [
                {"content": "H.264 (AVC): Industry standard (2003), 1080p@8Mbps good quality, universal playback (all devices), fast encode/decode, hardware support everywhere, use for compatibility, 10-20Mbps for archival, 3-8Mbps streaming", "keywords": ["h264", "avc", "bitrate", "compatibility"], "difficulty": "intermediate", "tags": ["h264"], "related_tools": ["Handbrake", "FFmpeg"]},
                {"content": "H.265 (HEVC): 40-50% smaller files than H.264 at same quality (1080p@4-6Mbps), 4K streaming standard (Netflix, YouTube), slower encode, patent issues, hardware decode 2016+ devices, use for 4K or storage savings", "keywords": ["h265", "hevc", "4k", "efficiency"], "difficulty": "intermediate", "tags": ["h265"], "related_tools": ["Handbrake"]},
                {"content": "AV1: Royalty-free (no patents), 30% smaller than H.265 (1080p@3-4Mbps), YouTube/Netflix adopting, VERY slow CPU encode, hardware encode 2023+ (Intel Arc, RTX 40xx), decode 2020+ (most browsers), future-proof", "keywords": ["av1", "royalty-free", "youtube", "slow encode"], "difficulty": "advanced", "tags": ["av1", "modern"], "related_tools": ["FFmpeg", "Handbrake"]},
                {"content": "Bitrate vs quality: 1080p H.264 = 8Mbps (good), 12Mbps (great), 20Mbps (archival), 4K H.265 = 15-25Mbps, streaming = lower (3-6Mbps), CRF 18-23 (constant quality, better than fixed bitrate), lower CRF = higher quality", "keywords": ["bitrate", "crf", "quality", "1080p", "4k"], "difficulty": "intermediate", "tags": ["quality"], "related_tools": []},
                {"content": "Hardware encoding: NVENC (NVIDIA), QuickSync (Intel), AMF (AMD), 5-10x faster than CPU (x264/x265), slightly lower quality at same bitrate (2-3% worse), use for streaming/recording, CPU for archival, NVENC best quality", "keywords": ["nvenc", "quicksync", "amf", "hardware encode"], "difficulty": "intermediate", "tags": ["hardware"], "related_tools": ["OBS", "Handbrake"]},
                {"content": "CPU encoding: x264 (H.264), x265 (H.265), best quality, slow (real-time for streaming needs fast preset), presets: ultrafast/fast/medium (balanced)/slow/veryslow (best quality), use slow for archival", "keywords": ["x264", "x265", "cpu encode", "presets"], "difficulty": "intermediate", "tags": ["cpu"], "related_tools": ["FFmpeg", "Handbrake"]},
                {"content": "Container formats: MP4 (universal, H.264/H.265), MKV (supports all codecs, chapters, multiple audio), WebM (AV1/VP9, web-friendly), MOV (Apple), use MP4 for compatibility, MKV for flexibility", "keywords": ["mp4", "mkv", "webm", "container"], "difficulty": "beginner", "tags": ["formats"], "related_tools": []},
                {"content": "Two-pass encoding: First pass analyzes video, second pass optimizes bitrate, better quality than single-pass at same file size, 2x slower, use for final exports, NOT for streaming (latency), Handbrake supports 2-pass", "keywords": ["two-pass", "2-pass", "quality", "handbrake"], "difficulty": "intermediate", "tags": ["quality"], "related_tools": ["Handbrake"]},
                {"content": "Audio codecs: AAC (universal, 128-192kbps stereo), Opus (better quality, 96-128kbps, MKV/WebM), AC3/DTS (surround sound), FLAC (lossless, archival), use AAC for MP4, Opus for MKV, 192kbps AAC transparent", "keywords": ["aac", "opus", "audio", "bitrate"], "difficulty": "intermediate", "tags": ["audio"], "related_tools": []},
                {"content": "Resolution vs bitrate: 720p = 3-5Mbps H.264, 1080p = 8-12Mbps, 1440p = 16-24Mbps, 4K = 35-50Mbps (H.264) or 20-30Mbps (H.265), higher bitrate needed for fast motion (action scenes), anime needs less (fewer details)", "keywords": ["resolution", "bitrate", "720p", "1080p", "4k"], "difficulty": "intermediate", "tags": ["quality"], "related_tools": []},
                {"content": "HDR encoding: HDR10 (static metadata, H.265), Dolby Vision (dynamic, proprietary), HLG (broadcast), requires 10-bit color, H.265 or AV1 only, Handbrake/FFmpeg support, HDR to SDR tone-mapping if device doesn't support HDR", "keywords": ["hdr", "hdr10", "dolby vision", "10-bit"], "difficulty": "advanced", "tags": ["hdr"], "related_tools": ["Handbrake", "FFmpeg"]},
                {"content": "Handbrake presets: Fast 1080p30 (H.264, RF 22, balanced), H.265 MKV 1080p30 (smaller files), Production Max (high quality, large), Very Fast (streaming), use presets as starting point, adjust RF/bitrate for quality", "keywords": ["handbrake", "presets", "rf", "h264"], "difficulty": "beginner", "tags": ["handbrake"], "related_tools": ["Handbrake"]}
            ]
        }

        # MULTIMEDIA_OBS_STREAMING
        kb["multimedia_obs_streaming"] = {
            "metadata": {
                "priority": 4,
                "tags": ["obs", "streaming", "recording", "twitch", "youtube", "encoder"],
                "difficulty": "intermediate",
                "description": "OBS Studio setup: encoder settings, bitrate, scenes, NVENC vs x264, streaming optimization"
            },
            "tips": [
                {"content": "Encoder selection: NVENC (NVIDIA GPU, low CPU, 6000+ series), QuickSync (Intel iGPU, 7th gen+), x264 (CPU, best quality, high load), AMF (AMD GPU, OK quality), use NVENC if available (best performance/quality balance)", "keywords": ["encoder", "nvenc", "x264", "quicksync", "amf"], "difficulty": "intermediate", "tags": ["encoding"], "related_tools": ["OBS Studio"]},
                {"content": "Bitrate for Twitch: 1080p60 = 6000kbps max (Twitch limit), 720p60 = 4500kbps, 720p30 = 3000kbps, partners get transcoding (viewers can lower quality), non-partners stick to 3000-4500kbps (mobile viewers), audio 160kbps", "keywords": ["twitch", "bitrate", "6000kbps", "transcoding"], "difficulty": "intermediate", "tags": ["twitch"], "related_tools": []},
                {"content": "Bitrate for YouTube: 1080p60 = 9000-12000kbps, 1440p60 = 18000-24000kbps, 4K60 = 40000-51000kbps, no hard limit (auto transcoding), higher = better quality but needs fast upload, check upload speed (speedtest.net)", "keywords": ["youtube", "bitrate", "1080p", "upload speed"], "difficulty": "intermediate", "tags": ["youtube"], "related_tools": []},
                {"content": "NVENC settings: Preset 'Quality' (balance) or 'Max Quality' (slower, better), Tuning 'High Quality' (streaming) or 'Lossless' (recording), Profile 'High', Look-ahead OFF (streaming latency), Psycho Visual Tuning ON (quality)", "keywords": ["nvenc", "quality preset", "tuning", "psycho visual"], "difficulty": "advanced", "tags": ["nvenc"], "related_tools": []},
                {"content": "x264 settings: Preset 'veryfast' (streaming, 6-core CPU) or 'medium' (8-core+), 'slow' for recording, CRF 18-23 (recording), Tune 'zerolatency' (streaming), Profile 'high', faster preset = lower CPU but worse quality", "keywords": ["x264", "preset", "veryfast", "crf", "zerolatency"], "difficulty": "advanced", "tags": ["x264"], "related_tools": []},
                {"content": "Output resolution: Native (1080p or 1440p) for recording, downscale to 720p60 for streaming (less bitrate needed, sharper than 1080p@low bitrate), Settings > Video > Output (Scaled) Resolution, Lanczos filter (best quality)", "keywords": ["resolution", "downscale", "720p", "1080p", "lanczos"], "difficulty": "intermediate", "tags": ["video"], "related_tools": []},
                {"content": "Scenes and sources: Scene = collection of sources (game capture, webcam, overlays), add source (+ button), order matters (top = front), groups for organization, Studio Mode (preview before going live), hotkeys for scene switching", "keywords": ["scenes", "sources", "studio mode", "hotkeys"], "difficulty": "beginner", "tags": ["setup"], "related_tools": []},
                {"content": "Game Capture: Fastest for fullscreen games, Mode 'Capture specific window', Match Priority 'Match title, else exe', anti-cheat compatibility (some games block), black screen = run OBS as admin or use Display Capture", "keywords": ["game capture", "specific window", "black screen"], "difficulty": "intermediate", "tags": ["capture"], "related_tools": []},
                {"content": "Audio setup: Desktop Audio (system sounds), Mic/Aux (microphone), Filters (noise suppression, noise gate, compressor), Audio Monitoring (listen to mic), Advanced Audio Properties (monitor + sync delays), test levels before stream", "keywords": ["audio", "filters", "noise suppression", "compressor"], "difficulty": "intermediate", "tags": ["audio"], "related_tools": []},
                {"content": "Recording settings: Output Mode 'Advanced', Recording Format 'mkv' (safe, no corruption on crash, remux to mp4 after), Encoder same as streaming or 'lossless' (huge files), CRF 18-20 for high quality, separate audio tracks for editing", "keywords": ["recording", "mkv", "lossless", "crf", "audio tracks"], "difficulty": "intermediate", "tags": ["recording"], "related_tools": []},
                {"content": "Performance optimization: Run OBS as admin (priority), Settings > Advanced > Process Priority 'High', disable Windows Game Bar, close Chrome (RAM hog), cap game FPS (reduces load), 'Performance Mode' power plan, monitor dropped frames (Stats dock)", "keywords": ["performance", "admin", "priority", "dropped frames"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": []},
                {"content": "Plugins: StreamFX (advanced effects, upscaling), Browser Source (overlays, alerts), VLC Source (playlists), Move Transition (smooth scene transitions), install via OBS Plugin Manager or manual download, restart OBS after install", "keywords": ["plugins", "streamfx", "browser source", "move transition"], "difficulty": "intermediate", "tags": ["plugins"], "related_tools": ["StreamFX"]}
            ]
        }

        # FILE_MANAGEMENT_TOOLS
        kb["file_management_tools"] = {
            "metadata": {
                "priority": 3,
                "tags": ["file-management", "tools", "productivity", "search", "organization"],
                "difficulty": "beginner",
                "description": "File management tools: Everything search, Total Commander, advanced explorers, organization"
            },
            "tips": [
                {"content": "Everything Search: Instant file search (NTFS indexing), searches by filename (NOT content), download voidtools.com, indexes drives in seconds, regex support, 'ext:pdf' (filter by extension), 'dm:today' (modified today), 'size:>100mb'", "keywords": ["everything", "search", "ntfs", "voidtools", "instant"], "difficulty": "beginner", "tags": ["search"], "related_tools": ["Everything"]},
                {"content": "Total Commander: Dual-pane file manager (Norton Commander clone), FTP/SFTP built-in, batch rename, file compare, plugins (archives, FTP), keyboard-driven (F5 copy, F6 move, F8 delete), $40 lifetime, alternative: Double Commander (free)", "keywords": ["total commander", "dual-pane", "ftp", "batch rename"], "difficulty": "intermediate", "tags": ["file-manager"], "related_tools": ["Total Commander", "Double Commander"]},
                {"content": "FreeCommander: Free Total Commander alternative, dual-pane, tabbed interface, built-in viewers (hex, text, images), file sync, archive support, folder tree, portable version available, good for casual users", "keywords": ["freecommander", "free", "dual-pane", "tabs"], "difficulty": "beginner", "tags": ["file-manager"], "related_tools": ["FreeCommander"]},
                {"content": "Files (Windows 11 app): Modern file manager, tabs, dual-pane, tags, column view, GitHub integration, faster than Explorer, free (Microsoft Store), preview pane, customizable, good Explorer replacement", "keywords": ["files app", "windows 11", "modern", "tabs"], "difficulty": "beginner", "tags": ["modern"], "related_tools": ["Files"]},
                {"content": "Bulk Rename Utility: Advanced batch renaming, regex support, preview changes, case conversion, numbering, find/replace, date/time stamps, EXIF data, free, portable, overkill for simple renames (Explorer F2 + Ctrl)", "keywords": ["bulk rename", "batch", "regex", "rename"], "difficulty": "intermediate", "tags": ["renaming"], "related_tools": ["Bulk Rename Utility"]},
                {"content": "TreeSize Free: Disk space analyzer, visualize folder sizes, tree view + bar chart, scan NTFS volumes, find large files, export reports, delete from app, alternative: WinDirStat (treemap view, slower), WizTree (fastest, Everything-based)", "keywords": ["treesize", "disk space", "analyzer", "windirstat", "wiztree"], "difficulty": "beginner", "tags": ["disk-space"], "related_tools": ["TreeSize", "WinDirStat", "WizTree"]},
                {"content": "File organization: Create 'Archive' folder (old files), 'Projects' (active work), 'Downloads' (sort weekly), use subfolders (no more than 3 levels deep), consistent naming (YYYY-MM-DD prefix for chronological), avoid Desktop clutter", "keywords": ["organization", "folders", "naming", "structure"], "difficulty": "beginner", "tags": ["organization"], "related_tools": []},
                {"content": "Quick Access (Windows): Pin frequently-used folders (drag to Quick Access), Shift+Right-click > 'Pin to Quick Access', remove clutter (unpin Recent files in Folder Options), faster than navigating deep paths", "keywords": ["quick access", "pin", "windows", "shortcuts"], "difficulty": "beginner", "tags": ["windows"], "related_tools": []},
                {"content": "Symbolic links: ln -s (Linux), mklink /D (Windows), link folder to another location (e.g., 'C:\\Games' -> 'D:\\Games'), saves space on C drive, transparent to apps, use for moving large game installs without reinstalling", "keywords": ["symbolic link", "mklink", "junction", "games"], "difficulty": "intermediate", "tags": ["advanced"], "related_tools": []},
                {"content": "File tagging: Windows 10/11 supports tags (Details pane), Everything search 'tag:important', useful for photos/documents, third-party: TagSpaces (cross-platform, markdown-based), Tabbles (advanced, paid), limited native support", "keywords": ["tags", "tagging", "tagspaces", "tabbles"], "difficulty": "intermediate", "tags": ["organization"], "related_tools": ["TagSpaces", "Tabbles"]},
                {"content": "Cloud sync: OneDrive (Windows integrated, 5GB free), Google Drive (15GB free), Dropbox (2GB free), selective sync (don't sync all folders), Files On-Demand (cloud-only until opened), avoid syncing app data (conflicts)", "keywords": ["onedrive", "google drive", "dropbox", "cloud sync"], "difficulty": "beginner", "tags": ["cloud"], "related_tools": ["OneDrive", "Google Drive"]},
                {"content": "Advanced search (Explorer): Search filters in Explorer, 'datemodified:today', 'size:>10MB', 'kind:music', 'tag:vacation', save searches (right-click > Save search), slower than Everything but searches content too", "keywords": ["windows search", "explorer", "filters", "search"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []}
            ]
        }

        # COMPRESSION_FORMATS
        kb["compression_formats"] = {
            "metadata": {
                "priority": 3,
                "tags": ["compression", "zip", "rar", "7z", "archive", "formats"],
                "difficulty": "beginner",
                "description": "Archive formats comparison: ZIP vs RAR vs 7Z, compression ratios, speed, encryption"
            },
            "tips": [
                {"content": "ZIP: Universal (built into Windows/macOS/Linux), fast compression/extraction, 4GB file limit (unless ZIP64), basic encryption (weak), use for compatibility/sharing, 7-Zip/WinRAR create better ZIPs than Windows", "keywords": ["zip", "universal", "4gb limit", "zip64"], "difficulty": "beginner", "tags": ["zip"], "related_tools": ["7-Zip", "WinRAR"]},
                {"content": "7Z: Best compression (LZMA2 algorithm), 30-70% smaller than ZIP, slower (high CPU), AES-256 encryption (strong), open-source, use 7-Zip app (free), NOT native in Windows, best for archival/large files", "keywords": ["7z", "lzma2", "best compression", "7-zip", "aes-256"], "difficulty": "intermediate", "tags": ["7z"], "related_tools": ["7-Zip"]},
                {"content": "RAR: Proprietary (WinRAR), good compression (between ZIP and 7Z), recovery records (repair corrupted archives), split archives, AES-256 encryption, $29 license (nagware = free), use for recovery features", "keywords": ["rar", "winrar", "recovery", "split", "proprietary"], "difficulty": "intermediate", "tags": ["rar"], "related_tools": ["WinRAR"]},
                {"content": "Compression speed: ZIP = fast (low CPU, good for frequent compression), 7Z Ultra = very slow (10x slower than ZIP, 20-30% smaller), 7Z Normal = balanced, RAR = medium speed, use ZIP for speed, 7Z for size", "keywords": ["speed", "compression ratio", "cpu usage"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "Solid archives: 7Z/RAR feature, compresses all files as one stream (better ratio), slower extraction (can't extract single file fast), use for archival (extract once), NOT for frequent access, 7-Zip 'Solid' option", "keywords": ["solid archive", "7z", "rar", "compression ratio"], "difficulty": "advanced", "tags": ["advanced"], "related_tools": ["7-Zip", "WinRAR"]},
                {"content": "Encryption: ZIP = ZipCrypto (weak, crack in minutes), 7Z/RAR = AES-256 (strong), encrypted filename list in 7Z (hides file names), use 7Z for secure archives, password length >12 chars, avoid dictionary words", "keywords": ["encryption", "aes-256", "zipcrypto", "password"], "difficulty": "intermediate", "tags": ["security"], "related_tools": ["7-Zip"]},
                {"content": "Split archives: Split large file (e.g., 5GB into 100MB parts), ZIP/RAR/7Z support, useful for upload limits (email, old FAT32 USB), extract needs all parts present, 7-Zip: 'Split to volumes' option, RAR: .part1.rar naming", "keywords": ["split", "multi-volume", "parts", "volumes"], "difficulty": "intermediate", "tags": ["split"], "related_tools": ["7-Zip", "WinRAR"]},
                {"content": "TAR.GZ: Unix/Linux standard, TAR = combine files (no compression), GZ = gzip compression, .tar.gz = both, slower than 7Z, worse compression than 7Z, use on Linux or cross-platform compatibility", "keywords": ["tar", "gzip", "tar.gz", "linux", "unix"], "difficulty": "intermediate", "tags": ["linux"], "related_tools": ["7-Zip", "tar"]},
                {"content": "Compression ratio by file type: Text/code = 80-90% (excellent), Images (JPG/PNG) = 0-10% (already compressed), Videos (MP4) = 0-5% (don't compress), ISO/installers = 30-50%, use 'Store' mode for media files (skip compression)", "keywords": ["compression ratio", "file types", "text", "images"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": []},
                {"content": "7-Zip features: Right-click > 7-Zip menu, 'Add to archive' (custom settings), 'Extract Here' (current folder), 'Test' (verify integrity), built-in file manager, benchmark (test CPU), command-line support (7z.exe)", "keywords": ["7-zip", "features", "extract", "benchmark"], "difficulty": "beginner", "tags": ["7-zip"], "related_tools": ["7-Zip"]},
                {"content": "WinRAR trial: 40-day trial, keeps working after (nagware), $29 license, legal use requires purchase but not enforced, 7-Zip free alternative (no nag screen), WinRAR better for RAR extraction speed", "keywords": ["winrar", "trial", "license", "nagware"], "difficulty": "beginner", "tags": ["licensing"], "related_tools": ["WinRAR"]},
                {"content": "Context menu integration: 7-Zip/WinRAR add to right-click menu, disable bloat ('Extract to <folder>' enough), clean up: Settings > Integration, remove WinZip (nagware, inferior to 7-Zip), Windows 11 native: right-click > 'Compress to ZIP'", "keywords": ["context menu", "right-click", "integration", "winzip"], "difficulty": "beginner", "tags": ["windows"], "related_tools": []}
            ]
        }

        # REMOTE_DESKTOP_GAMING
        kb["remote_desktop_gaming"] = {
            "metadata": {
                "priority": 4,
                "tags": ["remote-desktop", "gaming", "streaming", "parsec", "moonlight", "low-latency"],
                "difficulty": "intermediate",
                "description": "Low-latency remote desktop for gaming: Parsec, Moonlight, Steam Remote Play"
            },
            "tips": [
                {"content": "Parsec: Best for gaming (60fps, <10ms LAN latency), H.265 encoding, up to 4K60, free tier (personal use), Teams tier (hosting), NAT traversal (works anywhere), virtual controllers, use for couch gaming/remote work", "keywords": ["parsec", "low latency", "gaming", "h265", "4k"], "difficulty": "intermediate", "tags": ["parsec"], "related_tools": ["Parsec"]},
                {"content": "Moonlight: Open-source NVIDIA GameStream client, lowest latency (5-8ms LAN), 4K120 capable, NVIDIA GPU required (host), free, manual setup (add games), Android/iOS/Linux clients, use for NVIDIA users on LAN", "keywords": ["moonlight", "gamestream", "nvidia", "low latency"], "difficulty": "intermediate", "tags": ["moonlight", "nvidia"], "related_tools": ["Moonlight"]},
                {"content": "Steam Remote Play: Built into Steam, easy setup (no account needed), works on WAN/LAN, controller support, limited codec options (quality varies), free, good for Steam games only, Remote Play Together (local co-op online)", "keywords": ["steam remote play", "remote play together", "steam"], "difficulty": "beginner", "tags": ["steam"], "related_tools": ["Steam"]},
                {"content": "Sunshine: Open-source GameStream host, AMD/Intel GPU support (not just NVIDIA), Moonlight-compatible, manual setup (config files), AV1/H.265 encoding, use if no NVIDIA GPU but want Moonlight client, active development", "keywords": ["sunshine", "gamestream", "amd", "intel", "open-source"], "difficulty": "advanced", "tags": ["sunshine"], "related_tools": ["Sunshine", "Moonlight"]},
                {"content": "RDP vs gaming: Windows RDP (Remote Desktop) = terrible for gaming (30fps limit, high latency, no GPU acceleration), use Parsec/Moonlight instead, RDP OK for desktop work, enable in Windows Settings > Remote Desktop", "keywords": ["rdp", "remote desktop", "windows", "not gaming"], "difficulty": "beginner", "tags": ["rdp"], "related_tools": []},
                {"content": "Network requirements: LAN = 5GHz WiFi or Gigabit Ethernet (best), 100Mbps enough for 1080p60, WAN = 10-20Mbps upload (host), 5Mbps download (client), latency <50ms playable, <20ms ideal, use ethernet for host PC", "keywords": ["network", "bandwidth", "latency", "ethernet"], "difficulty": "intermediate", "tags": ["network"], "related_tools": []},
                {"content": "Parsec settings: H.265 codec (better quality), 10-30Mbps bitrate (LAN), VSync off (latency), Immersive Mode (fullscreen), host PC: enable Hosting (auto-start), port forwarding NOT needed (NAT traversal)", "keywords": ["parsec settings", "h265", "bitrate", "vsync"], "difficulty": "intermediate", "tags": ["parsec"], "related_tools": ["Parsec"]},
                {"content": "Moonlight settings: Stream settings > 1080p60 (balanced) or 4K60 (high-end), bitrate 20Mbps LAN, 10Mbps WAN, enable HDR if supported, VSync off, optimize game settings (NVIDIA Control Panel > Manage 3D Settings > max performance)", "keywords": ["moonlight settings", "bitrate", "1080p", "4k"], "difficulty": "intermediate", "tags": ["moonlight"], "related_tools": ["Moonlight"]},
                {"content": "Controller support: Parsec = virtual controllers (works everywhere), Moonlight = USB passthrough (lower latency), Steam Remote Play = Steam Controller API (best for Steam games), use wired controller for lowest latency", "keywords": ["controller", "gamepad", "usb", "latency"], "difficulty": "intermediate", "tags": ["controllers"], "related_tools": []},
                {"content": "Multi-monitor: Parsec supports multi-monitor (select display), Moonlight = primary monitor only (limitation), Steam Remote Play = single monitor, workaround: Windowed mode on host, DisplayFusion (virtual monitors)", "keywords": ["multi-monitor", "displays", "parsec"], "difficulty": "advanced", "tags": ["multi-monitor"], "related_tools": ["DisplayFusion"]},
                {"content": "Wake-on-LAN: Wake host PC remotely, enable in BIOS + Network Adapter properties (Magic Packet), Parsec desktop app (wake option), alternative: TeamViewer WoL, useful for headless gaming PC in closet", "keywords": ["wake-on-lan", "wol", "magic packet", "remote wake"], "difficulty": "intermediate", "tags": ["remote"], "related_tools": ["Parsec", "TeamViewer"]},
                {"content": "Performance tips: Host PC: Close background apps, Game Mode ON, latest GPU drivers, Client: Wired connection (or 5GHz WiFi close to router), close Chrome/Discord, hardware decoder if available, lower quality if laggy", "keywords": ["performance", "optimization", "game mode", "hardware decode"], "difficulty": "intermediate", "tags": ["optimization"], "related_tools": []}
            ]
        }

        # DUAL_BOOT_MANAGEMENT
        kb["dual_boot_management"] = {
            "metadata": {
                "priority": 4,
                "tags": ["dual-boot", "linux", "windows", "grub", "efi", "bootloader"],
                "difficulty": "advanced",
                "description": "Windows + Linux dual boot setup, GRUB bootloader, EFI partitions, troubleshooting"
            },
            "tips": [
                {"content": "Installation order: Install Windows FIRST, Linux SECOND (Windows overwrites bootloader), Linux installer (Ubuntu) auto-detects Windows and adds to GRUB menu, reverse order = manual GRUB repair (grub-install)", "keywords": ["installation order", "windows first", "grub", "bootloader"], "difficulty": "intermediate", "tags": ["setup"], "related_tools": []},
                {"content": "Partitioning: Separate drives easiest (select boot in BIOS), same drive: shrink Windows (Disk Management), create Linux partitions (/ root 50GB+, swap = RAM size, /home rest), leave Windows EFI partition (100MB)", "keywords": ["partitioning", "shrink", "efi", "root", "swap"], "difficulty": "intermediate", "tags": ["partitioning"], "related_tools": ["GParted"]},
                {"content": "GRUB bootloader: Linux bootloader, auto-detects OSes (os-prober), default boot Linux (change in /etc/default/grub GRUB_DEFAULT=saved, then grub-update), timeout 5-10 seconds (GRUB_TIMEOUT), theme customization available", "keywords": ["grub", "bootloader", "os-prober", "grub_default"], "difficulty": "intermediate", "tags": ["grub"], "related_tools": []},
                {"content": "EFI vs Legacy: Modern PCs = UEFI/EFI (GPT partition table), old PCs = Legacy BIOS (MBR), both OSes must use SAME mode (both UEFI or both Legacy), mismatch = OS won't boot, check in Disk Management (GPT or MBR)", "keywords": ["efi", "uefi", "legacy", "gpt", "mbr"], "difficulty": "intermediate", "tags": ["boot"], "related_tools": []},
                {"content": "EFI partition: 100-500MB FAT32 partition (/boot/efi), stores bootloaders (Windows Boot Manager, GRUB), shared between OSes, created by Windows installer, Linux uses existing EFI partition (select 'Use as EFI' in installer)", "keywords": ["efi partition", "fat32", "boot efi", "shared"], "difficulty": "advanced", "tags": ["partitioning"], "related_tools": []},
                {"content": "Boot order: BIOS/UEFI boot menu (F8/F10/F12 on startup), select Windows Boot Manager or GRUB, change default in BIOS (Boot tab), GRUB = shows all OSes, Windows Boot Manager = Windows only", "keywords": ["boot order", "bios", "boot menu", "f12"], "difficulty": "beginner", "tags": ["boot"], "related_tools": []},
                {"content": "Windows updates breaking GRUB: Windows updates can overwrite bootloader (rare), fix: Boot Linux live USB > chroot into Linux install > grub-install /dev/sda > update-grub, prevention: separate drives (select in BIOS)", "keywords": ["windows update", "grub repair", "chroot", "grub-install"], "difficulty": "advanced", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "Time sync issues: Windows uses local time, Linux uses UTC, causes time discrepancy, fix: Make Linux use local time 'timedatectl set-local-rtc 1 --adjust-system-clock' (recommended for dual boot), or make Windows use UTC (registry edit, complex)", "keywords": ["time sync", "utc", "local time", "timedatectl"], "difficulty": "intermediate", "tags": ["troubleshooting"], "related_tools": []},
                {"content": "Shared data partition: NTFS partition for files accessible from both OSes, Windows native NTFS support, Linux needs ntfs-3g (usually preinstalled), mount in /etc/fstab (auto-mount on boot), useful for documents/media", "keywords": ["shared partition", "ntfs", "ntfs-3g", "fstab"], "difficulty": "intermediate", "tags": ["file-sharing"], "related_tools": []},
                {"content": "Removing Linux: Delete Linux partitions (Windows Disk Management), fix bootloader: bootrec /fixmbr, bootrec /fixboot (Windows Recovery), or use EasyBCD (GUI tool), extends Windows partition to reclaim space (Disk Management)", "keywords": ["remove linux", "bootrec", "fixmbr", "easybcd"], "difficulty": "intermediate", "tags": ["uninstall"], "related_tools": ["EasyBCD"]},
                {"content": "Fast Startup issues: Windows Fast Startup (hybrid shutdown) locks NTFS partitions (read-only in Linux), causes issues accessing Windows files from Linux, disable: Power Options > Choose what power buttons do > Change settings > Uncheck Fast Startup", "keywords": ["fast startup", "hybrid shutdown", "ntfs", "read-only"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": []},
                {"content": "GRUB customization: Themes (grub-customizer GUI), change timeout/default OS (/etc/default/grub), hide GRUB (GRUB_TIMEOUT=0, hold Shift on boot to show), background images, custom menu entries for ISOs", "keywords": ["grub customization", "grub-customizer", "themes"], "difficulty": "intermediate", "tags": ["customization"], "related_tools": ["GRUB Customizer"]}
            ]
        }

        # SYSTEM_CLONING_MIGRATION
        kb["system_cloning_migration"] = {
            "metadata": {
                "priority": 4,
                "tags": ["cloning", "migration", "disk-imaging", "backup", "hdd-to-ssd"],
                "difficulty": "intermediate",
                "description": "Disk cloning and system migration: Macrium Reflect, HDD to SSD, bootable clones"
            },
            "tips": [
                {"content": "Macrium Reflect Free: Best free cloning tool, disk imaging + cloning, bootable rescue media (USB), incremental backups, clone HDD to SSD (auto-align partitions), verify clone, alternative: Clonezilla (open-source, complex UI)", "keywords": ["macrium reflect", "cloning", "disk imaging", "free"], "difficulty": "intermediate", "tags": ["macrium"], "related_tools": ["Macrium Reflect"]},
                {"content": "HDD to SSD migration: Clone entire disk (not just partition), destination SSD >= source used space (not total size), Macrium auto-resizes partitions, disconnect HDD after clone (boot from SSD first), boot order in BIOS if both connected", "keywords": ["hdd to ssd", "migration", "clone", "resize"], "difficulty": "intermediate", "tags": ["ssd"], "related_tools": ["Macrium Reflect"]},
                {"content": "Clone vs Image: Clone = exact copy (bootable immediately), Image = compressed backup file (.mrimg), restore image to new drive (useful for different size drives), clone faster for same-size drives, image for backup/restore", "keywords": ["clone", "image", "backup", "restore"], "difficulty": "intermediate", "tags": ["backup"], "related_tools": []},
                {"content": "Partition alignment: SSDs need 4K alignment (performance), Macrium auto-aligns, check after clone: msinfo32 > Components > Storage > Disks (Partition Starting Offset % 4096 = 0), misaligned = slow SSD", "keywords": ["partition alignment", "4k alignment", "ssd performance"], "difficulty": "advanced", "tags": ["optimization"], "related_tools": []},
                {"content": "Bootable rescue media: Create in Macrium (USB or ISO), boots WinPE environment (Windows-based), restore images, clone drives, fix boot issues, update rescue media after major Windows updates, keep USB handy", "keywords": ["rescue media", "bootable usb", "winpe", "recovery"], "difficulty": "intermediate", "tags": ["recovery"], "related_tools": ["Macrium Reflect"]},
                {"content": "System reserved partition: Windows creates 100-500MB partition (boot files), MUST be cloned (not just C:), Macrium 'Clone this disk' option (easier than selecting partitions), clone all partitions to avoid boot issues", "keywords": ["system reserved", "boot partition", "efi"], "difficulty": "intermediate", "tags": ["partitions"], "related_tools": []},
                {"content": "Clone verification: Macrium 'Verify Image/Clone' (MD5 checksum), ensure bootability before wiping source drive, test clone (boot from SSD, check files), keep source drive as backup for 1 week (verify stability)", "keywords": ["verification", "checksum", "md5", "verify"], "difficulty": "intermediate", "tags": ["verification"], "related_tools": ["Macrium Reflect"]},
                {"content": "Incremental backups: Macrium Reflect backup plans, full backup (first time) + incremental (only changes), saves space, schedule daily/weekly, restore chain (full + incrementals), backup to external HDD or NAS", "keywords": ["incremental backup", "backup plan", "schedule"], "difficulty": "intermediate", "tags": ["backup"], "related_tools": ["Macrium Reflect"]},
                {"content": "Larger to smaller drive: Clone 500GB HDD (200GB used) to 250GB SSD = OK, shrink source partitions BEFORE cloning (Disk Management), Macrium resizes automatically if space allows, data migration (move files to free space)", "keywords": ["larger to smaller", "shrink", "resize"], "difficulty": "advanced", "tags": ["migration"], "related_tools": ["Macrium Reflect"]},
                {"content": "Alternative tools: Clonezilla (free, open-source, bootable ISO, complex), Acronis True Image (paid, polished), Samsung Data Migration (Samsung SSDs only), Crucial/WD have brand-specific tools, Macrium best all-around", "keywords": ["clonezilla", "acronis", "samsung data migration"], "difficulty": "intermediate", "tags": ["alternatives"], "related_tools": ["Clonezilla", "Acronis"]},
                {"content": "Post-clone cleanup: Delete old backups on source drive, wipe source HDD (DBAN or diskpart clean), repurpose as data drive (reformat), check SSD TRIM enabled (fsutil behavior query DisableDeleteNotify = 0)", "keywords": ["cleanup", "wipe", "trim", "diskpart"], "difficulty": "intermediate", "tags": ["cleanup"], "related_tools": []},
                {"content": "UEFI/GPT vs BIOS/MBR: Clone must match (UEFI to UEFI, BIOS to BIOS), Macrium handles both, convert MBR to GPT: mbr2gpt.exe (Windows 10/11), GPT supports >2TB drives, UEFI required for modern features (Secure Boot)", "keywords": ["uefi", "gpt", "bios", "mbr", "mbr2gpt"], "difficulty": "advanced", "tags": ["boot"], "related_tools": []}
            ]
        }

        # WINDOWS_SANDBOX_SECURITY
        kb["windows_sandbox_security"] = {
            "metadata": {
                "priority": 4,
                "tags": ["sandbox", "security", "isolation", "testing", "windows"],
                "difficulty": "intermediate",
                "description": "Windows Sandbox, Sandboxie, isolated testing environments for untrusted software"
            },
            "tips": [
                {"content": "Windows Sandbox: Built-in Windows 10/11 Pro/Enterprise (NOT Home), isolated lightweight VM (discards all changes on close), clean OS every launch, enable: Windows Features > Windows Sandbox, requires virtualization (VT-x/AMD-V)", "keywords": ["windows sandbox", "isolated", "vm", "pro", "enterprise"], "difficulty": "intermediate", "tags": ["windows"], "related_tools": ["Windows Sandbox"]},
                {"content": "Windows Sandbox use cases: Test untrusted software (cracks, keygens, unknown EXEs), browse risky sites, open suspicious emails, testing scripts, all changes deleted on close (no persistence), fast startup (5-10 seconds)", "keywords": ["use cases", "untrusted software", "testing"], "difficulty": "beginner", "tags": ["security"], "related_tools": []},
                {"content": "Sandboxie: Third-party sandbox (free Classic, paid Plus), isolates apps in sandbox (changes to sandbox folder, not system), persistent sandbox (keep changes if needed), older but stable, Plus adds features (forced folders, better UI)", "keywords": ["sandboxie", "persistent", "sandbox folder", "classic"], "difficulty": "intermediate", "tags": ["sandboxie"], "related_tools": ["Sandboxie"]},
                {"content": "Sandbox configuration: Windows Sandbox .wsb config files (network on/off, shared folders, startup script), networking disabled by default (safer), share folder for file transfer, XML config with MappedFolder elements", "keywords": ["wsb config", "configuration", "mapped folder"], "difficulty": "advanced", "tags": ["configuration"], "related_tools": []},
                {"content": "Performance: Windows Sandbox uses Hyper-V (fast but requires 4GB+ RAM, 2 cores+), Sandboxie = lightweight (process isolation, not full VM), Sandbox better for full isolation, Sandboxie for performance", "keywords": ["performance", "hyper-v", "ram", "lightweight"], "difficulty": "intermediate", "tags": ["performance"], "related_tools": []},
                {"content": "Limitations: Windows Sandbox = no persistence (resets on close), no GPU acceleration (no gaming), Sandboxie = not full isolation (kernel exploits can escape), neither perfect for APTs (advanced persistent threats), use VM for serious malware analysis", "keywords": ["limitations", "persistence", "no gpu", "kernel exploits"], "difficulty": "advanced", "tags": ["limitations"], "related_tools": []},
                {"content": "File transfer: Windows Sandbox = shared folders (wsb config), copy/paste text works, drag/drop files (if enabled), Sandboxie = sandbox folder location in user profile, access sandbox files from host", "keywords": ["file transfer", "shared folders", "copy paste", "sandbox folder"], "difficulty": "intermediate", "tags": ["file-transfer"], "related_tools": []},
                {"content": "Browser sandboxing: Chrome/Edge = built-in sandbox (process isolation), Firefox = less sandboxed, use Windows Sandbox for extra layer (run browser in Sandbox), useful for downloading suspicious files (auto-deleted on close)", "keywords": ["browser", "chrome", "edge", "built-in sandbox"], "difficulty": "intermediate", "tags": ["browsers"], "related_tools": []},
                {"content": "Virtual machines alternative: VirtualBox/VMware = full isolation, snapshots (restore to clean state), portable (export VM), heavier (uses more RAM/CPU), use for persistent testing, Windows Sandbox for quick tests", "keywords": ["virtual machine", "virtualbox", "vmware", "snapshots"], "difficulty": "intermediate", "tags": ["alternatives"], "related_tools": ["VirtualBox", "VMware"]},
                {"content": "Sandboxie Plus features: Forced programs (auto-sandbox specific apps), forced folders (intercept file writes), app compartments (separate sandboxes per app), update checker, open-source, active development, free", "keywords": ["sandboxie plus", "forced programs", "forced folders"], "difficulty": "intermediate", "tags": ["sandboxie"], "related_tools": ["Sandboxie Plus"]},
                {"content": "Malware analysis: Windows Sandbox NOT for advanced malware (kernel exploits escape), use dedicated malware analysis VM (isolated network, no host sharing), tools: Process Monitor, Process Explorer, Wireshark, ANY.RUN (cloud sandbox)", "keywords": ["malware analysis", "process monitor", "wireshark"], "difficulty": "advanced", "tags": ["malware"], "related_tools": ["Process Monitor", "ANY.RUN"]},
                {"content": "Enable Windows Sandbox: Requirements: Windows 10/11 Pro/Enterprise, CPU virtualization enabled (BIOS), 4GB+ RAM, PowerShell (admin): Enable-WindowsOptionalFeature -Online -FeatureName 'Containers-DisposableClientVM', reboot", "keywords": ["enable", "powershell", "requirements", "virtualization"], "difficulty": "intermediate", "tags": ["setup"], "related_tools": []}
            ]
        }

'''

    file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

    # Lire le fichier
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver la position de "return kb"
    return_pos = content.find('        return kb')

    if return_pos == -1:
        print("ERROR: 'return kb' not found in file!")
        return False

    # Insérer les nouvelles catégories AVANT "return kb"
    new_content = content[:return_pos] + batch_4_code + '\n' + content[return_pos:]

    # Écrire le fichier modifié
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("[OK] Batch 4 categories added successfully!")
    return True


def test_import():
    """Test l'import et affiche les statistiques"""
    try:
        from ai_knowledge_unified import UnifiedKnowledgeBase

        kb = UnifiedKnowledgeBase()
        stats = kb.get_stats()

        print("\n" + "="*70)
        print("KNOWLEDGE BASE STATISTICS (After Batch 4)")
        print("="*70)
        print(f"Total Categories: {stats['total_categories']}")
        print(f"Total Tips: {stats['total_tips']}")
        print(f"\nProgress towards goal:")
        print(f"  Categories: {stats['total_categories']}/143 ({stats['total_categories']/143*100:.1f}%)")
        print(f"  Tips: {stats['total_tips']}/5000 ({stats['total_tips']/5000*100:.1f}%)")

        # Vérifier les nouvelles catégories
        batch_4_categories = [
            "networking_wifi_optimization",
            "networking_vpn_protocols",
            "virtualization_vmware_workstation",
            "virtualization_virtualbox",
            "wsl2_linux_windows",
            "development_git_workflow",
            "development_vscode_setup",
            "multimedia_video_encoding",
            "multimedia_obs_streaming",
            "file_management_tools",
            "compression_formats",
            "remote_desktop_gaming",
            "dual_boot_management",
            "system_cloning_migration",
            "windows_sandbox_security"
        ]

        print("\n" + "-"*70)
        print("BATCH 4 CATEGORIES VERIFICATION")
        print("-"*70)

        all_present = True
        for cat in batch_4_categories:
            if cat in kb.kb:
                tips_count = len(kb.kb[cat]["tips"])
                priority = kb.kb[cat]["metadata"]["priority"]
                print(f"[OK] {cat}: {tips_count} tips (priority {priority})")
            else:
                print(f"[FAIL] {cat}: MISSING!")
                all_present = False

        if all_present:
            print("\n[OK] All Batch 4 categories successfully added!")
        else:
            print("\n[FAIL] Some categories are missing!")

        return True

    except Exception as e:
        print(f"\n[ERROR] during import test: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("="*70)
    print("KNOWLEDGE BASE ENRICHMENT - BATCH 4")
    print("Adding 15 categories: Networking, Virtualization, Dev, Multimedia")
    print("="*70)

    # Ajouter les catégories
    if add_batch_4_categories():
        # Tester l'import
        test_import()
    else:
        print("\n[FAIL] Failed to add categories!")
