\LoadClass[
  a1paper, 
  landscape, 
  nocolumnxxxi, 
  columnvii, 
  simple
]{graduation_project_report_common/styles/eskdx/eskdgraph}

\newif\ifGPRIllustrationOnePage
\GPRIllustrationOnePagefalse

\DeclareOption{onepage}{\GPRIllustrationOnePagetrue}
\ProcessOptions\relax

\usepackage{graduation_project_report_common/illustration/preamble}
