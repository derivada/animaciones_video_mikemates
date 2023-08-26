@echo off
setlocal enabledelayedexpansion

for %%f in (manim_*.py) do (
  set "filename=%%~nf"
  set "num=!filename:~7!"
  
  echo Running manim %%f -qh
  manim %%f -qh
)

endlocal