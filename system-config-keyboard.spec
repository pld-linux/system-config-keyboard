Summary:	A graphical interface for modifying the keyboard
Name:		system-config-keyboard
Version:	1.2.7
Release:	0.3
License:	GPL
Group:		Base
URL:		http://fedora.redhat.com/projects/config-tools
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	625462272563a04e917229c1a06fd372
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	intltool
Requires:	gtk+2 >= 2:2.6
Requires:	python >= 1:2.0
Requires:	python-xf86config
Requires:	python-rhpl >= 0.53
Requires:	firstboot
#Requires:	usermode >= 1.36
BuildArch:	noarch
ExclusiveOS:	Linux
ExcludeArch:	s390 s390x ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
system-config-keyboard is a graphical user interface that allows the
user to change the default keyboard of the system.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTROOT=$RPM_BUILD_ROOT

desktop-file-install --vendor system --delete-original      \
  --dir $RPM_BUILD_ROOT%{_desktopdir}             \
  --add-category Application \
  --add-category SystemSetup \
  --add-category X-Red-Hat-Base          \
  $RPM_BUILD_ROOT%{_desktopdir}/system-config-keyboard.desktop

%py_comp $RPM_BUILD_ROOT/usr/share/system-config-keyboard
%py_ocomp $RPM_BUILD_ROOT/usr/share/system-config-keyboard
%py_postclean /usr/share/system-config-keyboard

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if 0
%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
	gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
	gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi
%endif

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/system-config-keyboard
%dir /usr/share/system-config-keyboard
/usr/share/system-config-keyboard/*
%dir /usr/share/firstboot/
%dir /usr/share/firstboot/modules
/usr/share/firstboot/modules/*
%attr(644,root,root) %{_desktopdir}/system-config-keyboard.desktop
%attr(644,root,root) %config /etc/security/console.apps/system-config-keyboard
%attr(644,root,root) %config /etc/pam.d/system-config-keyboard
%attr(644,root,root) %{_iconsdir}/hicolor/48x48/apps/system-config-keyboard.png
