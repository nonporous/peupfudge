#!/usr/bin/env python

# This script generates the xp table to be included directly in the manual tex file

# b = skill level base
# s = xp scale factor
# d = discount factor
b = 1.7
s = 10.2
d = 0.125

# a = attribute bonus
# c = current skill level
xp_cost = lambda a,c : int(round(s*pow(b,c)*(1-d*(a-3))))

clist = range(1,9)
alist = range(1,10)


colcolor = lambda color : ">{\\columncolor[HTML]{"+color+"}[\\tabcolsep][1.1\\tabcolsep]}"
blue = "\\cellcolor[HTML]{67C4D8}"
red  = "\\cellcolor[HTML]{F67D75}"
purp = "\\cellcolor[HTML]{AFA1A7}"


f = open("xptable.tex", "w")
f.write("\\setlength{\\minrowclearance}{6pt}\n")
f.write("\\begin{tabular}{crlllllllll}\n")

f.write("\\multicolumn{2}{"+colcolor("AFA1A7")+"c}{} & \\multicolumn{"+str(len(alist))+"}{"+colcolor("67C4D8")+"c}{\\textbf{Attribute Bonus}} \\\\\n")
f.write("\\noalign{\\vspace{-1pt}}\n")

f.write("\\multicolumn{2}{"+colcolor("AFA1A7")+"c}{\multirow{-2}{*}{\\textbf{XP Cost}}} &")
for a in alist:
  f.write(" \\multicolumn{1}{"+colcolor("67C4D8")+"r}{\\textbf{"+str(a)+"}} ")
  if a!=alist[-1]:
    f.write(" & ")
f.write("\\\\ \\cline{3-11}\n")

for c in clist:
  if c!=clist[-1]:
    f.write(" \\multicolumn{1}{"+colcolor("F67D75")+"r}{} & ")
  else:
    f.write("\\multicolumn{1}{"+colcolor("F67D75")+"l}{")
    f.write("\\multirow{-"+str(len(clist))+"}{*}{"+red)
    f.write("\\rotatebox[origin=c]{90}{\\textbf{Current Skill Level}}")
    f.write("}} & ")
  f.write(" \\multicolumn{1}{"+colcolor("F67D75")+"r|}{\\textbf{"+str(c)+"}} & ")
  for a in alist:
    f.write(" \\multicolumn{1}{r|}{"+str(xp_cost(a,c))+"} ")
    if a!=alist[-1]:
      f.write(" & ")
  f.write("\\\\ \\cline{3-11}\n")
  f.write("\\noalign{\\vspace{-1pt}}\n")

f.write("\\end{tabular}\n")
f.close()
