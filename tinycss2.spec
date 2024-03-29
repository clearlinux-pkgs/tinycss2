#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tinycss2
Version  : 1.1.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/ce/d3/ece7a98d5826bd134e269a3a3030153d30482194fca71d95a3041812aab8/tinycss2-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ce/d3/ece7a98d5826bd134e269a3a3030153d30482194fca71d95a3041812aab8/tinycss2-1.1.0.tar.gz
Summary  : tinycss2
Group    : Development/Tools
License  : BSD-3-Clause
Requires: tinycss2-license = %{version}-%{release}
Requires: tinycss2-python = %{version}-%{release}
Requires: tinycss2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
tinycss2 is a low-level CSS parser and generator written in Python: it can
parse strings, return objects representing tokens and blocks, and generate CSS
strings corresponding to these objects.

%package license
Summary: license components for the tinycss2 package.
Group: Default

%description license
license components for the tinycss2 package.


%package python
Summary: python components for the tinycss2 package.
Group: Default
Requires: tinycss2-python3 = %{version}-%{release}

%description python
python components for the tinycss2 package.


%package python3
Summary: python3 components for the tinycss2 package.
Group: Default
Requires: python3-core
Provides: pypi(tinycss2)
Requires: pypi(webencodings)

%description python3
python3 components for the tinycss2 package.


%prep
%setup -q -n tinycss2-1.1.0
cd %{_builddir}/tinycss2-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623430665
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tinycss2
cp %{_builddir}/tinycss2-1.1.0/LICENSE %{buildroot}/usr/share/package-licenses/tinycss2/26c7c8914cec0f36ce51a3d106cb8b51cdbb5fac
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tinycss2/26c7c8914cec0f36ce51a3d106cb8b51cdbb5fac

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
