%global tl_name latex-web-companion
%global tl_revision 29349

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Examples from The LaTeX Web Companion
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/examples/lwc
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-web-companion.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-web-companion.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The source of the examples printed in the book, together with necessary
supporting files.

