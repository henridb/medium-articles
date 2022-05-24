---
abstract: |
  Quantum computing (**QC** ) experts has proven may times that **QC**
  may bring great improvement in respect of computational speed. But
  most potential clients, as of today, only heard the buzz words,
  without seeing what **QC** was capable of. This is for a good reason:
  today, the actual quantum computers are barely reaching a level where
  they are relevant. This is not to say that the promises are in vain
  though, simply that Rome wasn't built in one day: neither is the
  quantum computer. This is why the business plan of ColibrITD cannot be
  to "simply" build a revolutionary platform: we need to have convincing
  arguments for clients to use quantum. For this reason, we are looking
  for good use-cases. In addition to being good demos, they can be part
  of our grand plan: building a platform for companies to use **QC**
  without needing the deep technical knowledge usually required. Such
  use-cases were previously established: a Navier-Stokes equation
  solver, an optimizer, a compiler, *etc\...* I will here present an
  idea of quantum SAT solver, using the power of superposition in order
  to find solution to systems of boolean equations.
author:
- Henri de Boutray
bibliography:
- SAT.bib
date: 2022-05-10
title: A (hybrid) quantum SAT solver
---

<!-- result from Pandoc -->

::: center
***Keywords:** SAT problem, combinatorial exploration, quantum
computing, quantum speedup*
:::

# Why: Solving problems with SAT {#sec:solving_problems_with_sat}

Problem solving is a cornerstone of our society. Improving processes
should not be a end in itself, but it is definitely a mean to improve
the lives of each of us. Amongst the problems we are confronted to
everyday (conscientiously or not), discrete problems are omnipresent.
This is why I chose to focus on those in this article. In particular, on
a specific class of those problems called SAT problems.

SAT or boolean SATisfiability problems are problems encoded as a logic
formula, and they enable the solving of many other discrete problems.
First of all, SAT is a very complex problem to solve (called a
NP-complete problem) [@Coo71], which makes it a great theoretical study
subject to analyze fundamental notions concerning quantum advantage (in
particular the likely differences between the P, NP and quantum
equivalent classes of complexity). But they are much more than that.

Most discrete optimization problems can be encoded as SAT problems,
which make the SAT solvers extremely useful tools. Here are some example
of areas where SAT solvers are used:

-   automated testing (model checking), for software but not only
    [@SBS96; @BCCZ99];

-   automated/semi-automated theorem proving and formal software
    verification [@DLL62; @Sta94; @BFMP11];

-   Electrical Design Automation (EDA):

    -   formal equivalence checking [@PK00];

    -   FPGA routing [@NSR02];

-   cryptoanalysis [@TID20];

-   various discrete optimization problems [@LAK+14].

These problems are usually huge in term of number of variables and
formula size, which implies an important need of efficient solvers.

Solving more efficiently those problems using quantum computing would
then enable us to use the quantum advantage for many discrete problems.
We could then sell our quantum SAT solver or use the SaaS approach and
sell our expertise by helping companies to efficiently solve their
discrete problems using quantum computers.

# How: Good candidates for quantum computing {#sec:good_candidates_for_quantum_computing}

SAT problems are especially interesting because of the huge size of the
problems. Indeed, **QC** is all about gaining a complexity advantage
over classical computing. Many theoretical example examples have already
been exhibited (more than 400 references split into more that 60
categories of algorithms centralized in the quantum algorithm zoo
[@Jor21]), some of them have been run on quantum processors, but the
real promise is still just that: a promise. Indeed, the the nature of
complexity comparison, the quantum advantage only gets bigger as the
size of the systems grow. This is the reason why SAT problems are such
good candidate: the real life example are typically using several
thousand of variables and exponentially more clauses. They are easy to
check but because of the number of variables, it is extremely long to
brute-force the solution.

A SAT problem is most often given as a logic formula in the Conjunctive
Normal Form (CNF). A CNF is conjunction of clauses, *i.e.* a set of
clauses that must all be true conjointly (at the same time) for the.
These clauses are themselves disjunction of literals, sets of literals
that can be disjointly true for the whole formula to be true. Finally,
each literal is either a variable or the negation of a variable.
Concretely, a CNF would look like the formula shown in
Eq.[\[eq:cnf\]](#eq:cnf){reference-type="ref" reference="eq:cnf"}.
$$\label{eq:cnf}
\bigwedge_{i=1}^n \left(\bigvee_{j=1}^m l_{i,j}\right) \text{ where } l_{i,j} \in
\{v_{i,j},\neg v_{i,j}\}$$

The SAT problems being in the NP-complete complexity class, they are
classically hard to solve. A brute-force search requires going through
$2^n$ elements, if there are $n$ variables. Since there are often around
$10^3$ variables for this king of problems, $2^{1000}$ solutions need to
be examined. With current rate of computing (exascale, $10^{18}$
operations per second [@Hin18]), this would take around $10^{275}$
years. Using a quantum search algorithm may transform these questions
from completely impossible to possible.

# What: The known the plan and the promising {#sec:the_known_the_plan_and_the_promising}

As they often are, this previous short presentation of a complex subject
was a bit reductive. Indeed, as said previously, SAT solvers are used in
day to day life, so SAT problems are solvable in less that $10^{275}$
years. Smarter than brute-force solutions exist, they are not guarantied
to finish in a reasonable time so they are most often equipped with a
timeout kill switch. These solvers are estimated to solve a problem in a
time in $O(1.329\ldots^n)$.

In comparison, if we manage to create an oracle for this problem, we
could use Grover's algorithm [@Gro96] to solve it with a complexity in
$O(\sqrt{N})=O(1.41\ldots^n)$ (the system has $n$ qubits and $N=2^n$ 
base states). And here is the first speed bump, as discussed in [@Amb05],
Grover's algorithm alone in not sufficient to leverage a quantum advantage over
the already existing algorithms that are cores to SAT solvers. This is
not the end of the line though, by combining the current classical
algorithms with Grover's, we could obtain a quadratic acceleration,
having a complexity in $O(1.153\ldots^n)$.

Other leads have also been explored: by nesting quantum search, Cerf *et
al.* managed to gain an exponential speedup [@CGW00], and by using a
very different method all together, Bian *et al.* manages to really
recently use a Quantum Annealer to explore the space of possibilities by
encoding the problem as an *Izing model* characterizing the quantum
annealer [@BCM+20].

All these options are promising. They may have an important time cost
for us, as SAT solvers are very specialized pieces of softwares, and
their intersection with other problems may be small. But because of the
remarkable possibilities they would open, being the first to have a
working quantum SAT solver may put us in a very good position.

We should also keep in mind that de Beaudrap *et al.* managed to encode
SAT problems into ZH-calculus --a variant of the diagrammatic quantum
language ZX-calculus-- and use its rewrite rules to give tools to
simplify SAT formulas [@dKM21]. This may be an interesting lead as it
means that SAT formulas may be encoded as quantum circuits, but how to
use those circuits to solve the SAT problems is left to be determined.
