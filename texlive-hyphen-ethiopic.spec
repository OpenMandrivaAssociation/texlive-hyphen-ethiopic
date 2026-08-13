%global tl_name hyphen-ethiopic
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Hyphenation patterns for Ethiopic scripts.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-ethiopic
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-ethiopic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-ethiopic.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for languages written using the Ethiopic script for
Unicode engines. They are not supposed to be linguistically relevant in
all cases and should, for proper typography, be replaced by files
tailored to individual languages.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-ethiopic:
ethiopic loadhyph-mul-ethi.tex
=amharic
=geez
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-ethiopic:
\addlanguage{ethiopic}{loadhyph-mul-ethi.tex}{}{1}{1}
\addlanguage{amharic}{loadhyph-mul-ethi.tex}{}{1}{1}
\addlanguage{geez}{loadhyph-mul-ethi.tex}{}{1}{1}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-ethiopic:
['ethiopic'] = {
	loader = 'loadhyph-mul-ethi.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = { 'amharic', 'geez' },
	patterns = 'hyph-mul-ethi.pat.txt',
},
TL_HYPHEN_EOF
