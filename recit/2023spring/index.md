# 2023 Spring | Calc 2

<style>
 a:visited {
  color: darkorchid
 }
</style>

* Course Coordinator:
  * Dr. Lino Amorim
* Recitation Instructor:
  * Winston Cheong
  * winstonc@ksu.edu
  * Recitations: MW 11:30&ndash;12:30 and 1:30&ndash;2:30
  * Office Hours: MW 12:30&ndash;1:30 & by appointment
  * [Zoom personal meeting room](https://ksu.zoom.us/j/2293865582?pwd=Z0dqUTQrUSt6THRBOW41SG43aitmdz09)
* [Help Session schedule](https://www.math.ksu.edu/student-success/undergraduate-success/help/helpsess.html) (staffed by math grad students, in Cardwell 041)

Most material for this course is on Canvas.

## Table of Contents

- [2023 Spring | Calc 2](#2023-spring--calc-2)
  - [Table of Contents](#table-of-contents)
  - [Recitation Schedule / Notes](#recitation-schedule--notes)
  - [KSU Math Exam Archive](#ksu-math-exam-archive)
  - [Exam Solutions](#exam-solutions)
  - [Other Resources](#other-resources)
    - [Computer Aid (For *checking* answers)](#computer-aid-for-checking-answers)
  - [Math background refresher (Calc 1 \& Trig)](#math-background-refresher-calc-1--trig)
  - [Integration practice](#integration-practice)
  - [Series things](#series-things)

## Recitation Schedule / Notes

Additional problems from the OpenStax Calc 2 textbook that seem decent / relevant are listed below. A subset of them will be worked through in recitation.

* Recit 1 (Wed, Jan 18): U-substitution
  * Section 1.5: 277, 280, 282, 297
  * Section 1.6: 331, 334, 352
  * Section 1.7: 412, 414, 423, 424, 429
* Recit 2 (Mon, Jan 23): Integration by parts
  * Section 3.1: 26, 27, 29, 32, 36, 38
    * #30 will be used as ~5e~
  * Supplemental video on the DI method / layout:
  <iframe width="560" height="315" src="https://www.youtube.com/embed/8xPfNuXLSwk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
* Recit 3 (Wed, Jan 25): Trig integrals
  * [Writeup of the cases for $\int \sin^p(x) \cos^q(x) \ dx$ and $\int \tan^p(x) \sec^q(x) \ dx$](https://www.overleaf.com/read/nhsjpxjqjkpd)
  * Section 3.2: 82, 83, 89, 90, 91, 99, 100, 102
  * Recommended Exercise: Rederive the reduction formulas for $\sin^n, \cos^n, \tan^n, \sec^n$ given in class. Also, check that they still work when $n=2$ (assuming that $\sin^0 = \cos^0 = \tan^0 = \sec^0 = 1$).
    * Do give this a go, before looking at my [writeup of this exercise](https://www.overleaf.com/read/wqzshgqrpdjm)
* Recit 4 (Mon, Jan 30): Trig sub / Review for Midterm 1
  * [Trig Sub Table](https://www.overleaf.com/read/jjhvrxhqzzgg)
  * Section 3.3: 134, 138, 139, 140
    * 147 will be used as ~4d~
* Recit 5 (Wed, Feb 1): Polynomial factorization, integrals of rational functions / Partial fraction decomposition
  * Factorization formulas for difference of squares, sum and difference of cubes
  * The discriminant of a quadratic, and how it allows us to check factorizability over $\mathbb{R}$
  * Rational root theorem
  * Polynomial long division vs. synthetic division
* Recit 6 (Mon, Feb 6): Partial fraction decomposition cont
  * Section 3.4: 197, 199, 200, 205, 206, 207, 211, 212
    * 199, 206, 205, 207 will be used as ~3 A-E~
* Recit 7 (Wed, Feb 8): Numerical integration
  * [Brief notes](https://www.overleaf.com/read/sdrkwkrxchyc)
* Recit 8 (Mon, Feb 13): Improper Integrals
* Recit 9 (Wed, Feb 15): Arclength, Surface area
  * The formulas I explained in recitation were taken from [Paul's Online Notes > Surface Area](https://tutorial.math.lamar.edu/classes/calcii/surfacearea.aspx)
  * Extra: [Gabriel's Horn](https://www.wikiwand.com/en/Gabriel%27s_horn), a mathematical object with infinite surface area but finite volume. After one has learned how to compute improper integrals, and knows the formulas for surface area and volume of a solid of revolution, this assertion can be checked.
* Recit 10 (Mon, Feb 20): Work
  * Due to the snow day, this topic is now optional and will not be in the exams. I will still cover it in recitation.
  * [Lecture 10 with solutions](https://www.dropbox.com/s/f8am1t72huaesvt/lect-10-sol.pdf?dl=0)
  * [Paul's Online Notes > Work](https://tutorial.math.lamar.edu/Classes/CalcI/Work.aspx)
* Recit 11 (Wed, Feb 22): Center of mass
  * [Formulas all on one page](https://www.overleaf.com/read/wzsvhrzrgfvs)
  * [Hw 6 Problem 6 solution](https://www.dropbox.com/s/vqm7v0wfqiaw6sq/hw6.6.pdf?dl=0) (Wrote this up because the values are nasty)
* Recit 12 (Mon, Feb 27): Review for Midterm 2 (on Tues, Feb 28)
  * [Midterm 2 Review Solutions](https://www.dropbox.com/s/odsm9afh77fc1ls/review2-sol.pdf?dl=0) (Try the problems for yourself, before referring to this!)
* Recit 13 (Wed, Mar 1): Hyperbolic functions
  * [https://www.wikiwand.com/en/Inverse_hyperbolic_function#Definitions_in_terms_of_logarithms]
* Recit 14 (Mon, Mar 6): (Separable) Differential Equations
* Recit 15 (Wed, Mar 8): Sequences
* Spring break (March 12--19)
* Recit 16 (Mon, Mar 20): Series
* Recit 17 (Wed, Mar 22): Integral test
* Recit 18 (Mon, Mar 27): Comparison tests
* Recit 19 (Wed, Mar 29): Alternating Series
* Recit 20 (Mon, Apr 3): Review for midterm 3 (on April 4)
  * [Midterm 3 Review Solutions](https://www.dropbox.com/s/lsfs8vxujqbq8r8/review3-sol.pdf?dl=0)
* Recit 21 (Wed, Apr 5): Ratio and root tests
* Recit 22 (Mon, Apr 10): Power series
* Recit 23 (Wed, Apr 12): Taylor series
* Recit 24 (Mon, Apr 17): Taylor series II
* Recit 25 (Wed, Apr 19): Parametric curves
* Recit 26 (Mon, Apr 24): Parametric calculus
* Recit 27 (Wed, Apr 26): Polar coordinates
* Recit 28 (Mon, May 1): Area and length in polar coordinates
* Recit 29 (Wed, May 3): Review for final
* Recit 29 (Mon, May 8): Review for final (do we still meet?)

## KSU Math Exam Archive

<https://winstoncheong.github.io/Better-KSU-Math-Exam-Archive/calc2/>

> Particularly relevant are the 2020 Spring, 2019 Spring, and 2018 Spring semesters.

## Exam Solutions

* [Midterm 1 mysol](https://www.dropbox.com/s/ejbd30j570h6rcj/exam1-mysol.pdf?dl=0)
* [Midterm 2 mysol](https://www.dropbox.com/s/jpjlfeqtsuzzeu0/exam2-mysol.pdf?dl=0)
* [Midterm 3](https://www.dropbox.com/s/f59fpk20tpxadb3/math221_S23_mid_3_sols.pdf?dl=0)
  * [Midterm 3 comments](https://www.dropbox.com/s/dsqzgfza4if81s4/exam3-comments.pdf?dl=0)

## Other Resources

* [Paul's Online Notes > Calc 2](https://tutorial.math.lamar.edu/classes/calcii/calcii.aspx)
* [blackpenredpen > Calc 2](https://www.blackpenredpen.com/calc2)

### Computer Aid (For *checking* answers)

* [Wolfram Alpha](https://www.wolframalpha.com/)

## Math background refresher (Calc 1 & Trig)

* [blackpenredpen > Calc 2](https://www.blackpenredpen.com/calc2)
  * Under "Videos with Worksheets", work through "Watch This Before Calc 2"
  * Under "Problem Set #1", work through "So you think you can take the derivative", and "Integral Battles"
* [Paul's Online Notes > Calc 1](https://tutorial.math.lamar.edu/classes/calci/calci.aspx)
  * Has worked out practice problems
* Cheat sheets
  * [Paul's Online Notes > Cheat Sheets & Tables](https://tutorial.math.lamar.edu/Extras/CheatSheets_Tables.aspx)
    * Look at "Common Derivatives and Integrals" and "Trig Cheat Sheet". Maybe also "Complete Calculus Cheat Sheet"
  * [My Unit Circle cheatsheet](https://www.overleaf.com/read/pjpffsrkrhfx)

## Integration practice

I highly recommend the things made by [blackpenredpen](https://www.blackpenredpen.com/calc2).
Particularly useful are his:

* [Ultimate Calc 2 integral starter packet](https://www.blackpenredpen.com/_files/ugd/287ba5_434067d1e62c46c184065780349cd084.pdf) with accompanying [video solutions](https://www.youtube.com/watch?v=XOUwIdufY9Y)
* [100 integrals packet](https://www.blackpenredpen.com/_files/ugd/287ba5_9809e0bcf44548b79263bf7e0c70ad17.pdf) with accompanying [video solutions](https://www.youtube.com/watch?v=dgm4-3-Iv3s) and [video transcript](https://www.blackpenredpen.com/_files/ugd/287ba5_62e3789012b14a77ae31c0986f993ecc.pdf)
* [Integration by parts worksheet](https://www.blackpenredpen.com/_files/ugd/287ba5_472a69bac7d74d3ab272d0dd6bccd170.pdf)
* [Trig integrals worksheet](https://www.blackpenredpen.com/_files/ugd/287ba5_4c6cd42fbf9a4cc58be455f39ef6267e.pdf) ([this playlist](https://www.youtube.com/playlist?list=PLj7p5OoL6vGyKrScQeswVIq5ud2Ui5wwX) might help)
* [Trig sub worksheet](https://www.blackpenredpen.com/_files/ugd/287ba5_f6e66543dc674672a69a3ada59d0005d.pdf) ([this playlist](https://www.youtube.com/playlist?list=PLj7p5OoL6vGwi8Fdeq-4ppvGmjx47a0Eo) might help)

## Series things

* [Convergence Tests notes](https://www.overleaf.com/read/rfmfhkchbtdf)
* [BPRP Convergence Tests handout](https://www.blackpenredpen.com/_files/ugd/287ba5_7460f4c914a64263958b991439536519.pdf)
* [BPRP Power series handout](https://www.blackpenredpen.com/_files/ugd/287ba5_c2c9c480845c41498f4b0d3242e37d21.pdf)
* [BPRP's "The List"](https://www.youtube.com/watch?v=dZ5dtcJsxgI) (12 mins)
  * Quick way to intuit whether a series converges or diverges by comparing the relative growth of standard functions.  (You'll need to argue things more thoroughly on the exam.)
* [BPRP's 100 Series video](https://www.youtube.com/watch?v=jTuTEcwvkP4) (6 hrs)
* [BPRP "What Series Convergence Test Do I Use?" livestream](https://www.youtube.com/watch?v=Od2YAt1_ibE) (1.5 hours, 15 series)
* [BPRP Power series study guide](https://www.youtube.com/watch?v=LKhvdkUdLtE) (3.5 hours, 26.2 power series)