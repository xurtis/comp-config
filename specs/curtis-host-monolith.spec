Name:		curtis-host-monolith
Version:	1.1.4
Release:	1.multi
Summary:	Meta-package for installing software for host 'monolith'

Group:		Applications/System
License:	ISC
BuildArch:	noarch

Requires:	curtis-repos
Requires:	curtis-desk-full
Requires:	curtis-tools
Requires:	curtis-media
Requires:	curtis-av
Requires:	curtis-games
#Requires:	xorg-x11-drv-nvidia kmod-nvidia
Requires:	gstreamer1-plugins-bad-nvenc

%description
Package dependancies for tower

%prep

%build

%clean

%install

%files

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created initial package
