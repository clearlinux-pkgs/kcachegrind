#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kcachegrind
Version  : 18.12.2
Release  : 3
URL      : https://download.kde.org/stable/applications/18.12.2/src/kcachegrind-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/kcachegrind-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/kcachegrind-18.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kcachegrind-bin = %{version}-%{release}
Requires: kcachegrind-data = %{version}-%{release}
Requires: kcachegrind-license = %{version}-%{release}
Requires: kcachegrind-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
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
%setup -q -n kcachegrind-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549881877
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549881877
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcachegrind
cp COPYING %{buildroot}/usr/share/package-licenses/kcachegrind/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kcachegrind/COPYING.DOC
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
/usr/share/kxmlgui5/kcachegrind/kcachegrindui.rc
/usr/share/locale/bs/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/da/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/de/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/el/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/es/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/et/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/it/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kcachegrind_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kcachegrind_qt.qm
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
/usr/share/package-licenses/kcachegrind/COPYING
/usr/share/package-licenses/kcachegrind/COPYING.DOC

%files locales -f kcachegrind.lang
%defattr(-,root,root,-)

