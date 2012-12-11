Summary:	Sampling-rate conversion program
Name:		resample
Version:	1.8.1
Release:	5
License:	LGPL
Group:		Sound
URL:		http://ccrma.stanford.edu/~jos/resample/
Source0:	http://ccrma.stanford.edu/~jos/resample/%{name}-%{version}.tar.gz
Patch0:		resample-1.8.1-string-fmt.patch
BuildRequires:	libtool

%description
The resample software package contains free sampling-rate conversion and filter
design utilities written in C, including a stand-alone command-line
sampling-rate conversion utility called resample. The package compiles readily
under Linux and most other UNIX operating systems. 

%prep
%setup -q
%patch0 -p1

chmod 644 AUTHORS COPYING ChangeLog NEWS README

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_mandir}/man1/*

