%define major 5
%define libname %mklibname KF5XmlGui %{major}
%define devname %mklibname KF5XmlGui -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kxmlgui
Version:	5.112.0
Release:	2
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 XML GUI library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: cmake(Qt5UiPlugin)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
# For QCH format docs
BuildRequires: qt5-assistant
BuildRequires: doxygen
Requires: %{libname} = %{EVRD}
Obsoletes: kxmlgui-default-settings < 5.240.0-0.20230818.1

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

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%package designer
Summary: Qt Designer plugin for handling %{name} widgets
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description designer
Qt Designer plugin for handling %{name} widgets

%files designer
%{_libdir}/qt5/plugins/designer/*.so

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_datadir}/qlogging-categories5/*.*categories
%{_libdir}/libexec/kf5/ksendbugmail
%{_sysconfdir}/xdg/ui

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/cmake/KF5XmlGui

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
