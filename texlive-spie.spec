Name:		texlive-spie
Version:	15878
Release:	2
Summary:	Support for formatting SPIE Proceedings manuscripts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/spie
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spie.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A class and a BibTeX style are provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/spie/report.bib
%{_texmfdistdir}/bibtex/bst/spie/spiebib.bst
%{_texmfdistdir}/tex/latex/spie/spie.cls
%doc %{_texmfdistdir}/doc/latex/spie/README
%doc %{_texmfdistdir}/doc/latex/spie/article.pdf
%doc %{_texmfdistdir}/doc/latex/spie/article.tex
%doc %{_texmfdistdir}/doc/latex/spie/mcr3b.eps

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
