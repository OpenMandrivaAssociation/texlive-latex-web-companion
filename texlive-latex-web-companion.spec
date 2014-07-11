# revision 29349
# category Package
# catalog-ctan /info/examples/lwc
# catalog-date 2012-07-10 08:38:43 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-latex-web-companion
Version:	20120710
Release:	8
Summary:	Examples from The LaTeX Web Companion
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/examples/lwc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-web-companion.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-web-companion.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%define __noautoprov 'perl\\(.*'

%description
The source of the examples printed in the book, together with
necessary supporting files.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/README.apa
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/latexexa-raw.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/latexexa.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/latexexa.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/latexexa.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/phys332-1.eps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/phys332-2.eps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/teched.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/teched.java
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/InvitationSAX.class
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/InvitationSAX.java
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/MySAXApp.class
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/MySAXApp.java
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/README.apb
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/bibliotest1.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/bibliotest2.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/biblioxml1.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/biblioxml2.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/colorcir.eps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/inv2.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/invitation.sty
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/invitation2.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/invitation2.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/latexmath.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/latexmml.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/makelatex.sh
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/minilatex.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/minilatex.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/minilatexexa.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/minilatexexa.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/mybiblio.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apb/utf82latin1.sh
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/ISOcyr1.pen
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/README.apc
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/invitation.sty
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/invitationfr.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/invitationfr.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/invitationfr.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/invitationfrraw.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/invlat1fr.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/utf8.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/utf8.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/utf8.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/utf8raw.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch2/latexexa.aux
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch2/latexexa.brf
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch2/latexexa.log
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch2/latexexa.out
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch2/latexexa.pdf
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch2/latexexa.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch2/phys332-1.pdf
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch2/phys332-2.pdf
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/Makefile.ex2
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/Makefile.ex3
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/README.ch3
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/colorcir.eps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/ex20.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/ex21.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/ex22.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/ex2bib.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/ex30.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/ex31.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/ex32.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/ex3bib.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/l2hexa.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/myinit.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/sampleAMS.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/sampleAMS.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/sampleMath.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/sampleMathImages.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/sampleMathThumb.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3/tac2dim.eps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/latexexa.aux
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/latexexa.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/latexexa.dvi
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/latexexa.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/latexexa.idv
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/latexexa.lg
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/latexexa.log
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/latexexa.otc
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/latexexa.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/latexexa.toc
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/latexexa.xref
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/phys332-1.eps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/phys332-2.eps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/tex4ht.env
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/tex4ht.tmp
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch4/tmp.ps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch6/README.ch6
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch6/catalog
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch6/emptyexample.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch6/invitation.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch6/invitation.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch6/wrong.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch6/xml.dcl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/README.ch7
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/SGMLS.pm
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/SGMLS/Output.pm
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/SGMLS/Refs.pm
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/SGMLS/SGMLS.pm
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/any.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/any.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/catalog
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/catalog.dsssl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/catalog.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/debug.txt
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/dsssl.cat
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/dsssl.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/empty.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/empty.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/emptyexample.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/fot.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/inv1html.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/inv2css.html.save
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/inv2html.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/inv2lat.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/inv3.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invcss.html.save
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invfo1.fop
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invfo1.out
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invfo1.pdf
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invfo1.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invhtml.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invhtml2.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invit.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invitation.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invitation.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invitation.fot
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invitation.sty
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invitation.tex.save
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invitation.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invitation2.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invitation2.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invitationfr.sty
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invlat1.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invtab1.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/invtab2.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/makesum.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/makesum.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/sectionexa.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/sectionexa.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/sgmlspl.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/skel.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/style-sheet.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/templatest.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/templatest.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/templatestnok.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/templatestok.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/test-SGMLS.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/writefile.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/writefiles.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/wrong.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/xml.dcl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/xsl.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch7/xslexa1.xsl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
