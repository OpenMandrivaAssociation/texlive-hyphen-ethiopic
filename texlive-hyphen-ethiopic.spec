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
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for languages written using the Ethiopic script for
Unicode engines. They are not supposed to be linguistically relevant in
all cases and should, for proper typography, be replaced by files
tailored to individual languages.

