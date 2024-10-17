Name:		texlive-plex
Version:	69154
Release:	1
Summary:	Support for IBM Plex fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/plex
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the IBM Plex families of fonts. Serif, Sans and
Mono families are available in eight weights: Regular, Light,
ExtraLight, Thin, Bold, Text, Medium and SemiBold (with
corresponding italics).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/plex
%{_texmfdistdir}/fonts/vf/ibm/plex
%{_texmfdistdir}/fonts/type1/ibm/plex
%{_texmfdistdir}/fonts/tfm/ibm/plex
%{_texmfdistdir}/fonts/opentype/ibm/plex
%{_texmfdistdir}/fonts/map/dvips/plex
%{_texmfdistdir}/fonts/enc/dvips/plex
%doc %{_texmfdistdir}/doc/fonts/plex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
