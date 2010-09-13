%define		plugin		phpwikify
Summary:	DokuWiki plugin to render PHP output as Wiki text
Summary(pl.UTF-8):	Wtyczka phpwikify dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20050722
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://glen.alkohol.ee/pld/dokuwiki-plugin-phpwikify.php.txt
# Source0-md5:	9b4011292cfb04a69226a2290ae7e207
URL:		http://www.dokuwiki.org/plugin:phpwikify
BuildRequires:	rpmbuild(macros) >= 1.520
# for %%undos macro
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	dokuwiki >= 20091225
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin enables you to use PHP scripts in the wiki pages in the
same way as by using the <php> tag. The difference is that the PHP
script output is feed through the DokuWiki parser/renderer and you
could create for example bulleted lists using " *...".

Security warning! This plugin is not recommended for a public wiki
Security wise it is the same as having the Configuration Setting:
phpok enabled. Even if the script output is parsed, any other actions
taken by the script is NOT checked.

%prep
%setup -qcT
cp -a %{SOURCE0} syntax.php

version=$(awk -F"'" '/date/{print $4}' syntax.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
