%define DATE	20040130
%define    language  Finnish
%define    lang      fi
%define format1      html-%{lang}
%define format2      HTML/%{lang}

Summary:   %language HOWTO documents (html format) from the Linux Documentation Project
Name:      howto-%{format1}
Version:	10.0
Release:	%mkrel 8
Group:		Books/Howtos

Source0:   %name.tar

Url:		http://www.linuxdoc.org/docs.html#howto
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

BuildRequires: howto-utils
Requires:    locales-%lang, xdg-utils

%description
Linux HOWTOs are detailed documents which describe a specific aspect of 
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

%prep
%setup -q -n %name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
untar_howtos; makehowtoindex %lang %language > index.html; cp -a * $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}

install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/applications
cat > %{buildroot}%_datadir/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Howto %language
Comment=HOWTO documents (html format) from the Linux Documentation Project in %language
Exec=xdg-open %_datadir/doc/HOWTO/HTML/%lang/index.html
Icon=documentation_section
Terminal=false
Type=Application
Categories=Documentation;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/HOWTO/%{format2}
%{_datadir}/applications/*.desktop

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 10.0-7mdv2011.0
+ Revision: 665421
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 10.0-6mdv2011.0
+ Revision: 605864
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 10.0-5mdv2010.1
+ Revision: 520699
- rebuilt for 2010.1

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 10.0-4mdv2009.0
+ Revision: 218432
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 10.0-4mdv2008.1
+ Revision: 150262
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 08 2007 Funda Wang <fwang@mandriva.org> 10.0-3mdv2008.0
+ Revision: 82157
- Rebuild for new era
- Import howto-html-fi



* Thu Jul 07 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 10.0-2mdk
- fix menu entry (#16626)

* Fri Jan 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 10.0-1mdk
- from Thomas Backlund <tmb@mandrake.org>:
  * updated Sal-Faq to 0.2.1
  * updated Finnish-Howto to 2.0.21

* Mon Mar 03 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-1mdk
from Thomas Backlund <tmb@iki.fi>:
- first mdk build
- specs and look based on howto-html 9.1-0.6mdk
