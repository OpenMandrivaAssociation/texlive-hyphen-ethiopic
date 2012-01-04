# revision 23085
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-ethiopic
Version:	20111103
Release:	1
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
\%\% from hyphen-ethiopic:
ethiopic loadhyph-mul-ethi.tex
=amharic
=geez
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-ethiopic <<EOF
\%\% from hyphen-ethiopic:
\addlanguage{ethiopic}{loadhyph-mul-ethi.tex}{}{1}{1}
\addlanguage{amharic}{loadhyph-mul-ethi.tex}{}{1}{1}
\addlanguage{geez}{loadhyph-mul-ethi.tex}{}{1}{1}
EOF
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
