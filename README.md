# TCGA_data_download
Tutorial to download raw genetic data of TCGA dataset from GDC data portal (updated 16 March 2023)

### 1. Search for your files in your browser e.g. RNA-seq raw sequencing data of head and neck cancer of 521 cases and 1698 samples <br>
```
https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-HNSC%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22files.data_category%22%2C%22value%22%3A%5B%22sequencing%20reads%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22files.experimental_strategy%22%2C%22value%22%3A%5B%22RNA-Seq%22%5D%7D%7D%5D%7D&searchTableTab=files
```

<img width="1410" alt="image" src="https://user-images.githubusercontent.com/47389288/225690258-533310d5-7308-481b-9c41-488869729069.png">


### 2. Download manifest file, which contains UUID of all files

![image](https://user-images.githubusercontent.com/47389288/225690920-a75420f6-5ea6-4608-9250-06179ec98cbb.png)

### 3. Install GDC tool following https://gdc.cancer.gov/access-data/gdc-data-transfer-tool
### 4. Download all the files by GDC tool with single command
```
gdc-client download -m gdc_manifest_20230127_133037.txt
```

if your data is **controlled** , you need to get permission to dowload the token file, and submit the token file with the command
```
gdc-client download -m gdc_manifest_20230127_133037.txt -t gdc-user-token.2023-01-30T16_31_33.133Z.txt
```

**Optional** <br>
submit parallel job by slurm 
```
#!/bin/bash
#
# jobs options
#SBATCH -J "download"
#SBATCH -A "slurm_download"
#SBATCH -c 1
#SBATCH --mem=1GB
#SBATCH --output=dw-%j.out
#SBATCH --error=dw-%j.err
#SBATCH -p high_p
#SBATCH --ntasks=100
for id in `cut -f1 gdc_manifest.2023-02-06.txt|tail -n+2`
do
   srun -N1 -n1 -c1 --exact gdc-client download $id -t gdc-user-token.txt &
done
wait
```

When the download is complete, your files will be in the folder named by uuid linking to the id in gdc_manifest.2023-02-06.txt <br>
![image](https://user-images.githubusercontent.com/47389288/225696491-a2d8655b-2b8a-4164-a1af-65fdcdfe061a.png)

### 5. Download metadata file containig uuid of each file, TCGA case ID, file name, disease, experiment, etc. by using python script convert_uuid_to_TCGA.py <br>
you need to install pandas, requests, json packages in python, I prefer to install by anaconda
```
conda create -n gdc
conda activate gdc
conda install -c anaconda pandas
conda install -c anaconda requests
conda install -c jmcmurray json
```
then you should run convert_uuid_to_TCGA.py (dowload from https://github.com/asangphukieo/TCGA_data_download) by

```
python convert_uuid_to_TCGA.py gdc_manifest.2023-02-06.txt > data_TCGA.txt
```
the output will be in data_TCGA.txt as tab-delimited format
![image](https://user-images.githubusercontent.com/47389288/225698635-a877a4ef-5040-4ec1-8c07-23a676ac3c9d.png)


Done!!!



 
