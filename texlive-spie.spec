# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/spie
# catalog-date 2007-04-25 15:28:03 +0200
# catalog-license lppl
# catalog-version 3.25
Name:		texlive-spie
Version:	3.25
Release:	5
Summary:	Support for formatting SPIE Proceedings manuscripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spie
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spie.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spie.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.25-2
+ Revision: 756154
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.25-1
+ Revision: 719564
- texlive-spie
- texlive-spie
- texlive-spie
- texlive-spie

