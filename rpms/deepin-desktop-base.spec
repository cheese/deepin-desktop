Name:           deepin-desktop-base
Version:        2019.01.28
Release:        3%{?dist}
Summary:        Base component for Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-desktop-base
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Recommends:     deepin-wallpapers
Recommends:     deepin-screensaver
Recommends:     plymouth-theme-deepin

%description
This package provides some components for Deepin desktop environment.

- deepin logo
- deepin desktop version
- login screen background image
- language information

%package -n deepin-manual-directory
Summary:        Package that owns the Deepin manual directory

%description -n deepin-manual-directory
This package owns the Deepin manual directory. This is a workaround
before deepin-manual actually comes into Fedora to unblock packaging.

%prep
%setup -q

# Remove Deepin distro's lsb-release
# Don't override systemd timeouts
# Remove apt-specific templates
sed -i -E '/lsb-release|systemd|apt|back/d' Makefile

# Fix data path
sed -i 's|/usr/lib|%{_datadir}|' Makefile

# Set deepin type to Fedora
sed -i 's|Type=.*|Type=Fedora|; /Type\[/d' files/desktop-version.in

%build
%make_build

%install
%make_install

# Make a symlink for deepin-version
ln -sfv ..%{_datadir}/deepin/desktop-version %{buildroot}/etc/deepin-version

mkdir %{buildroot}/%{_datadir}/dman
echo "This package owns the Deepin manual directory. This is a workaround
before deepin-manual actually comes into Fedora to unblock packaging." > %{buildroot}%{_datadir}/dman/README.Fedora

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/appstore.json
%{_sysconfdir}/deepin-version
%dir %{_datadir}/deepin/
%{_datadir}/deepin/desktop-version
%dir %{_datadir}/distro-info/
%{_datadir}/distro-info/deepin.csv
%{_datadir}/i18n/i18n_dependent.json
%{_datadir}/i18n/language_info.json
%dir %{_datadir}/plymouth
%{_datadir}/plymouth/deepin-logo.png

%files -n deepin-manual-directory
%{_datadir}/dman

%changelog
* Wed Mar 13 2019 Robin Lee <cheeselee@fedoraproject.org> - 2019.01.28-3
- Recommends deepin-screensaver

* Fri Mar  8 2019 Robin Lee <cheeselee@fedoraproject.org> - 2019.01.28-2
- Set deepin type to Fedora
- Own some unowned directories

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 2019.01.28-1
- Update to 2019.01.28

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 2018.10.29-2
- Add plymouth-theme-deepin dependence

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 2018.10.29-1
- Update to 2018.10.29

* Sun Oct 28 2018 Zamir SUN <sztsian@gmail.com> - 2018.7.23-2
- Add subpackage deepin-manual-directory to temporary own dman dir.

* Mon Jul 23 2018 mosquito <sensor.wen@gmail.com> - 2018.7.23-1
- Update to 2018.7.23

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 2017.11.1-1
- Update to 2017.11.1

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 2016.13.1-1
- Update to 2016.13.1

* Sun Aug  6 2017 mosquito <sensor.wen@gmail.com> - 2016.12.6-1
- Rebuild

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 2016.12.6-1.git94a22cf
- Update to 2016.12.6

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 2016.11.30-1.gita0f52f3
- Update to 2016.11.30

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 2016.11.29-1.git477c9a7
- Update to 2016.11.29

* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.11.28-1
- Update package to version 2016.11.28

* Sat Dec 03 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.02.03-1
- Update package to version 2016.02.03

* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.02.02-1
- Initial package build
