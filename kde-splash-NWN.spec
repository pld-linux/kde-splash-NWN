
%define		_splash		NWN

Summary:	KDE splash screen - NWN theme
Summary(pl):	Ekran startowy KDE - motyw NWN
Name:		kde-splash-%{_splash}
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=1706
Source0:	http://www.kde-look.org/content/files/13285-nwn_splash.tar.gz
# Source0-md5:	73a0298260c579960234a53c97df5a8c
Source1:	%{name}-Preview.png
Source2:	%{name}-Theme.rc
URL:		http://www.kdelook.org/content/download.php?content=13285
Requires:	kdebase-desktop
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE splash screen with NeverWinter Nights logo and icons.

%description -l pl
Ekran startowy KDE z logo i ikonami z gry NeverWinter Nights.

%prep
%setup -q -n %{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

cp * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

install %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Preview.png

install %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Theme.rc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}