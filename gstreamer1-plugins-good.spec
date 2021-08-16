%bcond_with extras
%bcond_with qt

Name:		    gstreamer1-plugins-good		
Version:	    1.16.2
Release:	    3
Summary:	    GStreamer plugins with good code and licensing
License:	    LGPLv2+	
URL:		    http://gstreamer.freedesktop.org/
Source0:	    http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.xz
Source1:	    gstreamer-good.appdata.xml

Patch6000:          backport-CVE-2021-3497.patch
Patch6001:          backport-CVE-2021-3498.patch

BuildRequires:	gcc gcc-c++ gstreamer1-devel gstreamer1-plugins-base-devel flac-devel
BuildRequires:  gdk-pixbuf2-devel libjpeg-devel libpng-devel libshout-devel orc-devel
BuildRequires:  libsoup-devel libX11-devel libXext-devel libXdamage-devel libXfixes-devel
BuildRequires:  pulseaudio-libs-devel speex-devel taglib-devel wavpack-devel libv4l-devel
BuildRequires:  libvpx-devel gtk3-devel mesa-libGL-devel libglvnd-devel lame-devel
BuildRequires:  mesa-libEGL-devel mesa-libGLU-devel mpg123-devel twolame-devel libdv-devel
BuildRequires:  libavc1394-devel libiec61883-devel libraw1394-devel gtk-doc

Provides:       gstreamer1-plugins-mpg123 = %{version}-%{release}
Obsoletes:   	gstreamer1-plugins-mpg123 < %{version}-%{release}

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.

%package	 	gtk
Summary:		gtk plugin for gstreamer1-plugins-good
Requires:		%{name} = %{version}-%{release}
Provides:		gstreamer1-plugins-bad-free-gtk = %{version}-%{release}
Obsoletes:		gstreamer1-plugins-bad-free-gtk < %{version}-%{release}

%description    gtk
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.

%package_help

%prep
%autosetup -n gst-plugins-good-%{version} -p1

%build
%configure --disable-silent-rules --disable-fatal-warnings --enable-experimental \
           --enable-gtk-doc --enable-orc --disable-monoscope --disable-aalib \
           --disable-cairo --disable-libcaca --disable-jack  \
           --with-default-visualizer=autoaudiosink 

%make_build

%install
%make_install 
%delete_la_and_a
install -p -D %{SOURCE1} %{buildroot}%{_metainfodir}/gstreamer-good.appdata.xml

%files 
%defattr(-,root,root)
%doc AUTHORS 
%license COPYING
%{_libdir}/gstreamer-1.0/*.so
%{_datadir}/locale/*
%dir %{_datadir}/gstreamer-1.0/presets 
%{_datadir}/gstreamer-1.0/presets/*.prs
%{_metainfodir}/gstreamer-good.appdata.xml
%exclude %{_libdir}/gstreamer-1.0/libgstgtk.so

%files 		gtk
%defattr(-,root,root)
%{_libdir}/gstreamer-1.0/libgstgtk.so

%files		help
%defattr(-,root,root)
%doc README REQUIREMENTS
%doc %{_datadir}/gtk-doc/html/*

%changelog
* Mon Aug 16 2021 yanglu <yanglu72@huawei.com> - 1.16.2-3
- Type:cves
- ID:CVE-2021-3497 CVE-2021-3498
- SUG:NA
- DESC:fix CVE-2021-3497 CVE-2021-3498

* Thu Oct 29 2020 gaihuiying <gaihuiying1@huawei.com> - 1.16.2-2
- Type:requirement
- ID:NA
- SUG:NA
- DESC:remove python2

* Thu Aug 06 2020 yuboyun <yuboyun@huawei.com> - 1.16.2-1
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:update to 1.16.2

* Fri Mar 6 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.14.4-3
- Package init
