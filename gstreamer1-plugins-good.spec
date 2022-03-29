%bcond_with extras
%bcond_with qt

Name:		    gstreamer1-plugins-good
Version:	    1.19.3
Release:	    1
Summary:	    GStreamer plugins with good code and licensing
License:	    LGPLv2+	
URL:		    http://gstreamer.freedesktop.org/
Source0:	    http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.xz
Source1:	    gstreamer-good.appdata.xml

BuildRequires:	gcc gcc-c++ gstreamer1-devel gstreamer1-plugins-base-devel flac-devel
BuildRequires:  gdk-pixbuf2-devel libjpeg-devel libpng-devel libshout-devel orc-devel
BuildRequires:  libsoup-devel libX11-devel libXext-devel libXdamage-devel libXfixes-devel
BuildRequires:  pulseaudio-libs-devel speex-devel taglib-devel wavpack-devel libv4l-devel
BuildRequires:  libvpx-devel gtk3-devel mesa-libGL-devel libglvnd-devel lame-devel
BuildRequires:  mesa-libEGL-devel mesa-libGLU-devel mpg123-devel twolame-devel libdv-devel
BuildRequires:  libavc1394-devel libiec61883-devel libraw1394-devel
BuildRequires:  chrpath nasm libgudev-devel meson >= 0.48.0

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

%package qt
Summary:         GStreamer "good" plugins qt qml plugin
Requires:        %{name}%{?_isa} = %{version}-%{release}
 
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5WaylandClient)

Supplements: (gstreamer1-plugins-good and qt5-qtdeclarative)
 
%description qt
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.
 
GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.
 
This package (%{name}-qt) contains the qtsink output plugin.

%package extras
Summary:        Extra GStreamer plugins with good code and licensing
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description extras
GStreamer is a streaming media framework, based on graphs of filters
which operate on media data.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.

%{name}-extras contains extra "good" plugins
which are not used very much and require additional libraries
to be installed.

%package help
Summary:        Gstreamer readme and helps.

%description help
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

%prep
%setup -q -n gst-plugins-good-%{version}

%build
%meson \
  -D doc=disabled \
  -D gtk_doc=disabled \
  -D orc=enabled \
  -D monoscope=disabled \
  -D aalib=disabled \
  -D libcaca=disabled \
  -D jack=disabled \
  -D rpicamsrc=disabled

%meson_build

%install
%meson_install
%delete_la_and_a

install -p -D %{SOURCE1} %{buildroot}%{_metainfodir}/gstreamer-good.appdata.xml

mkdir -p %{buildroot}/etc/ld.so.conf.d
echo "%{_libdir}" > %{buildroot}/etc/ld.so.conf.d/%{name}-%{_arch}.conf

%ldconfig_scriptlets

%files
%defattr(-,root,root)
%doc AUTHORS 
%license COPYING
%{_metainfodir}/gstreamer-good.appdata.xml
%config(noreplace) /etc/ld.so.conf.d/*

%dir %{_datadir}/gstreamer-1.0/presets/
%{_datadir}/gstreamer-1.0/presets/GstVP8Enc.prs
%{_datadir}/gstreamer-1.0/presets/GstIirEqualizer10Bands.prs
%{_datadir}/gstreamer-1.0/presets/GstIirEqualizer3Bands.prs
%{_datadir}/gstreamer-1.0/presets/GstQTMux.prs
%{_datadir}/locale/*/LC_MESSAGES/gst-plugins-good-1.0.mo

%{_libdir}/gstreamer-1.0/libgstalaw.so
%{_libdir}/gstreamer-1.0/libgstalphacolor.so
%{_libdir}/gstreamer-1.0/libgstalpha.so
%{_libdir}/gstreamer-1.0/libgstapetag.so
%{_libdir}/gstreamer-1.0/libgstaudiofx.so
%{_libdir}/gstreamer-1.0/libgstaudioparsers.so
%{_libdir}/gstreamer-1.0/libgstauparse.so
%{_libdir}/gstreamer-1.0/libgstautodetect.so
%{_libdir}/gstreamer-1.0/libgstavi.so
%{_libdir}/gstreamer-1.0/libgstcutter.so
%{_libdir}/gstreamer-1.0/libgstdebug.so
%{_libdir}/gstreamer-1.0/libgstdeinterlace.so
%{_libdir}/gstreamer-1.0/libgstdtmf.so
%{_libdir}/gstreamer-1.0/libgsteffectv.so
%{_libdir}/gstreamer-1.0/libgstequalizer.so
%{_libdir}/gstreamer-1.0/libgstflv.so
%{_libdir}/gstreamer-1.0/libgstflxdec.so
%{_libdir}/gstreamer-1.0/libgstgoom2k1.so
%{_libdir}/gstreamer-1.0/libgstgoom.so
%{_libdir}/gstreamer-1.0/libgsticydemux.so
%{_libdir}/gstreamer-1.0/libgstid3demux.so
%{_libdir}/gstreamer-1.0/libgstimagefreeze.so
%{_libdir}/gstreamer-1.0/libgstinterleave.so
%{_libdir}/gstreamer-1.0/libgstisomp4.so
%{_libdir}/gstreamer-1.0/libgstlevel.so
%{_libdir}/gstreamer-1.0/libgstmatroska.so
%{_libdir}/gstreamer-1.0/libgstmulaw.so
%{_libdir}/gstreamer-1.0/libgstmultifile.so
%{_libdir}/gstreamer-1.0/libgstmultipart.so
%{_libdir}/gstreamer-1.0/libgstnavigationtest.so
%{_libdir}/gstreamer-1.0/libgstoss4.so
%{_libdir}/gstreamer-1.0/libgstreplaygain.so
%{_libdir}/gstreamer-1.0/libgstrtp.so
%{_libdir}/gstreamer-1.0/libgstrtsp.so
%{_libdir}/gstreamer-1.0/libgstshapewipe.so
%{_libdir}/gstreamer-1.0/libgstsmpte.so
%{_libdir}/gstreamer-1.0/libgstspectrum.so
%{_libdir}/gstreamer-1.0/libgstudp.so
%{_libdir}/gstreamer-1.0/libgstvideobox.so
%{_libdir}/gstreamer-1.0/libgstvideocrop.so
%{_libdir}/gstreamer-1.0/libgstvideofilter.so
%{_libdir}/gstreamer-1.0/libgstvideomixer.so
%{_libdir}/gstreamer-1.0/libgstwavenc.so
%{_libdir}/gstreamer-1.0/libgstwavparse.so
%{_libdir}/gstreamer-1.0/libgstximagesrc.so
%{_libdir}/gstreamer-1.0/libgsty4menc.so

%{_libdir}/gstreamer-1.0/libgstcairo.so
%{_libdir}/gstreamer-1.0/libgstflac.so
%{_libdir}/gstreamer-1.0/libgstgdkpixbuf.so
%{_libdir}/gstreamer-1.0/libgstjpeg.so
%{_libdir}/gstreamer-1.0/libgstossaudio.so
%{_libdir}/gstreamer-1.0/libgstpng.so
%{_libdir}/gstreamer-1.0/libgstpulseaudio.so
%{_libdir}/gstreamer-1.0/libgstrtpmanager.so
%{_libdir}/gstreamer-1.0/libgstshout2.so
%{_libdir}/gstreamer-1.0/libgstsoup.so
%{_libdir}/gstreamer-1.0/libgstspeex.so
%{_libdir}/gstreamer-1.0/libgsttaglib.so
%{_libdir}/gstreamer-1.0/libgstvideo4linux2.so
%{_libdir}/gstreamer-1.0/libgstvpx.so
%{_libdir}/gstreamer-1.0/libgstwavpack.so
%{_libdir}/gstreamer-1.0/libgstlame.so
%{_libdir}/gstreamer-1.0/libgstmpg123.so
%{_libdir}/gstreamer-1.0/libgsttwolame.so

%files extras
#%%{_libdir}/gstreamer-1.0/libgstjack.so
%{_libdir}/gstreamer-1.0/libgstdv.so
%{_libdir}/gstreamer-1.0/libgst1394.so

%files 		gtk
%defattr(-,root,root)
%{_libdir}/gstreamer-1.0/libgstgtk.so

%files    qt
%{_libdir}/gstreamer-1.0/libgstqmlgl.so

%files		help
%defattr(-,root,root)
%doc README REQUIREMENTS
%if 0
%doc %{_datadir}/gtk-doc/html/*
%endif

%changelog
* Tue Mar 29 2022 Jiacheng Zhou <jchzhou@outlook.com> - 1.19.3-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:Upgrade to 1.19.3 to match gst version

* Fri Sep 10 2021 gaihuiying <gaihuiying1@huawei.com> - 1.16.2-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:remove rpath of libgstshout2.so

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
