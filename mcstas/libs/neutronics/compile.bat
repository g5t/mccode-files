@REM Script for post-install compilation of libmcpl.a on Windows
@REM
cd /d %~dp0%
gfortran -c neutronics-subs.f
ar rcs libneutronics.a neutronics-subs.o
