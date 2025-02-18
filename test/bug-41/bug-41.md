DLL load failed while importing _arcgisscripting #41

https://github.com/JamesRamm/archook/issues/41#issuecomment-2654165134

tried recipe from scratch in a Win11 VM, forgetting that Pro is not installed there so of course it will fail. However in the process I recalled that `arcgis.mapping` can be installed from conda and will install `arcpy` along with it. Could this be a way out? It doesn't solve the project's raison d'etre, combining Pro with non-Esri python projects, but arcgis.mapping didn't exist in 2015.

To do: add test to look for arcgis.mapping if Pro search fails.


### scrapbook

uv init
uv add arcgis.mapping
uv run python test-gh-41.py