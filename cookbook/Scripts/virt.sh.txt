#!/usr/bin/env bash

## Purpose: Use this script to quickly get kvm/virsh installed and working after a steamos update. I like having VM capability on
## my steamdeck since the deck is a powerfull and portable pc. However, I don't want to mess with the underlying OS much since
## I want it to recieve updates correctly.
## Created On: 08/24/2024
## Created by: N
## Version: 1.0
## License: GPL

##**Note** Go up to set 4 if you are just trying to re-install after a new steamdeck Update
##all of your VMS/virsh configs will be perserved since I'm pretty sure all that stuff
##lives in /etc

## MAIN Function
main() {

    message 1 "SELECT AN OPTION"
    message 1 "1 = enable_ssh"
    message 1 "2 = install_kvm"
    message 1 "3 = config_default_network"
    message 1 "4 = add_kernel_mods"
    message 1 "5 = manually provision new vm"
    message 1 "Any Other Option to Exit!"

    select CHOICE in {1..5}; do 

        case $CHOICE in

            1)
                enable_ssh
                ;;
            2)
                install_kvm
                ;;
            3)
                config_default_network
                ;;
            4)
                add_kernel_mods
                ;;
            5) 
                provision_vm
                ;;
            *)
                message 4 "GOODBYE"
                break
                ;;

        esac

    done 

}


## Functions

##It seems after a new steam update, ssh is automatically turned off, so this will enabled it
enable_ssh() {

    systemctl enable sshd
    systemctl start sshd

}

install_kvm() {

    steamos-readonly disable
    pacman-key --init
    pacman-key --populate archlinux holo
    message 1 "Use 1, then yes for everything. There might be an error displayed, but it shouldn't be too much of an issue"
    read -p ""
## Note: I need the overides because when SteamOS updates it removes all extra packages outside of its image, HOWEVER "/etc" is 
## preserved, so when pacman tries to install libvirt again, it finds a bunch of files already in place and then panics. Therefore
## I need to overwrite these files in order to succeed in the re-install of kvm/libvirt
pacman -S \
--overwrite *vte.csh \
--overwrite *vte.sh \
--overwrite *daxctl.example.conf \
--overwrite *monitor.conf \
--overwrite *ndctl.conf \
--overwrite *keys.readme \
--overwrite *asyncrecv.rc \
--overwrite *closemachine.rc \
--overwrite *openmachine.rc \
--overwrite *sendcmd.rc \
--overwrite *vdecmd \
--overwrite *fakeroot.conf \
--overwrite *cache-mq.profile \
--overwrite *cache-smq.profile \
--overwrite *command_profile_template.profile \
--overwrite *lvmdbusd.profile \
--overwrite *metadata_profile_template.profile \
--overwrite *thin-generic.profile \
--overwrite *thin-performance.profile \
--overwrite *vdo-small.profile \
--overwrite *guestfs_php.ini \
virt-manager virt-viewer qemu qemu-arch-extra edk2-ovmf vde2 ebtables dnsmasq bridge-utils openbsd-netcat libguestfs
    systemctl enable libvirtd.service
    systemctl start libvirtd.service
    systemctl status libvirtd.service
    steamos-readonly enable

}

## This will reload the firewall to allow libvirt to do stuff (rules should have been put in place during install,
## but not applied yet) as well as sets the default network to default. Note: the default network is internal on only
## used for nat and access internally. The bridge that should be setup, will be the actual external facing nic, thus
## each VM will have two nics. Moreover, the bridge will be added to the VM via an import xml or upon it's creation
## (or modification of the xml)
config_default_network() {

    firewall-cmd --reload
    virsh net-start default
    virsh net-autostart default

}

## This adds the correct kernel mods for virtio to work
## You might need to do this for every reboot, but I'm
## not sure
add_kernel_mods() {

    modprobe -a virtio-net virtio-blk virtio-scsi virtio-balloon
    lsmod | grep virtio

}

## This will create a new VM and mount the install iso into it's drive.
## This will be a quick way to build a new systems if you do not want to automate
## You will select all the parameters as defined by script
## Note: Vagrant does this better if you already have a box provisioned, so for 
## mass box/vm deployment use that. This is really just for quick and dirty installs
## of Kali or other custom os'es.
## You will be prompted for the full path location of the ISO as well as the pool to use for
## the qcow creation

provision_vm() {

message 1 "Please Specify Full ISO path"
read -e -p "" ISOPATH

if [[ ! -e ${ISOPATH} ]]; then

    message 3 "Could Not Find ISO PATH!"
    return 1

fi    

message 1 "Please Specify Name Of New VM (no spaces)"
read -p "" VMNAME

message 1 "Here is the OS list, please choose which OS you want to use (Press Enter)"
read -p ""
osinfo-query os | vim -
message 1 "Please Specify your OS Type"
read -p "" OSSELECT

message 1 "Please Specify Size Of Main HD in GB (it will be in qcow format)"
read -p "" VMHDSIZE

virsh pool-list

message 1 "Please Specify which Storage Pool You Would Like To Save HD To"
read -p "" VMSTORAGEPOOL

message 1 "Please Specify Number Of CPUs"
read -p "" VMCPUS

message 1 "Please Specify Memory In MB (2048, 1024, etc)"
read -p "" VMRAM

ip -c a sh
message 1 "Please Specify The Network Bridge you would like to use (leave blank for now bridge)"
message 1 "Also, a default network is created every time, so you will always have a nat connection"
read -p "" VMBRIDGE

if [[ -z ${VMBRIDGE} ]]; then

    VMBRIDGE=""

else

    VMBRIDGE="--network bridge=${VMBRIDGE},model=virtio "
fi

message 2 "-----------------------------------"
message 1 ${ISOPATH}
message 1 ${VMNAME}
message 1 ${OSSELECT}
message 1 ${VMHDSIZE}
message 1 ${VMSTORAGEPOOL}
message 1 ${VMCPUS}
message 1 ${VMRAM}
message 1 "${VMBRIDGE}"
message 2 "Is this correct?[Y/n]"
read -p "" YEP

if [[ ${YEP} == "Y" ]]; then

message 1 "Starting VMCreation"

virt-install \
--virt-type kvm \
--name ${VMNAME} \
--memory ${VMRAM} \
--vcpus ${VMCPUS} \
--os-variant ${OSSELECT} \
--hvm \
--cdrom ${ISOPATH} \
--network network=default,model=virtio \
${VMBRIDGE}\
--graphics vnc \
--disk pool=${VMSTORAGEPOOL},size=${VMHDSIZE},format=qcow2,sparse=true,bus=virtio

else

message 3 "Wrong Information, please run again!!!"


fi 


}

## Todo Todo
## Note: Do not use this funciton until
## It is fixed to work correctly!
## I really just have this here if I would ever
## need to build a bridge for my steam deck and
## I don't have my notes
build_brige() {

    ## Check to see if you already have a bridge
    nmcli con show --active

    ## Create Bridge Interface
    nmcli con add ifname virb0 type bridge con-name virb0

    ## Link Bridge Interface to Real Interface
    ## This assumes you have only one physical ethernet card
    ETHCARD=$(nmcli dev status | grep ethernet | cut -d ' ' -f1)
    nmcli con addd type bridge-slave ifname ${ETHCARD} master virb0

    ## Remove Spanning Tree Config
    nmcli con modify virb0 bridge.stp no

    ##Add Static IP Information so you can access the physical host (if you have only one ethernet)
    ## This can also be configured for DHCP, though some posts on the internet say not to do this
    ## Also I don't think you need an acutal IP for this if just want the IPs addresses of what is connected to the bridge

    nmcli con modify virb0 ipv4.addresses '192.0.2.1/24' ipv4.gateway '192.0.2.254' ipv4.dns '192.0.2.253' ipv4.dns-search 'example.com' ipv4.method manual
    
    ## In order for changes to take effect, you need to bring connection down then up and then restart NetworkManager Service
    nmcli con down ${ETHCARD}
    nmcli con up ${ETHCARD}
    systemctl restart NetworkManager.service

}

## Utility Functions


message() {

    local BLUE='\033[96m'
    local YELLOW='\033[33m'
    local GREEN='\033[0;32m'
    local RED='\033[0;31m'
    local NC='\033[0m'

    case "${1}" in

        1)
            echo -e "${BLUE}<INFO> ${2}${NC}"
            ;;
        2)
            echo -e "${YELLOW}<WARN> ${2}${NC}"
            ;;
        3) 
            echo -e "${RED}<ERROR> ${2}${NC}"
            ;;
        *)
            echo -e "${GREEN}${2}${NC}"

  esac


}

## START SCRIPT

set -o errexit
set -o nounset
set -o pipefail


if [[ "${TRACE-0}" -eq "1" ]]; then

  set -o xtrace

fi


if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then

  message 1 "Usage: ${0}"
  exit 0

fi

main
