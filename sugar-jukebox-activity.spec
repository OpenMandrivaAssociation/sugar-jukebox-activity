# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name: sugar-jukebox-activity
Version: 18
Release: %mkrel 1
Summary: Audio and video player for Sugar
License: GPLv2
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Jukebox/Jukebox-18.tar.bz2

Requires: sugar-toolkit >= 0.88.0

BuildRequires: gettext  
BuildRequires: gstreamer0.10-plugins-base  
BuildRequires: sugar-toolkit >= 0.88.0

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Audio and video player for Sugar.

%prep
%setup -q -n Jukebox-18


%build

rm -f MANIFEST
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot}/%{_prefix}
find %{buildroot} -name '*.py.orig' -print0 | xargs -0 rm -f
%find_lang org.laptop.sugar.Jukebox

%clean
rm -rf %{buildroot}

%files -f org.laptop.sugar.Jukebox.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc AUTHORS COPYING NEWS TODO

