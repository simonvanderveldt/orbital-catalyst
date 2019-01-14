subarch: amd64
version_stamp: 2018.11
target: livecd-stage2
rel_type: default
profile: default/linux/amd64/17.0
snapshot: 20181101
source_subpath: default/livecd-stage1-amd64-2018.11

portage_confdir: /home/simon/src/simonvanderveldt/orbital-catalyst/portage

livecd/fstype: squashfs
livecd/cdtar: /usr/share/catalyst/livecd/cdtar/isolinux-3.72-cdtar.tar.bz2
livecd/iso: orbital-2018.11.iso
livecd/type: generic-livecd
livecd/volid: Orbital 2018.11
livecd/rcadd: docker|default

# Will probably need these
# livecd/readme
# livecd/motd

# Not sure if we need these
#livecd/fsscript: @REPO_DIR@/releases/latest/scripts/livecd.sh
#livecd/overlay: @REPO_DIR@/releases/latest/overlays/common/overlay/livecd


boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /home/simon/src/simonvanderveldt/orbital-catalyst/kernel.config
boot/kernel/gentoo/packages:
	sys-fs/zfs
  app-emulation/docker
  app-emulation/docker-compose

#boot/kernel/gentoo/use: atm png truetype usb

livecd/bootargs: nosound

livecd/rcadd: docker|default docker-compose-autostart|default

livecd/empty:
	/var/tmp
	/var/empty
	/var/cache/edb/dep
	/tmp
	/usr/portage
	/usr/src

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2

#livecd/unmerge:
#  app-misc/livecd-tools

livecd/root_overlay: overlays/orbital
