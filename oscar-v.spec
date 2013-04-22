Summary:        OSCAR extension to support system-level virtualization.
Name:           oscarv
Version:        1.0
Release:        1
Vendor:         Open Cluster Group <http://OSCAR.OpenClusterGroup.org/>
Distribution:   OSCAR
Packager:       Olivier Lahaye <olivier.lahaye@cea.fr>
License:        GPL
Group:          Development/Libraries
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_localstatedir}/tmp/%{name}-root
BuildArch:      noarch
#AutoReqProv: 	no
Requires:       oscar-base-lib > 6.0.2
Requires:       packman

%description
OSCAR extension to support system-level virtualization such as Xen or KVM.

%prep
%setup

%install
%__make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog VERSION
%{_bindir}/oscar-v
%{perl_vendorlib}/OSCAR/*
%{_mandir}/man1/oscar-v.1*

%changelog
* Thu Apr 04 2013 Olivier Lahaye <olivier.lahaye@cea.fr> 1.0-1
- Initial packaging.