::These parameters are specific to computer

::Store current Directory:
set currDir=%CD%

::get folder name as variable
SET "MYDIR=%~p0"
set MYDIR1=%MYDIR:~0,-1%
for %%f in (%MYDIR1%) do set myfolder=%%~nxf

:: Set openMVS directory
set oMVS=C:\Users\Peter\Downloads\openMVS_sample-0.7a

:: Set openMVG directory:
set oMVG=C:\Users\Peter\Downloads\OpenMVG_v1.3

:: Set Working Directory (windows)
set workDir=D:\%myfolder%\

mkdir %workDir% 
copy *.jpg %workDir%\ 
cd /d %workDir%

echo "start %time%">>timings.txt
%oMVG%\openMVG_main_SfMInit_ImageListing -i . -d %oMVG%\sensor_width_database\sensor_width_camera_database.txt -o matches
echo "imagelisting %time%" >> timings.txt
%oMVG%\openMVG_main_ComputeFeatures -p HIGH -i matches\sfm_data.json -o matches
echo "features %time%" >> timings.txt
%oMVG%\openMVG_main_ComputeMatches -r .8 -i matches\sfm_data.json -o matches
echo "matches %time%" >> timings.txt
%oMVG%\openMVG_main_IncrementalSfM -i matches\sfm_data.json -m matches -o out_Incremental_Reconstruction
echo "SfM done %time%" >> timings.txt
mkdir mvs_dir
%oMVG%\openMVG_main_ComputeStructureFromKnownPoses -i out_Incremental_Reconstruction\sfm_data.bin -m matches -f matches\matches.f.bin -o :: out_Incremental_Reconstruction\robust.bin
echo "structure %time%" >> timings.txt
%oMVG%\openMVG_main_ComputeSfM_DataColor.exe -i out_Incremental_Reconstruction\robust_colorized.ply
echo "color %time%" >> timings.txt
%oMVG%\openMVG_main_openMVG2openMVS -i out_Incremental_Reconstruction\sfm_data.bin -o mvs_dir\model.mvs -d mvs_dir
echo "convert to mvs %time%" >> timings.txt
%oMVS%\DensifyPointCloud.exe -i mvs_dir\model.mvs
echo "densifydone %time%">>timings.txt
%oMVS%\ReconstructMesh.exe mvs_dir\model_dense.mvs
echo "reconstructmesh done %time%">>timings.txt
%oMVS%\RefineMesh.exe --resolution-level 2 mvs_dir\model_dense_mesh.mvs
echo "refine done %time%">>timings.txt
%oMVS%\TextureMesh.exe mvs_dir\model_dense_mesh_refine.mvs
echo "all done %time%">>timings.txt