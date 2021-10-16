#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kcachegrind
Version  : 21.08.2
Release  : 32
URL      : https://download.kde.org/stable/release-service/21.08.2/src/kcachegrind-21.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.2/src/kcachegrind-21.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.2/src/kcachegrind-21.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kcachegrind-bin = %{version}-%{release}
Requires: kcachegrind-data = %{version}-%{release}
Requires: kcachegrind-license = %{version}-%{release}
Requires: kcachegrind-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kcachegrind-21.08.2
cd %{_builddir}/kcachegrind-21.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634363591
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634363591
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcachegrind
cp %{_builddir}/kcachegrind-21.08.2/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kcachegrind/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/kcachegrind-21.08.2/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kcachegrind/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/kcachegrind-21.08.2/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kcachegrind/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
cp %{_builddir}/kcachegrind-21.08.2/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kcachegrind/19d98e1b6f8ef12849ea4012a052d3907f336c91
pushd clr-build
%make_install
popd
%find_lang kcachegrind

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/metainfo/org.kde.kcachegrind.appdata.xml

%files doc
%defattr(0644,root,root,0755)
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

