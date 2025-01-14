import m5
from m5.objects import *
import os

## Paths
SPEC_PATH       = os.environ['SPEC_PATH']
RUN_DIR_prefix  = '/benchspec/CPU2006/'
RUN_DIR_postfix = '/run/run_base_ref_amd64-m64-gcc41-nn.0000'
x86_suffix = '_base.amd64-m64-gcc41-nn'

#temp
#binary_dir = spec_dir
#data_dir = spec_dir
pacManTest = Process()
pacManTest.executable = 'pointerUse' + x86_suffix
pacManTest.cmd = [pacManTest.executable]
pacManTest.cwd = SPEC_PATH + RUN_DIR_prefix + 'pointerUse' + RUN_DIR_postfix 

#400.perlbench
perlbench = Process() # Update June 7, 2017: This used to be LiveProcess()
perlbench.executable =  'perlbench' + x86_suffix
# TEST CMDS
#perlbench.cmd = [perlbench.executable] + ['-I.', '-I./lib', 'attrs.pl']
# REF CMDS
perlbench.cmd = [perlbench.executable] + ['-I./lib', 'checkspam.pl', '2500', '5', '25', '11', '150', '1', '1', '1', '1']
#perlbench.cmd = [perlbench.executable] + ['-I./lib', 'diffmail.pl', '4', '800', '10', '17', '19', '300']
#perlbench.cmd = [perlbench.executable] + ['-I./lib', 'splitmail.pl', '1600', '12', '26', '16', '4500']
#perlbench.output = out_dir+'perlbench.out'
perlbench.cwd = SPEC_PATH + RUN_DIR_prefix + '400.perlbench' + RUN_DIR_postfix 

#401.bzip2
bzip2 = Process() # Update June 7, 2017: This used to be LiveProcess()
bzip2.executable =  'bzip2' + x86_suffix
# TEST CMDS
#bzip2.cmd = [bzip2.executable] + ['input.program', '5']
# REF CMDS
bzip2.cmd = [bzip2.executable] + ['input.source', '280']
#bzip2.cmd = [bzip2.executable] + ['chicken.jpg', '30']
#bzip2.cmd = [bzip2.executable] + ['liberty.jpg', '30']
#bzip2.cmd = [bzip2.executable] + ['input.program', '280']
#bzip2.cmd = [bzip2.executable] + ['text.html', '280']
#bzip2.cmd = [bzip2.executable] + ['input.combined', '200']
#bzip2.output = out_dir + 'bzip2.out'
bzip2.cwd = SPEC_PATH + RUN_DIR_prefix + "401.bzip2" + RUN_DIR_postfix

#403.gcc
gcc = Process() # Update June 7, 2017: This used to be LiveProcess()
gcc.executable = 'gcc' + x86_suffix
# TEST CMDS
#gcc.cmd = [gcc.executable] + ['cccp.i', '-o', 'cccp.s']
# REF CMDS
gcc.cmd = [gcc.executable] + ['166.i', '-o', '166.s']
#gcc.cmd = [gcc.executable] + ['200.i', '-o', '200.s']
#gcc.cmd = [gcc.executable] + ['c-typeck.i', '-o', 'c-typeck.s']
#gcc.cmd = [gcc.executable] + ['cp-decl.i', '-o', 'cp-decl.s']
#gcc.cmd = [gcc.executable] + ['expr.i', '-o', 'expr.s']
#gcc.cmd = [gcc.executable] + ['expr2.i', '-o', 'expr2.s']
#gcc.cmd = [gcc.executable] + ['g23.i', '-o', 'g23.s']
#gcc.cmd = [gcc.executable] + ['s04.i', '-o', 's04.s']
#gcc.cmd = [gcc.executable] + ['scilab.i', '-o', 'scilab.s']
#gcc.output = out_dir + 'gcc.out'
gcc.cwd = SPEC_PATH + RUN_DIR_prefix + "403.gcc" + RUN_DIR_postfix

#410.bwaves
bwaves = Process() # Update June 7, 2017: This used to be LiveProcess()
bwaves.executable = 'bwaves' + x86_suffix
# TEST CMDS
#bwaves.cmd = [bwaves.executable]
# REF CMDS
bwaves.cmd = [bwaves.executable]
#bwaves.output = out_dir + 'bwaves.out'
bwaves.cwd = SPEC_PATH + RUN_DIR_prefix + "410.bwaves" + RUN_DIR_postfix

#416.gamess
gamess = Process() # Update June 7, 2017: This used to be LiveProcess()
gamess.executable = 'gamess' + x86_suffix
# TEST CMDS
#gamess.cmd = [gamess.executable]
#gamess.input = 'exam29.config'
# REF CMDS
gamess.cmd = [gamess.executable]
gamess.input = 'cytosine.2.config'
#gamess.cmd = [gamess.executable]
#gamess.input = 'h2ocu2+.gradient.config'
#gamess.cmd = [gamess.executable]
#gamess.input = 'triazolium.config'
#gamess.output = out_dir + 'gamess.out'
gamess.cwd = SPEC_PATH + RUN_DIR_prefix + "416.gamess" + RUN_DIR_postfix

#429.mcf
mcf = Process() # Update June 7, 2017: This used to be LiveProcess()
mcf.executable =  'mcf' + x86_suffix
# TEST CMDS
#mcf.cmd = [mcf.executable] + ['inp.in']
# REF CMDS
mcf.cmd = [mcf.executable] + ['inp.in']
#mcf.output = out_dir + 'mcf.out'
mcf.cwd = SPEC_PATH + RUN_DIR_prefix + "429.mcf" + RUN_DIR_postfix

#433.milc
milc = Process() # Update June 7, 2017: This used to be LiveProcess()
milc.executable = 'milc' + x86_suffix
# TEST CMDS
#milc.cmd = [milc.executable]
#milc.input = 'su3imp.in'
# REF CMDS
milc.cmd = [milc.executable]
milc.input = 'su3imp.in'
#milc.output = out_dir + 'milc.out'
milc.cwd = SPEC_PATH + RUN_DIR_prefix + "433.milc" + RUN_DIR_postfix

#434.zeusmp
zeusmp = Process() # Update June 7, 2017: This used to be LiveProcess()
zeusmp.executable = 'zeusmp' + x86_suffix
# TEST CMDS
#zeusmp.cmd = [zeusmp.executable]
# REF CMDS
zeusmp.cmd = [zeusmp.executable]
#zeusmp.output = out_dir + 'zeusmp.out'
zeusmp.cwd = SPEC_PATH + RUN_DIR_prefix + "434.zeusmp" + RUN_DIR_postfix

#435.gromacs
gromacs = Process() # Update June 7, 2017: This used to be LiveProcess()
gromacs.executable = 'gromacs' + x86_suffix
# TEST CMDS
#gromacs.cmd = [gromacs.executable] + ['-silent','-deffnm', 'gromacs', '-nice','0']
# REF CMDS
gromacs.cmd = [gromacs.executable] + ['-silent','-deffnm', 'gromacs', '-nice','0']
#gromacs.output = out_dir + 'gromacs.out'
gromacs.cwd = SPEC_PATH + RUN_DIR_prefix + '435.gromacs' + RUN_DIR_postfix 

#436.cactusADM
cactusADM = Process() # Update June 7, 2017: This used to be LiveProcess()
cactusADM.executable = 'cactusADM' + x86_suffix
# TEST CMDS
#cactusADM.cmd = [cactusADM.executable] + ['benchADM.par']
# REF CMDS
cactusADM.cmd = [cactusADM.executable] + ['benchADM.par']
#cactusADM.output = out_dir + 'cactusADM.out'
cactusADM.cwd = SPEC_PATH + RUN_DIR_prefix + "436.cactusADM" + RUN_DIR_postfix

#437.leslie3d
leslie3d = Process() # Update June 7, 2017: This used to be LiveProcess()
leslie3d.executable = 'leslie3d' + x86_suffix
# TEST CMDS
#leslie3d.cmd = [leslie3d.executable]
#leslie3d.input = 'leslie3d.in'
# REF CMDS
leslie3d.cmd = [leslie3d.executable]
leslie3d.input = 'leslie3d.in'
#leslie3d.output = out_dir + 'leslie3d.out'
leslie3d.cwd = SPEC_PATH + RUN_DIR_prefix + "437.leslie3d" + RUN_DIR_postfix

#444.namd
namd = Process() # Update June 7, 2017: This used to be LiveProcess()
namd.executable = 'namd' + x86_suffix
# TEST CMDS
#namd.cmd = [namd.executable] + ['--input', 'namd.input', '--output', 'namd.out', '--iterations', '1']
# REF CMDS
namd.cmd = [namd.executable] + ['--input', 'namd.input', '--output', 'namd.out', '--iterations', '38']
#namd.output = out_dir + 'namd.out'
namd.cwd = SPEC_PATH + RUN_DIR_prefix + "444.namd"

#445.gobmk
gobmk = Process() # Update June 7, 2017: This used to be LiveProcess()
gobmk.executable = 'gobmk' + x86_suffix
# TEST CMDS
#gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
#gobmk.input = 'dniwog.tst'
# REF CMDS
gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
gobmk.input = '13x13.tst'
#gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
#gobmk.input = 'nngs.tst'
#gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
#gobmk.input = 'score2.tst'
#gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
#gobmk.input = 'trevorc.tst'
#gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
#gobmk.input = 'trevord.tst'
#gobmk.output = out_dir + 'gobmk.out'
gobmk.cwd = SPEC_PATH + RUN_DIR_prefix + "445.gobmk" + RUN_DIR_postfix

#447.dealII
####### NOT WORKING #########
dealII = Process() # Update June 7, 2017: This used to be LiveProcess()
dealII.executable = 'dealII' + x86_suffix
# TEST CMDS
####### NOT WORKING #########
#dealII.cmd = [gobmk.executable]+['8']
# REF CMDS
####### NOT WORKING #########
#dealII.output = out_dir + 'dealII.out'
dealII.cwd = SPEC_PATH + RUN_DIR_prefix + "447.dealII" + RUN_DIR_postfix

#450.soplex
soplex = Process() # Update June 7, 2017: This used to be LiveProcess()
soplex.executable = 'soplex' + x86_suffix
# TEST CMDS
#soplex.cmd = [soplex.executable] + ['-m10000', 'test.mps']
# REF CMDS
soplex.cmd = [soplex.executable] + ['-m45000', 'pds-50.mps']
#soplex.cmd = [soplex.executable] + ['-m3500', 'ref.mps']
#soplex.output = out_dir + 'soplex.out'
soplex.cwd = SPEC_PATH + RUN_DIR_prefix + "450.soplex" + RUN_DIR_postfix

#453.povray
povray = Process() # Update June 7, 2017: This used to be LiveProcess()
povray.executable = 'povray' + x86_suffix
# TEST CMDS
#povray.cmd = [povray.executable] + ['SPEC-benchmark-test.ini']
# REF CMDS
povray.cmd = [povray.executable] + ['SPEC-benchmark-ref.ini']
#povray.output = out_dir + 'povray.out'
povray.cwd = SPEC_PATH + RUN_DIR_prefix + "453.povray" + RUN_DIR_postfix

#454.calculix
calculix = Process() # Update June 7, 2017: This used to be LiveProcess()
calculix.executable = 'calculix' + x86_suffix
# TEST CMDS
#calculix.cmd = [calculix.executable] + ['-i', 'beampic']
# REF CMDS
calculix.cmd = [calculix.executable] + ['-i', 'hyperviscoplastic']
#calculix.output = out_dir + 'calculix.out'
calculix.cwd = SPEC_PATH + RUN_DIR_prefix + "454.calculix" + RUN_DIR_postfix

#456.hmmer
hmmer = Process() # Update June 7, 2017: This used to be LiveProcess()
hmmer.executable = 'hmmer' + x86_suffix
# TEST CMDS
#hmmer.cmd = [hmmer.executable] + ['--fixed', '0', '--mean', '325', '--num', '45000', '--sd', '200', '--seed', '0', 'bombesin.hmm']
# REF CMDS
hmmer.cmd = [hmmer.executable] + ['nph3.hmm', 'swiss41']
#hmmer.cmd = [hmmer.executable] + ['--fixed', '0', '--mean', '500', '--num', '500000', '--sd', '350', '--seed', '0', 'retro.hmm']
#hmmer.output = out_dir + 'hmmer.out'
hmmer.cwd = SPEC_PATH + RUN_DIR_prefix + "456.hmmer" + RUN_DIR_postfix

#458.sjeng
sjeng = Process() # Update June 7, 2017: This used to be LiveProcess()
sjeng.executable = 'sjeng' + x86_suffix
# TEST CMDS
#sjeng.cmd = [sjeng.executable] + ['test.txt']
# REF CMDS
sjeng.cmd = [sjeng.executable] + ['ref.txt']
#sjeng.output = out_dir + 'sjeng.out'
sjeng.cwd = SPEC_PATH + RUN_DIR_prefix + '458.sjeng' + RUN_DIR_postfix 

#459.GemsFDTD
GemsFDTD = Process() # Update June 7, 2017: This used to be LiveProcess()
GemsFDTD.executable = 'GemsFDTD' + x86_suffix
# TEST CMDS
#GemsFDTD.cmd = [GemsFDTD.executable]
# REF CMDS
GemsFDTD.cmd = [GemsFDTD.executable]
#GemsFDTD.output = out_dir + 'GemsFDTD.out'
GemsFDTD.cwd = SPEC_PATH + RUN_DIR_prefix + "459.GemsFDTD" + RUN_DIR_postfix

#462.libquantum
libquantum = Process() # Update June 7, 2017: This used to be LiveProcess()
libquantum.executable = 'libquantum' + x86_suffix
# TEST CMDS
#libquantum.cmd = [libquantum.executable] + ['33','5']
# REF CMDS [UPDATE 10/2/2015]: Sparsh Mittal has pointed out the correct input for libquantum should be 1397 and 8, not 1297 and 8. Thanks!
libquantum.cmd = [libquantum.executable] + ['1397','8']
#libquantum.output = out_dir + 'libquantum.out'
libquantum.cwd = SPEC_PATH + RUN_DIR_prefix + "462.libquantum" + RUN_DIR_postfix

#464.h264ref
h264ref = Process() # Update June 7, 2017: This used to be LiveProcess()
h264ref.executable = 'h264ref' + x86_suffix
# TEST CMDS
#h264ref.cmd = [h264ref.executable] + ['-d', 'foreman_test_encoder_baseline.cfg']
# REF CMDS
h264ref.cmd = [h264ref.executable] + ['-d', 'foreman_ref_encoder_baseline.cfg']
#h264ref.cmd = [h264ref.executable] + ['-d', 'foreman_ref_encoder_main.cfg']
#h264ref.cmd = [h264ref.executable] + ['-d', 'sss_encoder_main.cfg']
#h264ref.output = out_dir + 'h264ref.out'
h264ref.cwd = SPEC_PATH + RUN_DIR_prefix + "464.h264ref" + RUN_DIR_postfix

#465.tonto
tonto = Process() # Update June 7, 2017: This used to be LiveProcess()
tonto.executable = 'tonto' + x86_suffix
# TEST CMDS
#tonto.cmd = [tonto.executable]
# REF CMDS
tonto.cmd = [tonto.executable]
#tonto.output = out_dir + 'tonto.out'
tonto.cwd = SPEC_PATH + RUN_DIR_prefix + "465.tonto" + RUN_DIR_postfix

#470.lbm
lbm = Process() # Update June 7, 2017: This used to be LiveProcess()
lbm.executable = 'lbm' + x86_suffix
# TEST CMDS
#lbm.cmd = [lbm.executable] + ['20', 'reference.dat', '0', '1', '100_100_130_cf_a.of']
# REF CMDS
lbm.cmd = [lbm.executable] + ['300', 'reference.dat', '0', '0', '100_100_130_ldc.of']
#lbm.output = out_dir + 'lbm.out'
lbm.cwd = SPEC_PATH + RUN_DIR_prefix + "470.lbm" + RUN_DIR_postfix

#471.omnetpp
omnetpp = Process() # Update June 7, 2017: This used to be LiveProcess()
omnetpp.executable = 'omnetpp' + x86_suffix
# TEST CMDS
#omnetpp.cmd = [omnetpp.executable] + ['omnetpp.ini']
# REF CMDS
omnetpp.cmd = [omnetpp.executable] + ['omnetpp.ini']
#omnetpp.output = out_dir + 'omnetpp.out'
omnetpp.cwd = SPEC_PATH + RUN_DIR_prefix + "471.omnetpp" + RUN_DIR_postfix

#473.astar
astar = Process() # Update June 7, 2017: This used to be LiveProcess()
astar.executable = 'astar' + x86_suffix
# TEST CMDS
#astar.cmd = [astar.executable] + ['lake.cfg']
# REF CMDS
astar.cmd = [astar.executable] + ['rivers.cfg']
#astar.output = out_dir + 'astar.out'
astar.cwd = SPEC_PATH + RUN_DIR_prefix + "473.astar" + RUN_DIR_postfix

#481.wrf
wrf = Process() # Update June 7, 2017: This used to be LiveProcess()
wrf.executable = 'wrf' + x86_suffix
# TEST CMDS
#wrf.cmd = [wrf.executable]
# REF CMDS
wrf.cmd = [wrf.executable]
#wrf.output = out_dir + 'wrf.out'
wrf.cwd = SPEC_PATH + RUN_DIR_prefix + "481.wrf" + RUN_DIR_postfix

#482.sphinx3
sphinx3 = Process() # Update June 7, 2017: This used to be LiveProcess()
sphinx3.executable = 'sphinx_livepretend' + x86_suffix
# TEST CMDS
#sphinx3.cmd = [sphinx3.executable] + ['ctlfile', '.', 'args.an4']
# REF CMDS
sphinx3.cmd = [sphinx3.executable] + ['ctlfile', '.', 'args.an4']
#sphinx3.output = out_dir + 'sphinx3.out'
sphinx3.cwd = SPEC_PATH + RUN_DIR_prefix + "482.sphinx3" + RUN_DIR_postfix

#483.xalancbmk
######## NOT WORKING ###########
xalancbmk = Process() # Update June 7, 2017: This used to be LiveProcess()
xalancbmk.executable = 'xalancbmk' + x86_suffix
# TEST CMDS
######## NOT WORKING ###########
#xalancbmk.cmd = [xalancbmk.executable] + ['-v','test.xml','xalanc.xsl']
# REF CMDS
######## NOT WORKING ###########
#xalancbmk.output = out_dir + 'xalancbmk.out'
xalancbmk.cwd = SPEC_PATH + RUN_DIR_prefix + "483.xalancbmk" + RUN_DIR_postfix

#998.specrand
specrand_i = Process() # Update June 7, 2017: This used to be LiveProcess()
specrand_i.executable = 'specrand' + x86_suffix
# TEST CMDS
#specrand_i.cmd = [specrand_i.executable] + ['324342', '24239']
# REF CMDS
specrand_i.cmd = [specrand_i.executable] + ['1255432124', '234923']
#specrand_i.output = out_dir + 'specrand_i.out'
specrand_i.cwd = SPEC_PATH + RUN_DIR_prefix + "998.specrand" + RUN_DIR_postfix

#999.specrand
specrand_f = Process() # Update June 7, 2017: This used to be LiveProcess()
specrand_f.executable = 'specrand' + x86_suffix
# TEST CMDS
#specrand_f.cmd = [specrand_f.executable] + ['324342', '24239']
# REF CMDS
specrand_f.cmd = [specrand_f.executable] + ['1255432124', '234923']
#specrand_f.output = out_dir + 'specrand_f.out'
specrand_f.cwd = SPEC_PATH + RUN_DIR_prefix + "999.specrand" + RUN_DIR_postfix
