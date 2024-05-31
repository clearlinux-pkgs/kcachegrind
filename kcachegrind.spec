#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kcachegrind
Version  : 24.05.0
Release  : 68
URL      : https://download.kde.org/stable/release-service/24.05.0/src/kcachegrind-24.05.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.0/src/kcachegrind-24.05.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.0/src/kcachegrind-24.05.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kcachegrind-bin = %{version}-%{release}
Requires: kcachegrind-data = %{version}-%{release}
Requires: kcachegrind-license = %{version}-%{release}
Requires: kcachegrind-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KCachegrind / QCachegrind
-========================
{K,Q}Cachegrind is a KDE/Qt GUI to visualize profiling data.
It's mainly used as visualization frontend for data measured
by Cachegrind/Callgrind tools from the Valgrind package, but
there are converters for other measurement tools available.

%package bin
Summary: bin components for the kcachegrind package.
Group: Binaries
Requires: kcachegrind-data = %{version}-%{release}
Requires: kcachegrind-license = %{version}-%{release}

%description bin
bin components for the kcachegrind package.


%package data
Summary: data components for the kcachegrind package.
Group: Data

%description data
data components for the kcachegrind package.


%package doc
Summary: doc components for the kcachegrind package.
Group: Documentation

%description doc
doc components for the kcachegrind package.


%package license
Summary: license components for the kcachegrind package.
Group: Default

%description license
license components for the kcachegrind package.


%package locales
Summary: locales components for the kcachegrind package.
Group: Default

%description locales
locales components for the kcachegrind package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kcachegrind-24.05.0
cd %{_builddir}/kcachegrind-24.05.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716570763
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
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
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
export SOURCE_DATE_EPOCH=1716570763
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcachegrind
cp %{_builddir}/kcachegrind-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kcachegrind/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kcachegrind-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kcachegrind/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kcachegrind-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kcachegrind/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/kcachegrind-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kcachegrind/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcachegrind
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kcachegrind
/usr/bin/dprof2calltree
/usr/bin/hotshot2calltree
/usr/bin/kcachegrind
/usr/bin/memprof2calltree
/usr/bin/op2calltree
/usr/bin/pprof2calltree

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kcachegrind.desktop
/usr/share/icons/hicolor/128x128/apps/kcachegrind.png
/usr/share/icons/hicolor/32x32/apps/kcachegrind.png
/usr/share/icons/hicolor/48x48/apps/kcachegrind.png
/usr/share/icons/hicolor/64x64/apps/kcachegrind.png
/usr/share/kcachegrind/icons/hicolor/16x16/actions/move.png
/usr/share/kcachegrind/icons/hicolor/16x16/actions/percent.png
/usr/share/kcachegrind/icons/hicolor/22x22/actions/hidetemplates.png
/usr/share/kcachegrind/icons/hicolor/22x22/actions/move.png
/usr/share/kcachegrind/icons/hicolor/22x22/actions/percent.png
/usr/share/kcachegrind/icons/hicolor/32x32/actions/percent.png
/usr/share/kcachegrind/tips
/usr/share/locale/ast/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/da/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/de/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/el/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/en/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/es/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/et/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/it/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/se/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/metainfo/org.kde.kcachegrind.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/ca/kcachegrind/index.docbook
/usr/share/doc/HTML/de/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/de/kcachegrind/index.docbook
/usr/share/doc/HTML/en/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/en/kcachegrind/index.docbook
/usr/share/doc/HTML/es/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/es/kcachegrind/index.docbook
/usr/share/doc/HTML/et/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/et/kcachegrind/index.docbook
/usr/share/doc/HTML/fr/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/fr/kcachegrind/index.docbook
/usr/share/doc/HTML/gl/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/gl/kcachegrind/index.docbook
/usr/share/doc/HTML/it/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/it/kcachegrind/index.docbook
/usr/share/doc/HTML/nl/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/nl/kcachegrind/index.docbook
/usr/share/doc/HTML/pt/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/pt/kcachegrind/index.docbook
/usr/share/doc/HTML/pt_BR/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcachegrind/index.docbook
/usr/share/doc/HTML/ru/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/ru/kcachegrind/index.docbook
/usr/share/doc/HTML/sv/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/sv/kcachegrind/index.docbook
/usr/share/doc/HTML/uk/kcachegrind/index.cache.bz2
/usr/share/doc/HTML/uk/kcachegrind/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcachegrind/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/kcachegrind/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kcachegrind/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kcachegrind/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567

%files locales -f kcachegrind.lang
%defattr(-,root,root,-)

