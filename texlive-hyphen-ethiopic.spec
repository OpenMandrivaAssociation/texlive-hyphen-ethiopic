# revision 23085
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-ethiopic
Version:	20120124
Release:	7
Summary:	Hyphenation patterns for Ethiopic scripts
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-ethiopic.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for languages written using the Ethiopic
script for Unicode engines. They are not supposed to be
linguistically relevant in all cases and should, for proper
typography, be replaced by files tailored to individual
languages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-ethiopic
%_texmf_language_def_d/hyphen-ethiopic
%_texmf_language_lua_d/hyphen-ethiopic

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-ethiopic <<EOF
\%% from hyphen-ethiopic:
ethiopic loadhyph-mul-ethi.tex
=amharic
=geez
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-ethiopic
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-ethiopic <<EOF
\%% from hyphen-ethiopic:
\addlanguage{ethiopic}{loadhyph-mul-ethi.tex}{}{1}{1}
\addlanguage{amharic}{loadhyph-mul-ethi.tex}{}{1}{1}
\addlanguage{geez}{loadhyph-mul-ethi.tex}{}{1}{1}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-ethiopic
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-ethiopic <<EOF
-- from hyphen-ethiopic:
	['ethiopic'] = {
		loader = 'loadhyph-mul-ethi.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = { 'amharic', 'geez' },
		patterns = 'hyph-mul-ethi.pat.txt',
		hyphenation = '',
	},
EOF


%changelog
* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120124-1
+ Revision: 767539
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 759910
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718651
- texlive-hyphen-ethiopic
- texlive-hyphen-ethiopic
- texlive-hyphen-ethiopic
- texlive-hyphen-ethiopic

