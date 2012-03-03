Summary:	A graphical interface for modifying the keyboard
Summary(pl.UTF-8):	Graficzny interfejs do zmiany klawiatury
Name:		system-config-keyboard
Version:	1.3.1
Release:	0.10
License:	GPL v2+
Group:		Base
Source0:	https://fedorahosted.org/releases/s/y/system-config-keyboard/%{name}-%{version}.tar.gz
# Source0-md5:	012b1aec6d237f853bea6824e71d19ed
Patch0:		s-c-keyboard-do_not_remove_the_OK_button.patch
Patch1:		sck-1.3.1-no-pyxf86config.patch
URL:		https://fedorahosted.org/system-config-keyboard/
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	sed >= 4.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	firstboot >= 1.99
Requires:	gtk+2 >= 2:2.6
Requires:	python >= 1:2.0
Requires:	python-rhpl >= 0.53
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
system-config-keyboard is a graphical user interface that allows the
user to change the default keyboard of the system.

%description -l pl.UTF-8
system-config-keyboard to graficzny interfejs użytkownika
umożliwiający użytkownikowi zmianę domyślnej klawiatury w systemie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTROOT=$RPM_BUILD_ROOT


desktop-file-install --vendor system --delete-original \
	--dir $RPM_BUILD_ROOT%{_desktopdir} \
	--add-category Application \
	--add-category System \
	$RPM_BUILD_ROOT%{_desktopdir}/system-config-keyboard.desktop

sed -i 's/\.py/.pyc/' $RPM_BUILD_ROOT%{_sbindir}/system-config-keyboard

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_postclean %{_datadir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.apps/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/%{name}
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_sbindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py[co]
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/pixmaps/%{name}.png
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

%dir %{_datadir}/firstboot
%dir %{_datadir}/firstboot/modules
%{_datadir}/firstboot/modules/*.py

# python-%{name}
%dir %{py_sitescriptdir}/system_config_keyboard
%{py_sitescriptdir}/system_config_keyboard/*.py[co]
