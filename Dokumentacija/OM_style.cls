% Declare that this style file requires at least LaTeX version 2e.
\NeedsTeXFormat{LaTeX2e}

% Provide the name of your page, the date it was last updated, and a comment about what it's used for

% test whether main document provides options. 
\ProvidesClass{OM_style}
%\LoadClassWithOptions{scrartcl} % ukoliko u glavnom dokumentu zelimo spec. opcije
\LoadClass[a4paper,oneside,12pt,DIV=10]{scrbook}
\usepackage{etex}
\reserveinserts{28}


% Now paste your code from the preamble here

%%% localization %%%
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[croatian]{babel}

%%% 


%%% picx, tables %%%

\usepackage{multicol}
\usepackage{titling}
%\usepackage{abstract}

\usepackage[affil-it]{authblk}
\usepackage{lastpage}


\usepackage{xcolor}
\usepackage{booktabs}

\usepackage[pdftex]{graphicx}
\usepackage{epstopdf}

\usepackage [linkcolor=blue]{hyperref}
\usepackage{listings}
\usepackage{array}
\usepackage{fancybox}
\usepackage{xtab}
\usepackage{tabulary}
\usepackage{calc}
\usepackage{hyperref}
\usepackage{memhfixc}
\usepackage{amsfonts}
\usepackage{tikz}
\usepackage{verbatim}
\usepackage{wrapfig}
%\usepackage{clrscode} 
% zbog algpseudocode
\usepackage{marginnote}
\usepackage{float}

% font style
\addtokomafont{disposition}{\rmfamily}
\usepackage{courier}


% geometry of paper
\usepackage{geometry}
\geometry{a4paper, top=2cm, left=2.5cm, right=3.0cm, bottom=1.0cm, includehead, includefoot}
\usepackage{subfigure}

%%% ams packages %%%
\usepackage[amsthm,thmmarks]{ntheorem}
\usepackage{thmtools}
%\usepackage{amsthm}
\usepackage{amssymb,amsmath}


\let\oldtitle\title
\renewcommand{\title}[1]{\oldtitle{#1}\def\titletext{#1}}

\usepackage{fancyhdr}
\usepackage{authoraftertitle}


\fancypagestyle{OM_lecture}{ %
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyhead[c]{\OMlogo{\CourseName}{\LectureType}}
\fancyfoot[c]{\thepage}
%\fancyfoot[c]{\color{white}{\thepage/\pageref{LastPage}}}

}



%%% colors

%\definecolor{lightblue}{RGB}{201,216,255}


% font types
\usepackage[sc]{mathpazo} % use mathpazo for math fonts
\usepackage{tgpagella} % but use tgpagella as main font

%\usetikzlibrary{arrows,decorations.pathmorphing,backgrounds,fit}

% math commands



% programming code
\lstloadlanguages{C++}
\lstset{language=C++,
    basicstyle={\ttfamily \scriptsize},
    backgroundcolor=\color{gray!20},                            %
    keywordstyle=\color[rgb]{0,0.5,1},                    %
    commentstyle=\color[rgb]{0.5,0.5,0.5},    %
    stringstyle=\color[rgb]{0.627,0.126,0.941},%
    showstringspaces=false,
	%numbers=left,
	tabsize = 3,
    breaklines
}




%\theoremstyle{plain} \theorembodyfont{\upshape}
\newtheorem{lema}{Lema}[chapter]
\newtheorem{teorem}{Teorem}[chapter]
\newtheorem{korolar}{Korolar}[chapter]
\newtheorem{propozicija}{Propozicija}[chapter]

\theoremstyle{remark}
\newtheorem{napomena}{Napomena}[chapter]
\newtheorem{primjedba}{Primjedba}[chapter]

\theoremstyle{definition}
\newtheorem{definicija}{Definicija}[chapter]
\newtheorem{primjer}{Primjer}
\theoremstyle{break}
\theorembodyfont{\normalfont}
\newtheorem{zadatak}{Zadatak}


\theoremstyle{nonumberbreak}
\theoremheaderfont{\scshape\bfseries}
\theorembodyfont{\normalfont}
\theoremseparator{}
\theoremsymbol{\ensuremath{\blacktriangleleft}}
\newtheorem{rjesenje}{Rješenje}
 

\newenvironment{solution}
               {
                \def\@addpunct##1{}%
                \renewcommand\proofSymbol{\ensuremath{\blacktriangleleft}}
                \begin{proof}[\scshape\textbf{Rješenje}]\mbox{}\\*}%
               {\end{proof}%
               }
%\makeatother




%%% bibliography style
\bibliographystyle{plain}



% Graffiti as in GKP's book "Concrete Mathematics"
% thanks to Lorenzo Pantieri and Enrico Gregorio
\def\graffito@setup{%
   \slshape\footnotesize%
   \parindent=0pt \lineskip=0pt \lineskiplimit=0pt %
   \tolerance=2000 \hyphenpenalty=300 \exhyphenpenalty=300%
   \doublehyphendemerits=100000%
   \finalhyphendemerits=\doublehyphendemerits}
%\DeclareRobustCommand{\graffito}[1]{\marginpar%
% [\graffito@setup\raggedleft\hspace{0pt}{#1}]%
% {\graffito@setup\raggedright\hspace{0pt}{#1}}}
\let\oldmarginpar\marginpar
\renewcommand{\marginpar}[1]{\oldmarginpar%
 [\graffito@setup\scriptsize\raggedleft\hspace{0pt}{#1}]%
 {\graffito@setup\scriptsize\raggedright\hspace{0pt}{#1}}}

 % logo

 
 
 %%% commands %%%%%
 

 
 
 \newcommand*{\OMlogo}[2]
 {
 \begin{tikzpicture}[remember picture,overlay]
  \node at (current page.north west) 
  {
  \begin{tikzpicture}[remember picture,overlay]
  %\fill[color=gray!20!white] (0,0) rectangle (0.7\paperwidth,-2);
  \draw(1.7,-1) node {\includegraphics[scale=0.12]{geo_logo_OM.pdf}}; 
  \draw[black] (3.5,-0.75) node[anchor = west] {\large \sc #1};
  \draw[black] (3.5,-1.35) node[anchor=west] {\footnotesize \href{\CourseURL}{\CourseURL}};
\end{tikzpicture}  
  };
  %\node[xshift=-0.2cm] at (current page.south) {\tikz {\draw[fill=black] (0,0) rectangle (1.8,3);}};
  \node[xshift=-3cm,yshift=-0.75cm] at (current page.north east) {\tikz {\draw[black] node {\Large \sc #2 };}};
  \node[xshift=-2.8cm,yshift=-1.35cm] at (current page.north east) {\tikz {\draw[black] node {\footnotesize \LectureDate};}};
  
  
\end{tikzpicture}
 }


% title
\makeatletter
\def\thickhrulefill{\leavevmode \leaders \hrule height 1.2ex \hfill \kern \z@}
\def\@makechapterhead#1{
\OMlogo{\CourseName}{\LectureType}
  \vspace*{10\p@}%
  {\parindent \z@ \centering \reset@font
        %\thickhrulefill\quad 
        %\scshape\bfseries\textit{\@chapapp{}  \thechapter}  
        %\quad \thickhrulefill
        \par\nobreak
        \vspace*{10\p@}%
        \interlinepenalty\@M
        \hrule
        \vspace*{10\p@}%
        \Huge \bfseries #1 \par\nobreak
        \par
        \vspace*{10\p@}%
        \hrule
        \vskip 50\p@
  }}


%%% captions

\usepackage{caption}
\DeclareCaptionFont{white}{\color{white}}
\DeclareCaptionFormat{listing}{\colorbox{gray}{\parbox{\textwidth}{#1#2#3}}}
\captionsetup[lstlisting]{format=listing,labelfont=white,textfont=white}
\captionsetup[ruled]{labelsep=period}	
	

\usepackage[ruled]{algorithm}
%\makeatletter\renewcommand{\ALG@name}{\sc Program}
%\renewcommand{\thealgorithm}{\arabic{chapter}.\arabic{algorithm}} 
\usepackage{algpseudocode}


\makeatletter\renewcommand{\ALG@name}{Algoritam}
\renewcommand{\thealgorithm}{\arabic{algorithm}} 

\algrenewcommand\alglinenumber[1]{\footnotesize #1}
% za bez : kod brojeva

\captionsetup[algorithm]{labelfont={sc,bf}}


%%% new environments %%%
\newenvironment{opis}[1]
    {\centering\vspace{-0.5ex}
    {\large\bfseries #1}\\[1ex]
	\small
    \begin{tabular}{p{0.9\textwidth}}
    %\hline\\
    }
    { 
   % \\[1ex]
    \end{tabular} 	
	\vspace{0.5ex}
	
}

