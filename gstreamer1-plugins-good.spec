Name:           gstreamer1-plugins-good
Version:        1.14.4
Release:        2
Summary:        Good code and licensing for GStreamer plugins 
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.xz
Source1:        gstreamer-good.appdata.xml
BuildRequires:  gcc-c++ gstreamer1-devel >= %{version} gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  flac-devel >= 1.1.4 gdk-pixbuf2-devel libjpeg-devel libpng-devel >= 1.2.0
BuildRequires:  libshout-devel libsoup-devel libX11-devel libXext-devel libXdamage-devel
BuildRequires:  libXfixes-devel orc-devel pulseaudio-libs-devel speex-devel taglib-devel
BuildRequires:  wavpack-devel libv4l-devel libvpx-devel >= 1.1.0 gtk3-devel >= 3.4
BuildRequires:  mesa-libGL-devel mesa-libGLES-devel mesa-libGLU-devel mesa-libEGL-devel
BuildRequires:  lame-devel mpg123-devel twolame-devel gtk-doc python2-devel libraw1394-devel
BuildRequires:  jack-audio-connection-kit-devel libavc1394-devel libdv-devel libiec61883-devel
Obsoletes:      gstreamer1-plugin-mpg123 < 1.13.1
Obsoletes:      gstreamer1-plugins-bad-free-gtk < 1.13.1-2
obsoletes:      gstreamer1-plugins-good-gtk < %{version}-%{release}
obsoletes:      gstreamer1-plugins-good-extras < %{version}-%{release}
Provides:       gstreamer1-plugin-mpg123 = %{version}-%{release}
Provides:       gstreamer1-plugins-good-extras = %{version}-%{release}
Provides:       gstreamer1-plugins-bad-free-gtk = %{version}-%{release}
Provides:       gstreamer1-plugins-good-gtk = %{version}-%{release}

%description
GStreamer is a framework for constructing graphs of various filters that will handle
streaming media. Any discrete (packetizable) media type is supported, with provisions
for automatically determining source type. Formatting/framing information is provided
with a powerful negotiation framework.

%prep
%autosetup -n gst-plugins-good-%{version}

%build
%configure --disable-silent-rules --disable-fatal-warnings \
  --with-package-name='GStreamer1-plugins-good package' \
  --with-package-origin='https://gstreamer.freedesktop.org/src/gst-plugins-good/' \
  --enable-experimental --enable-gtk-doc --enable-orc \
  --disable-monoscope --disable-aalib --disable-cairo \
  --disable-libcaca --disable-qt --with-default-visualizer=autoaudiosink\
  --enable-jack

%make_build V=1

%install
%make_install

mkdir -p %{buildroot}%{_metainfodir}/
cp %{SOURCE1} %{buildroot}%{_metainfodir}/gstreamer-good.appdata.xml
touch %{buildroot}%{_metainfodir}/gstreamer-good.appdata.xml

%delete_la

%find_lang gst-plugins-good-1.0

%files -f gst-plugins-good-1.0.lang
%doc AUTHORS README REQUIREMENTS COPYING
%{_metainfodir}/gstreamer-good.appdata.xml
%doc %{_datadir}/gtk-doc/html/gst-plugins-good-plugins-1.0
%dir %{_datadir}/gstreamer-1.0/presets/
%{_datadir}/gstreamer-1.0/presets/*
%{_libdir}/gstreamer-1.0/*.so

%changelog
* Tue Dec 03 2019 zhujunhao <zhujunhao5@huawei.com> - 1.14.4-2
- Package init
