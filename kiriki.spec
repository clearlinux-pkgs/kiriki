#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kiriki
Version  : 19.12.3
Release  : 19
URL      : https://download.kde.org/stable/release-service/19.12.3/src/kiriki-19.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.3/src/kiriki-19.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.3/src/kiriki-19.12.3.tar.xz.sig
Summary  : An addictive and fun dice game
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kiriki-bin = %{version}-%{release}
Requires: kiriki-data = %{version}-%{release}
Requires: kiriki-license = %{version}-%{release}
Requires: kiriki-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the kiriki package.
Group: Binaries
Requires: kiriki-data = %{version}-%{release}
Requires: kiriki-license = %{version}-%{release}

%description bin
bin components for the kiriki package.


%package data
Summary: data components for the kiriki package.
Group: Data

%description data
data components for the kiriki package.


%package doc
Summary: doc components for the kiriki package.
Group: Documentation

%description doc
doc components for the kiriki package.


%package license
Summary: license components for the kiriki package.
Group: Default

%description license
license components for the kiriki package.


%package locales
Summary: locales components for the kiriki package.
Group: Default

%description locales
locales components for the kiriki package.


%prep
%setup -q -n kiriki-19.12.3
cd %{_builddir}/kiriki-19.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583447927
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1583447927
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kiriki
cp %{_builddir}/kiriki-19.12.3/COPYING %{buildroot}/usr/share/package-licenses/kiriki/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kiriki-19.12.3/COPYING.DOC %{buildroot}/usr/share/package-licenses/kiriki/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang kiriki

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kiriki

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kiriki.desktop
/usr/share/icons/hicolor/128x128/apps/kiriki.png
/usr/share/icons/hicolor/16x16/apps/kiriki.png
/usr/share/icons/hicolor/22x22/apps/kiriki.png
/usr/share/icons/hicolor/32x32/apps/kiriki.png
/usr/share/icons/hicolor/48x48/apps/kiriki.png
/usr/share/icons/hicolor/64x64/apps/kiriki.png
/usr/share/kiriki/images/dice-1.png
/usr/share/kiriki/images/dice-2.png
/usr/share/kiriki/images/dice-3.png
/usr/share/kiriki/images/dice-4.png
/usr/share/kiriki/images/dice-5.png
/usr/share/kiriki/images/dice-6.png
/usr/share/kiriki/images/dice-none.png
/usr/share/kxmlgui5/kiriki/kirikiui.rc
/usr/share/metainfo/org.kde.kiriki.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kiriki/index.cache.bz2
/usr/share/doc/HTML/de/kiriki/index.docbook
/usr/share/doc/HTML/en/kiriki/configuration.png
/usr/share/doc/HTML/en/kiriki/gameboard.png
/usr/share/doc/HTML/en/kiriki/index.cache.bz2
/usr/share/doc/HTML/en/kiriki/index.docbook
/usr/share/doc/HTML/es/kiriki/index.cache.bz2
/usr/share/doc/HTML/es/kiriki/index.docbook
/usr/share/doc/HTML/et/kiriki/index.cache.bz2
/usr/share/doc/HTML/et/kiriki/index.docbook
/usr/share/doc/HTML/fr/kiriki/index.cache.bz2
/usr/share/doc/HTML/fr/kiriki/index.docbook
/usr/share/doc/HTML/it/kiriki/index.cache.bz2
/usr/share/doc/HTML/it/kiriki/index.docbook
/usr/share/doc/HTML/nl/kiriki/index.cache.bz2
/usr/share/doc/HTML/nl/kiriki/index.docbook
/usr/share/doc/HTML/pl/kiriki/index.cache.bz2
/usr/share/doc/HTML/pl/kiriki/index.docbook
/usr/share/doc/HTML/pt/kiriki/index.cache.bz2
/usr/share/doc/HTML/pt/kiriki/index.docbook
/usr/share/doc/HTML/pt_BR/kiriki/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kiriki/index.docbook
/usr/share/doc/HTML/sv/kiriki/index.cache.bz2
/usr/share/doc/HTML/sv/kiriki/index.docbook
/usr/share/doc/HTML/uk/kiriki/configuration.png
/usr/share/doc/HTML/uk/kiriki/gameboard.png
/usr/share/doc/HTML/uk/kiriki/index.cache.bz2
/usr/share/doc/HTML/uk/kiriki/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kiriki/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kiriki/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kiriki.lang
%defattr(-,root,root,-)

