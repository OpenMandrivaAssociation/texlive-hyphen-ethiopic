Name:		texlive-hyphen-ethiopic
Version:	73410
Release:	1
Summary:	Hyphenation patterns for Ethiopic scripts
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-ethiopic.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-ethiopic
%_texmf_language_def_d/hyphen-ethiopic
%_texmf_language_lua_d/hyphen-ethiopic

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

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
