subarch: amd64
version_stamp: 2018.11
target: livecd-stage1
rel_type: default
profile: default/linux/amd64/17.0
snapshot: 20181101
source_subpath: default/stage3-amd64-20181101



# The livecd-stage1 target is where you will build packages for your CD.  These
# packages can be built with customized USE settings.  The settings here are
# additive to the default USE configured by the profile.  For building release
# media, the first thing we do is disable all default USE flags with -* and then
# begin to set our own.
# example:
# livecd/use: -* ipv6 socks5 livecd fbcon ncurses readline ssl
livecd/use: livecd

# This is the set of packages that we will merge into the CD's filesystem.  They
# will be built with the USE flags configured above.  These packages must not
# depend on a configured kernel.  If the package requires a configured kernel,
# then it will be defined elsewhere.
# example:
#livecd/packages: livecd-tools dhcpcd acpid apmd gentoo-sources coldplug fxload irssi gpm syslog-ng parted links raidtools dosfstools nfs-utils jfsutils xfsprogs e2fsprogs reiserfsprogs ntfsprogs pwgen rp-pppoe screen mirrorselect penggy iputils hwdata-knoppix hwsetup lvm2 evms vim pptpclient mdadm ethtool wireless-tools prism54-firmware wpa_supplicant
livecd/packages: app-admin/pwgen app-misc/livecd-tools net-misc/dhcpcd sys-apps/baselayout sys-apps/hwsetup

#livecd/cdtar
