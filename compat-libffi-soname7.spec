#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v4
# autospec commit: da8b975
#
Name     : compat-libffi-soname7
Version  : 3.3
Release  : 39
URL      : https://github.com/libffi/libffi/archive/v3.3/libffi-3.3.tar.gz
Source0  : https://github.com/libffi/libffi/archive/v3.3/libffi-3.3.tar.gz
Summary  : Library supporting Foreign Function Interfaces
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: compat-libffi-soname7-lib = %{version}-%{release}
Requires: compat-libffi-soname7-license = %{version}-%{release}
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : tcl
BuildRequires : texinfo
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Update-ax_cc_maxopt-m4-macro.patch

%description
Status
======
[![Build Status](https://travis-ci.org/libffi/libffi.svg?branch=master)](https://travis-ci.org/libffi/libffi)
[![Build status](https://ci.appveyor.com/api/projects/status/8lko9vagbx4w2kxq?svg=true)](https://ci.appveyor.com/project/atgreen/libffi)

%package lib
Summary: lib components for the compat-libffi-soname7 package.
Group: Libraries
Requires: compat-libffi-soname7-license = %{version}-%{release}

%description lib
lib components for the compat-libffi-soname7 package.


%package lib32
Summary: lib32 components for the compat-libffi-soname7 package.
Group: Default
Requires: compat-libffi-soname7-license = %{version}-%{release}

%description lib32
lib32 components for the compat-libffi-soname7 package.


%package license
Summary: license components for the compat-libffi-soname7 package.
Group: Default

%description license
license components for the compat-libffi-soname7 package.


%prep
%setup -q -n libffi-3.3
cd %{_builddir}/libffi-3.3
%patch -P 1 -p1
pushd ..
cp -a libffi-3.3 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708473737
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%autogen --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1708473737
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-libffi-soname7
cp %{_builddir}/libffi-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/compat-libffi-soname7/6ead3a7aa9b1daab14e473e5b0a18383eeb9faee || :
cp %{_builddir}/libffi-%{version}/LICENSE-BUILDTOOLS %{buildroot}/usr/share/package-licenses/compat-libffi-soname7/edba73156489a814c9ec38f23fa6aea64efebcbf || :
export GOAMD64=v2
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/include/ffi.h
rm -f %{buildroot}*/usr/include/ffitarget.h
rm -f %{buildroot}*/usr/lib32/libffi.so
rm -f %{buildroot}*/usr/lib32/pkgconfig/32libffi.pc
rm -f %{buildroot}*/usr/lib32/pkgconfig/libffi.pc
rm -f %{buildroot}*/usr/lib64/libffi.so
rm -f %{buildroot}*/usr/lib64/pkgconfig/libffi.pc
rm -f %{buildroot}*/usr/share/info/libffi.info
rm -f %{buildroot}*/usr/share/man/man3/ffi.3
rm -f %{buildroot}*/usr/share/man/man3/ffi_call.3
rm -f %{buildroot}*/usr/share/man/man3/ffi_prep_cif.3
rm -f %{buildroot}*/usr/share/man/man3/ffi_prep_cif_var.3

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libffi.so.7
/usr/lib64/libffi.so.7.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libffi.so.7
/usr/lib32/libffi.so.7.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-libffi-soname7/6ead3a7aa9b1daab14e473e5b0a18383eeb9faee
/usr/share/package-licenses/compat-libffi-soname7/edba73156489a814c9ec38f23fa6aea64efebcbf
