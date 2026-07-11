%global tl_name plex
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for IBM Plex fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/plex
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the IBM Plex families of fonts. Serif, Sans and Mono families are
available in eight weights: Regular, Light, ExtraLight, Thin, Bold,
Text, Medium and SemiBold (with corresponding italics).

