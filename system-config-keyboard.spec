Summary:	A graphical interface for modifying the keyboard
Summary(pl.UTF-8):	Graficzny interfejs do zmiany klawiatury
Name:		system-config-keyboard
Version:	1.2.15
Release:	1
License:	GPL
Group:		Base
# https://fedorahosted.org/releases/s/y/system-config-keyboard/ (not yet)
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	13a0e4444f7fcbb6a3e9c88f42285faf
Patch1:		%{name}-beenset.patch
Patch2:		%{name}-fixcomments.patch
URL:		https://fedorahosted.org/system-config-keyboard/
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	intltool
Requires:	firstboot >= 1.99
Requires:	gtk+2 >= 2:2.6
Requires:	python >= 1:2.0
Requires:	python-rhpl >= 0.53
Requires:	python-xf86config
BuildArch:	noarch
ExclusiveOS:	Linux
ExcludeArch:	s390 s390x ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
system-config-keyboard is a graphical user interface that allows the
user to change the default keyboard of the system.

%description -l pl.UTF-8
system-config-keyboard to graficzny interfejs użytkownika
umożliwiający użytkownikowi zmianę domyślnej klawiatury w systemie.

%prep
%setup -q
%patch1 -p1
%patch2 -p0

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTROOT=$RPM_BUILD_ROOT

desktop-file-install --vendor system --delete-original \
	--dir $RPM_BUILD_ROOT%{_desktopdir} \
	--add-category Application \
	--add-category System \
	$RPM_BUILD_ROOT%{_desktopdir}/system-config-keyboard.desktop

%py_comp $RPM_BUILD_ROOT%{_datadir}/system-config-keyboard
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/system-config-keyboard
%py_postclean %{_datadir}/system-config-keyboard

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
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.apps/system-config-keyboard
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/system-config-keyboard
%attr(755,root,root) %{_sbindir}/system-config-keyboard
%dir %{_datadir}/system-config-keyboard
%{_datadir}/system-config-keyboard/*
%dir %{_datadir}/firstboot
%dir %{_datadir}/firstboot/modules
%{_datadir}/firstboot/modules/*
%{_desktopdir}/system-config-keyboard.desktop
%{_iconsdir}/hicolor/48x48/apps/system-config-keyboard.png
