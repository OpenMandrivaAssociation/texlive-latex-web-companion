# revision 15878
# category Package
# catalog-ctan /info/examples/lwc
# catalog-date 2006-06-10 21:35:51 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-latex-web-companion
Version:	20060610
Release:	2
Summary:	Examples from The LaTeX Web Companion
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/examples/lwc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-web-companion.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-web-companion.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The source of the examples printed in the book, together with
necessary supporting files.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/README.apa
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/latexexa-raw.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/latexexa.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apa/latexexa.ltx
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
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/invitationfr.sty
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/invitationfr.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/invitationfr.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/invlat1fr.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/utf8.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/utf8.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/utf8.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/apc/utf8tei.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/Makefile
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/Makefile.ex2
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/Makefile.ex3
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/README.ch3
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/colorcir.eps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex20.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex21.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex22.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex2bib.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex30.dvi
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex30.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex30/contents.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex30/ex30.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex30/ex30.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex30/index.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex30/index.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex30/internals.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex30/labels.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex30/sections.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31.ptr
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/Timg1.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/WARNINGS
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/contents.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/ex31.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/ex31.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/figure.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/images.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/images.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/img1.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/index.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/internals.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/labels.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex31/sections.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex32.ptr
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex32.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex32/contents.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex32/ex32.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex32/ex32.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex32/index.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex32/internals.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex32/labels.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex32/sections.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex32/table.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/ex3bib.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa.dvi
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/images.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/images.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/img1.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/img2.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/index.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/internals.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/l2hexa.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/l2hexa.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/labels.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/node1.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/node2.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/node3.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/node4.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/node5.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/node6.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/node7.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/l2hexa/node8.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/myinit.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS.dvi
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/WARNINGS
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/images.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/images.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img1.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img10.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img11.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img12.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img13.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img14.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img15.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img16.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img17.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img18.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img19.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img2.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img20.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img21.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img3.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img4.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img5.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img6.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img7.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img8.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/img9.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/index.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/internals.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/labels.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/node1.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/sampleAMS.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleAMS/sampleAMS.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath.dvi
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/WARNINGS
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/images.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/images.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img1.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img10.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img11.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img12.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img13.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img14.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img15.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img16.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img17.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img18.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img19.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img2.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img20.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img3.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img4.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img5.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img6.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img7.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img8.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/img9.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/index.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/internals.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/labels.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/node1.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/sampleMath.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMath/sampleMath.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages.dvi
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/WARNINGS
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/images.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/images.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img1.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img2.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img3.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img4.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img5.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img6.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img7.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img8.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img9.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/index.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/internals.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/labels.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/node1.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/sampleMathImages.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathImages/sampleMathImages.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb.dvi
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/Timg8.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/Timg9.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/WARNINGS
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/images.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/images.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img1.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img2.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img3.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img4.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img5.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img6.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img7.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img8.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img9.gif
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/index.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/internals.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/labels.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/node1.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/sampleMathThumb.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/sampleMathThumb.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/ch3bis/tac2dim.eps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/intro/lwc.eepic
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/intro/lwc.fig
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/Makefile.ex2
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/Makefile.ex3
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/README.ch3
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/colorcir.eps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/ex20.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/ex21.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/ex22.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/ex2bib.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/ex30.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/ex31.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/ex32.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/ex3bib.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/l2hexa.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/myinit.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/sampleAMS.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/sampleAMS.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/sampleMath.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/sampleMathImages.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/sampleMathThumb.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2html/tac2dim.eps
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/amaya.mml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isoamsae.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isoamsbe.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isoamsce.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isoamsne.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isoamsoe.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isoamsre.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isogrk3e.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isomfrke.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isomopfe.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isomscre.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isonume.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/isoteche.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/l2xdemo.cfg
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/l2xdemo.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/l2xdemo.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/l2xmath.cfg
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/mathml.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/mathml.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/mathmltools.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/mathmlx.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/mmaliase.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/mmlent.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/mtdemo.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/stix.mml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/techexpl.mml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/test.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/test.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/tmp.tmp
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/try.cfg
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/try2.cfg
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/try3.cfg
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/try4.cfg
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/try5.cfg
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/webeq.mml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/latex2xml/xml.dcl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xml/README.ch6
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xml/catalog
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xml/emptyexample.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xml/invitation.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xml/invitation.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xml/wrong.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xml/xml.dcl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/README.ch7
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/SGMLS.pm
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/SGMLS/Output.pm
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/SGMLS/Refs.pm
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/SGMLS/SGMLS.pm
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/catalog
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/catalog.dsssl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/catalog.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/dsssl.cat
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/dsssl.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/empty.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/empty.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/emptyexample.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/entable-alt.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/entable.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/fot.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/frisotab1exa1.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/frisotab1exa2.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/inv1html.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/inv2css.html.save
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/inv2html.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/inv2lat.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/inv3.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invcss.html.save
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invfo1.fo
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invfo1.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invfop.pdf
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invhtml.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invhtml2.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invit.css
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invitation.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invitation.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invitation.out
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invitation.sty
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invitation.tex.save
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invitation.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invitation1.tex
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invitation2.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invitation2.html
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invitation2.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invitationfr.sty
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invlat1.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invtab1.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/invtab2.dsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/isotab1to2-bis.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/isotab1to2.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/isotabexa1.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/isotabexa2.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/sectionexa.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/sectionexa.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/sgmlspl.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/skel.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/style-sheet.dtd
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/templatest.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/templatest.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/templatestnok.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/templatestok.xsl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/test-SGMLS.pl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/writefiles.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/wrong.xml
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/xml.dcl
%doc %{_texmfdistdir}/doc/latex/latex-web-companion/xmlstyle/xslexa1.xsl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
