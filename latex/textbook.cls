% Auth: Nicklas Vraa
% Docs: https://github.com/NicklasVraa/LiX
% ------------------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{textbook}[2023/02/10 For academic textbooks]

% Intercept class options.
\newcommand{\numColumns}{1}
\DeclareOption{twocolumn}{
    \renewcommand{\numColumns}{2}
    \PassOptionsToClass{\CurrentOption}{report}
}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions\relax
\LoadClass[12pt, twoside, openany]{report}

% SETUP: -----------------------------------------------------------------------
\RequirePackage{luatexja}
\RequirePackage{lltjp-listings}
\RequirePackage[basics, code, cover, figures, formatting, header, headings, isbn, license, lists, math, metadata, publish, refs, size, tables]{lix}

% OVERRIDES: -------------------------------------------------------------------
\setlength\parindent{0pt}
%\usecompacttoc % disabled for Japanese font compatibility
\geometry{letterpaper, top=28mm, bottom=28mm, left=20mm, right=20mm}
\setlength{\columnsep}{5mm}
\setlength{\droptitle}{-110mm}%
\setlength{\headsep}{5mm}%
\setcounter{secnumdepth}{4}% Levels of heading that will be numbered.
\renewcommand*{\@seccntformat}[1]{% Add dot after number.
    \csname the#1\endcsname.\hspace{0.5em}%
}
\titlespacing{\chapter}{-1pt}{-45pt}{4pt}
\titlespacing{\numberless}{0pt}{14pt}{4pt}
\titlespacing{\section}{0pt}{14pt}{4pt}
\titlespacing{\subsection}{0pt}{14pt}{4pt}
\titlespacing{\subsubsection}{0pt}{14pt}{4pt}
\titleformat*{\section}{\LARGE\bfseries}
\titleformat*{\subsection}{\Large\bfseries}
\titleformat*{\subsubsection}{\large\bfseries}
\titleformat*{\paragraph}{\bfseries}
\titleformat{\chapter}[display]{%
    \normalsize%
}{% Prefix.
    \hspace{1pt}\small\color{darkgray}\chaptertitlename \ \thechapter%
    \hfill Page \thepage\ of \pageref{LastPage}
}{% Vertical space between.
    \ifnum\numColumns=1%
        -9pt%
    \else
        -4pt%
    \fi
}{% Chapter name.
    \thispagestyle{empty}\LARGE\bfseries%
}

% HEADER AND FOOTER: -----------------------------------------------------------
\pagestyle{fancy}%
\renewcommand{\headrulewidth}{0pt}%
\renewcommand{\chaptermark}[1]{\markboth{#1}{#1}}%
\fancyhead[L]{%
    \small\color{darkgray} \chaptername\ \thechapter\ --\ \leftmark%
}
\fancyhead[R]{%
    \small\color{darkgray} Page \thepage\ of \pageref{LastPage}%
}
\fancyfoot{}%

% LAYOUT: ----------------------------------------------------------------------
\wrap{%
    \@ifundefined{theTitle}{}{%
        \@ifundefined{theSubtitle}{%
            \oldtitle{\Huge\textbf{\textsc{\theTitle}}}%
        }{%
            \oldtitle{\Huge\textbf{\textsc{\theTitle}}\\[0.4ex]%
            \large\theSubtitle}%
        }
    }
    \@ifundefined{theAuthor}{%
        \oldauthor{}%
    }{%
        \oldauthor{\normalsize{\theAuthor}}%
    }
    \@ifundefined{theDate}{%
        \olddate{}%
    }{%
        \olddate{\normalsize{\theDate}}%
    }
    \addMetadata
    \addBlanks{\theFrontBlanks}
    \addFrontCover
    \ifnum\printOnCover=1
        \@ifundefined{theTitle}{}{%
            \maketitle%
        }
    \else
        \mbox{}\newpage%
    \fi
    \addFormalPage
}{
    \addBackCover
    \addBlanks{\theBackBlanks}
}
