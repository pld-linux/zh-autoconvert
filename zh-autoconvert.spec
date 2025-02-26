Summary:	Chinese HZ/GB/BIG5/UTF-16/UTF-7/UTF-8 encodings auto-converter
Summary(pl.UTF-8):	Automatyczny konwerter kodowań chińskich znaków HZ/GB/BIG5/UTF-16/UTF-7/UTF-8
Name:		zh-autoconvert
Version:	0.3.16
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.debian.org/debian/pool/main/z/zh-autoconvert/%{name}_%{version}.orig.tar.gz
# Source0-md5:	1f4aa2332afc076910b5d510b8c81966
Patch0:		%{name}-dirs.patch
Patch1:		%{name}-xchat-gtk2.patch
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoConvert is an intelligent Chinese Encoding converter. It uses
builtin functions to judge the type of the input file's Chinese
Encoding (such as GB/Big5/HZ), then converts the input file to any
type of Chinese Encoding you want. You can use autoconvert to handle
incoming mail, automatically converting messages to the Chinese
Encoding you want. It can alse handle Unicode (UTF-16)/UTF-7/UTF-8
now.

%description -l pl.UTF-8
AutoConvert to inteligentny konwerter kodowania znaków chińskich.
Używa wbudowanych funkcji do rozpoznawania w pliku wejściowym typu
kodowania znaków chińskich (takiego jak GB/Big5/HZ), a następnie
konwertuje plik do dowolnie wybranego kodowania. Pakietu można używać
do obsługi poczty przychodzącej, aby automatycznie konwertować
wiadomości. Potrafi też obsługiwać kodowania unikodowe
(UTF-16/UTF-7/UTF-8).

%package devel
Summary:	Header files for libhz library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libhz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libhz library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libhz.

%package static
Summary:	Static libhz library
Summary(pl.UTF-8):	Statyczna biblioteka libhz
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libhz library.

%description static -l pl.UTF-8
Statyczna biblioteka libhz.

%package -n xchat-zh-autoconvert
Summary:	zh-autoconvert plugins for XChat IRC client
Summary(pl.UTF-8):	Wtyczki zh-autoconvert dla klienta IRC-a XChat
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	xchat >= 2

%description -n xchat-zh-autoconvert
zh-autoconvert plugins for XChat IRC client.

%description -n xchat-zh-autoconvert -l pl.UTF-8
Wtyczki zh-autoconvert dla klienta IRC-a XChat.

%prep
%setup -q -n autoconvert-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} -j1 \
	CC="%{__cc}" \
	CFLAG="%{rpmcflags} -Wall -Iinclude" \
	CFLAGS="%{rpmcflags} -Wall -I../include" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/xchat/plugins,%{_includedir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE Readme TODO Thanks
%attr(755,root,root) %{_bindir}/autob5
%attr(755,root,root) %{_bindir}/autogb
%attr(755,root,root) %{_libdir}/libhz.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libhz.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhz.so
%{_includedir}/hz.h
%{_includedir}/zhstatis.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libhz.a

%files -n xchat-zh-autoconvert
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xchat/plugins/xchat-autob5.so
%attr(755,root,root) %{_libdir}/xchat/plugins/xchat-autogb.so
