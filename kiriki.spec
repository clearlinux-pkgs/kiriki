#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v12
# autospec commit: fbcebd0
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kiriki
Version  : 24.05.1
Release  : 30
URL      : https://download.kde.org/stable/release-service/24.05.1/src/kiriki-24.05.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.1/src/kiriki-24.05.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.1/src/kiriki-24.05.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: kiriki-bin = %{version}-%{release}
Requires: kiriki-data = %{version}-%{release}
Requires: kiriki-license = %{version}-%{release}
Requires: kiriki-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kiriki-24.05.1
cd %{_builddir}/kiriki-24.05.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718597167
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718597167
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kiriki
cp %{_builddir}/kiriki-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kiriki/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kiriki-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kiriki/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/kiriki-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/kiriki/bd75d59f9d7d9731bfabdc48ecd19e704d218e38 || :
export GOAMD64=v2
GOAMD64=v2
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
/usr/share/metainfo/org.kde.kiriki.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kiriki/configuration.png
/usr/share/doc/HTML/ca/kiriki/gameboard.png
/usr/share/doc/HTML/ca/kiriki/index.cache.bz2
/usr/share/doc/HTML/ca/kiriki/index.docbook
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
/usr/share/package-licenses/kiriki/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kiriki/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kiriki/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kiriki.lang
%defattr(-,root,root,-)

