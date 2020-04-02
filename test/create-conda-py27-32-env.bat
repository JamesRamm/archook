set CONDA_FORCE_32BIT=1
call conda create -n archook-py27-32 python=2.7
call conda activate archook-py27-32
call conda install numpy
@echo. --------------------------------
@echo. Next step: 
@echo. 
@echo.   Test archook
@echo.
