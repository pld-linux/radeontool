Summary:	Utility to control some functions of ATI Radeon chips
Summary(pl):	Narzêdzie do kontroli kilku funkcji kart ATI Radeon
Name:		radeontool
Version:	1.5
Release:	1
Source0:	http://fdd.com/software/radeon/%{name}-%{version}.tar.gz
# Source0-md5:	8065eebe5a2b163e43b40461bfe49a56
#Source1: http://fdd.com/software/radeon/lightwatch2.pl
License:	BSD
Group:		Applications/System
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to control some functions of ATI Radeon chips:
- Turning on/off external DAC
- Turning on/off lcd panel backlight
- Turn on/off LCD scaling for resolution mismatch
- Dumping registers

%description -l pl
Narzêdzie do kontrolowania kilu funkcji kart opartych o chipset ATI
Radeon:
- W³±czanie/wy³±czanie zewnêtrznego DAC
- W³±czanie/wy³±czanie pod¶wietlania panelu LCD
- W³±czanie/wy³±czanie skalowania LCD przy niepasuj±cych
  rozdzielczo¶ciach
- Zrzucanie rejestrów

%prep
%setup -q

%build
%{__cc} %{rpmcflags} -o radeontool radeontool.c

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install lightwatch.pl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%attr(755, root, root) %{_bindir}/*
