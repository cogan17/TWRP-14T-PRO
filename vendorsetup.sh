# OrangeFox build settings for rothko; read by OrangeFox's build script, ignored by TWRP builds
if [ "$FOX_BUILD_DEVICE" = rothko ]; then
	# recovery lives in vendor_boot (fragment "recovery"), virtual A/B
	export FOX_VENDOR_BOOT_RECOVERY=1
	export FOX_AB_DEVICE=1
	export FOX_VIRTUAL_AB_DEVICE=1
	export FOX_USE_BASH_SHELL=1
	export FOX_USE_NANO_EDITOR=1
	export FOX_USE_TAR_BINARY=1
	export FOX_USE_SED_BINARY=1
	export OF_MAINTAINER=cogan17
	export FOX_BUILD_TYPE=Beta
fi
