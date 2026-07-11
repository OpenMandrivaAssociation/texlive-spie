%global tl_name spie
%global tl_revision 75447

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.25
Release:	%{tl_revision}.1
Summary:	Support for formatting SPIE Proceedings manuscripts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/spie
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spie.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A class and a BibTeX style are provided.

