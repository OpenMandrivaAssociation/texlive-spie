# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/spie
# catalog-date 2007-04-25 15:28:03 +0200
# catalog-license lppl
# catalog-version 3.25
Name:		texlive-spie
Version:	3.25
Release:	1
Summary:	Support for formatting SPIE Proceedings manuscripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spie
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spie.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spie.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A class and a BibTeX style are provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
