# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-jukebox-activity
Version: 6
Release: %mkrel 1
Summary: Audio and video player for Sugar
License: GPLv2
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Jukebox/Jukebox-6.tar.bz2

Requires: sugar-toolkit >= 0.83.4

BuildRequires: sugar-toolkit >= 0.83.4
BuildRequires: gettext  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Audio and video player for Sugar.

%prep
%setup -q -n Jukebox-6


%build
python  \
	setup.py \
	build

%install
rm -rf %{buildroot}
[ -f setup.py ] && chmod 0755 setup.py
python  \
	setup.py \
	install \
	--prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.sugar.Jukebox

%clean
rm -rf %{buildroot}

%files -f org.laptop.sugar.Jukebox.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc AUTHORS COPYING NEWS TODO

