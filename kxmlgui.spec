%define major 5
%define libname %mklibname KF5XmlGui %{major}
%define devname %mklibname KF5XmlGui -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kxmlgui
Version: 5.5.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 XML GUI library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 XML GUI library.

%package -n %{libname}
Summary: The KDE Frameworks 5 XML GUI library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The KDE Frameworks 5 XML GUI library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build
%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_sysconfdir}/xdg/ui
%{_libdir}/libexec/kf5/ksendbugmail
%{_datadir}/kf5/kxmlgui

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/cmake/KF5XmlGui
