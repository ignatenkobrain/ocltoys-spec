%global hash 39c5bb1b3c2a244397ee2339881848db0a8ce54b   
%global hash_short %(c=%{hash}; echo ${c:0:12})

Name:           ocltoys
Version:        1.0
Release:        2.%{hash_short}%{?dist}
Summary:        Collection of OpenCL examples focused on Computer Graphics

License:        GPLv3
URL:            http://code.google.com/p/ocltoys/
Source0:        http://ocltoys.googlecode.com/archive/%{hash}.zip
Patch0:         0001-build-migrate-to-GNU-autotools.patch
Patch1:         0002-configure-add-sse-and-sse2-to-cppflags.patch

BuildRequires:  automake libtool
BuildRequires:  boost-devel opencl-headers freeglut-devel ocl-icd-devel
Requires:       pocl

%description
Collection of OpenCL examples focused on Computer Graphics

%prep
%setup -q -n %{name}-%{hash_short}
%patch0 -p1 -b .autotools
%patch1 -p1 -b .sse
chmod +x ./autogen.sh

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS COPYING
%{_bindir}/jugCLer
%{_bindir}/juliagpu
%{_bindir}/mandelgpu
%{_bindir}/smallptgpu
%{_datadir}/%{name}/

%changelog
* Mon Jan 20 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-2.39c5bb1b3c2a
- Add patch for fix sse, sse2 CPPFLAGS

* Sun Jan 19 2014 Vitaly Sulimov <blackphoenix10@yandex.ru> - 1.0-1.39c5bb1b3c2a
- Initial import
