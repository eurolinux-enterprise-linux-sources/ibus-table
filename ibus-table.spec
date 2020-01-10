Name:       ibus-table
Version:    1.5.0
Release:    2%{?dist}
Summary:    The Table engine for IBus platform
License:    LGPLv2+
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://mfabian.fedorapeople.org/ibus-table/%{name}-%{version}.tar.gz
Patch1:     ibus-table-1.3.9.20110827-uppercase-umlauts.patch
Patch2:     0001-Changes-in-dconf-values-now-get-applied-immediately.patch
Patch3:     0001-Make-comments-about-_chinese_mode-clearer.patch
Patch4:     0002-Improve-detection-of-simplified-and-traditional-Chin.patch
Patch5:     0003-add-engine-chinese_variants.py-to-engine-Makefile.am.patch
Patch6:     add-engine-chinese_variants.py-to-engine-Makefile.in.patch
Patch7:     0001-Fix-typo-thanks-to-Mathieu-Bridon.patch
Patch8:     0002-Add-auto_select-functionality-to-select-the-first-ph.patch
Patch9:     0003-Update-cmode-pproperty-in-chinese-mode-only.patch
Patch10:    0004-Fall-back-to-auto_select-False-if-neither-dconf-nor-.patch
Patch11:    0005-Preedit-needs-to-be-updated-on-page-up-and-page-down.patch

Requires:       ibus > 1.3.0
BuildRequires:  ibus-devel > 1.3.0

Obsoletes:   ibus-table-additional < 1.2.0.20100111-5

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

%description
The Table engine for IBus platform.

%package -n %{name}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}, pkgconfig

%description -n %{name}-devel
Development files for %{name}.

%prep
%setup -q
%patch1 -p1 -b .uppercase-umlauts
%patch2 -p1 -b .apply-dconf-changes
%patch3 -p1 -b .make-comments-about-chinese-mode-clearer
%patch4 -p1 -b .improve-detection-of-simplified-and-traditional-chinese
%patch5 -p1 -b .fix-makefile-am
%patch6 -p1 -b .fix-makefile-in
%patch7 -p1 -b .fix-typo
%patch8 -p1 -b .add-auto-select
%patch9 -p1 -b .update-cmode-in-chinese-mode-only
%patch10 -p1 -b .fall-back-to-auto-select-false-by-default
%patch11 -p1 -b .preedit-needs-to-be-updated-when-paging

%build
%configure --disable-static --disable-additional
%__make %{?_smp_mflags}

%install
%__rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=${RPM_BUILD_ROOT} NO_INDEX=true install pkgconfigdir=%{_datadir}/pkgconfig

%find_lang %{name}

%clean
%__rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/engine
%dir %{_datadir}/%{name}/tables
%dir %{_datadir}/%{name}/icons
%dir %{_datadir}/%{name}/data
%{_datadir}/ibus/component/table.xml
%{_datadir}/%{name}/icons/%{name}.svg
%{_datadir}/%{name}/icons/full-letter.svg
%{_datadir}/%{name}/icons/full-punct.svg
%{_datadir}/%{name}/icons/half-letter.svg
%{_datadir}/%{name}/icons/half-punct.svg
%{_datadir}/%{name}/icons/onechar.svg
%{_datadir}/%{name}/icons/phrase.svg
%{_datadir}/%{name}/icons/py-mode.svg
%{_datadir}/%{name}/icons/tab-mode.svg
%{_datadir}/%{name}/icons/chinese.svg
%{_datadir}/%{name}/icons/acommit.svg
%{_datadir}/%{name}/icons/english.svg
%{_datadir}/%{name}/icons/ncommit.svg
%{_datadir}/%{name}/icons/cb-mode.svg
%{_datadir}/%{name}/icons/sc-mode.svg
%{_datadir}/%{name}/icons/scb-mode.svg
%{_datadir}/%{name}/icons/tc-mode.svg
%{_datadir}/%{name}/icons/tcb-mode.svg
%{_datadir}/%{name}/data/pinyin_table.txt.bz2
%{_datadir}/%{name}/engine/chinese_variants.py
%{_datadir}/%{name}/engine/chinese_variants.pyc
%{_datadir}/%{name}/engine/chinese_variants.pyo
%{_datadir}/%{name}/engine/factory.py
%{_datadir}/%{name}/engine/factory.pyc
%{_datadir}/%{name}/engine/factory.pyo
%{_datadir}/%{name}/engine/main.py
%{_datadir}/%{name}/engine/main.pyc
%{_datadir}/%{name}/engine/main.pyo
%{_datadir}/%{name}/engine/tabcreatedb.py
%{_datadir}/%{name}/engine/tabcreatedb.pyc
%{_datadir}/%{name}/engine/tabcreatedb.pyo
%{_datadir}/%{name}/engine/tabdict.py
%{_datadir}/%{name}/engine/tabdict.pyc
%{_datadir}/%{name}/engine/tabdict.pyo
%{_datadir}/%{name}/engine/table.py
%{_datadir}/%{name}/engine/table.pyc
%{_datadir}/%{name}/engine/table.pyo
%{_datadir}/%{name}/engine/tabsqlitedb.py
%{_datadir}/%{name}/engine/tabsqlitedb.pyc
%{_datadir}/%{name}/engine/tabsqlitedb.pyo
%{_datadir}/%{name}/tables/template.txt
%{_bindir}/%{name}-createdb
%{_libexecdir}/ibus-engine-table

%files devel
%defattr(-, root, root, -)
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Thu Feb 14 2013 Mike FABIAN <mfabian@redhat.com> - 1.5.0-2
- Resolves: #911487 - Non-Chinese tables from the ibus-table-other package do not work
- Add auto_select functionality to select the first phrase when typing.
  Useful for Cyrillic transliteration
- Update cmode property in chinese mode only
- Fall back to auto_select = False if neither dconf nor the table
  have a value for auto_select
- Preedit needs to be updated on page-up and page-down

* Mon Jan 28 2013 Mike FABIAN <mfabian@redhat.com> - 1.5.0-1
- update to latest upstream 1.5.0  from Caius ‘kaio’ Chance’s repository
- add patches for better simplified/traditional Chinese detection
- Resolves: #857967 - simplified/traditional Chinese detection in ibus-table does not work well

* Thu Jan 10 2013 Mike FABIAN <mfabian@redhat.com> - 1.4.99.20130110-1
- Resolves: #513901 ibus-table setup does not store config settings
- update to latest upstream 1.4.99.20130110 from Caius ‘kaio’ Chance’s repository, 1.5.0 branch
- When detecting the Chinese mode from the environment, also check LC_ALL
- Fix typo in self._chinese_mode variable (The typo broke the SC/TC property)
- Make cursor in lookup table always visible (became invisible after the port to GObjectIntrospection)
- apply changes in values of dconf keys immediately

* Tue Jan 08 2013 Mike FABIAN <mfabian@redhat.com> - 1.4.99.20130108-1
- update to latest upstream 1.4.99.20130108 from Caius ‘kaio’ Chance’s repository, 1.5.0 branch
- includes port to GObjectIntrospection now

* Thu Jan 03 2013 Mike FABIAN <mfabian@redhat.com> - 1.4.99.20130103-1
- update to latest upstream 1.4.99.20130103 from Caius ‘kaio’ Chance’s repository, 1.5.0 branch

* Tue Nov 13 2012 Mike FABIAN <mfabian@redhat.com> - 1.4.99.20121113-1
- update to latest upstream 1.4.99.20121113 from Caius ‘kaio’ Chance’s repository, using rel20121101 git tag
- remove ibus-table-1.4.99.20120907-improve-chinese-category-check.patch (included upstream)
- remove fix-ipa-x-sampa-table-and-phrases-containing-spaces.patch (included upstream)
- Fix marking of translatable strings for gettext
- update zh_??.po files
- Add German translation
- Do not fail if the ~/.ibus/byo-tables/ directory does not exist

* Thu Sep 13 2012 Mike FABIAN <mfabian@redhat.com> - 1.4.99.20120907-3
- Resolves: #856903
- Fix ipa-x-sampa table and phrases containing spaces in emoji-table
  Currently there is a regular expression which filters out several
  lines defining valid phrases. The emoji-table for example has phrases
  containing spaces which are currently filtered out and the ipa-x-sampa
  table has trailing comments which are filtered out as well.

* Tue Sep 11 2012 Mike FABIAN <mfabian@redhat.com> - 1.4.99.20120907-2
- Resolves: #856320
- Improve check whether a phrase is simplified or traditional Chinese
  The improvement is to ignore all non-Han characters when
  doing the check.
  This is to avoid classifying a simplified Chinese string as
  traditional just because it happens to include some non-Chinese
  characters, for example box drawing characters, which cannot be
  converted to gb2312 but happen to be convertible to big5hkscs.
  This fixes the problem in the emoji-table input method that most
  phrases cannot be input at all.

* Fri Sep 07 2012 Mike FABIAN <mfabian@redhat.com> - 1.4.99.20120907-1
- Relates: #855250
- see comment#1 in #855250
- update to latest upstream 1.4.99.20120907 from Caius 'kaio' Chance's repository
- remove ibus-table-1.3.9.20110827-add-some-keys-for-translit.patch (included upstream)
- remove ibus-table-1.3.9.20110827-enable-non-ascii.patch (included upstream)

* Wed Sep 05 2012 Mike FABIAN <mfabian@redhat.com> - 1.3.9.20110827-4
- Resolves: #845798
- add ibus-table-1.3.9.20110827-add-some-keys-for-translit.patch (from Yuwei YU, upstream)
- add ibus-table-1.3.9.20110827-enable-non-ascii.patch  (from Yuwei YU, upstream)
- add ibus-table-1.3.9.20110827-uppercase-umlauts.patch to allow uppercase as well in translit

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.20110827-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.20110827-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 31 2011 Caius 'kaio' Chance - 1.3.9.20110827-1
- Updated to upstream. 

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0.20100621-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 19 2010 Ding-Yi Chen <dchen@redhat.com> - 1.3.0.20100621-4
- Rebuild for ibus-1.4

* Wed Sep  1 2010 Jens Petersen <petersen@redhat.com> - 1.3.0.20100621-3
- remove the redundant post and postun scripts (#625330)

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.0.20100621-2
- recompiling .py files against Python 2.7 (rhbz#623320)

* Mon Jun 21 2010 Caius Chance <cchance@redhat.com> - 1.2.0.20100621-1
- Updated from upstream which tarball was rebuilt with IBus 1.3.

* Wed Mar 10 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100111-7
- Add template.txt in files.

* Wed Mar 10 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100111-6
- Disable -additional.

* Wed Mar 10 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100111-5
- Remove -additional for obsoletion by ibus-table-latin and ibus-table-code.

* Mon Feb 15 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100111-4.fc13
- Fixed latex.svg location.

* Fri Jan 29 2010 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20100111-3.fc13
- Split .pc to -devel subpackage.

* Thu Jan 14 2010 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20100111-2.fc13
- Temporary keep files of additional available in ibus-table until 
  ibus-table-{code,latin} packages are ready in repository.

* Mon Jan 11 2010 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20100111-1.fc13
- Updated source from upstream.
- Migreate tables from ibus-table-additional to ibus-table-latin and ibus-table-code.

* Wed Jan 06 2010 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090912-3.fc13
- Apply parsing equal sign patch.

* Wed Nov 11 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090912-2.fc13
- Fix crashing caused by speedmeter.

* Fri Sep 04 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090912-1.fc12
- Upgraded to upstream source.

* Fri Sep 04 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090904-1.fc12
- Updated source with additional tables separated.

* Thu Sep 03 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090902-2.fc12
- Rebuilt.

* Wed Sep 02 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090902-1.fc12
- Updated source.

* Tue Aug 04 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090804-1.fc12
- Cleaned up unused dcommit contents.

* Tue Aug 03 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090803-1.fc12
- Updated to upstream.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090625-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090625-2.fc12
- Rebuilt.

* Wed Jul 01 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090625-1.fc12
- Updated source from upstream, which released for IBus 1.2 and so on.

* Wed May 27 2009 Caius 'kaio' Chance <cchance@redhat.com> - 1.1.0.20090527-1.fc12
- Updated source from upstream, which with candidate order fix.

* Mon Mar 16 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090316-1.fc11
- Resolves: rhbz#490396
- Updated source tarball.
- Disabled speedmeter until config option is implemented.

* Fri Mar  6 2009 Jens Petersen <petersen@redhat.com> - 1.1.0.20090220-5
- make pkgconfig noarch with ibus-table-pkgconfig-noarch.patch
- fix license field: actually LGPL
- drop gettext-devel BR
- require ibus > 1.1.0

* Mon Mar 02 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090220-4.fc11
- Rebuilt.

* Mon Mar 02 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090220-3.fc11
- Rebuilt.

* Mon Mar 02 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090220-2.fc11
- Rebuilt.

* Mon Mar 02 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090220-1.fc11
- Resolves: rhbz#484650
- Updated to latest upstream release.
- Splitted chinese input methods into modules.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1.20081014-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Caius Chance <cchance@redhat.com> - 0.1.1.20081014-4
- Resolves: rhbz#466430 rhbz#466844
- Added wildcard features.
- Added preedit clearance on refocus.

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.1.20081014-3
- Rebuild for Python 2.6

* Mon Dec 1 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20081014-2
- Modified spec file to own all directories created by ibus-table.

* Fri Oct 14 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20081014-1
- Update to 0.1.1.20081014.

* Mon Sep 01 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080901-1
- Update to 0.1.1.20080901.

* Wed Aug 19 2008 Yu Yuwei <acevery@gmail.com> - 0.1.1.20080829-1
- The first version.
