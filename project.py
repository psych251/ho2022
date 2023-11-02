import fire
import zipfile
import os
import subprocess

def __run_cmd(cmd_list, cwd='.'):
    print(" ".join(cmd_list))
    process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, cwd=cwd)
    output, error = process.communicate()
    if output:
        print(output.decode("UTF-8"))
    if error:
        print(error)

files_to_zip = [
    # analyzed datafiles
    "experiments/exp1/data/navtrials.json",
    "experiments/exp1/data/participantdata.json",
    "experiments/exp1/data/attentiontrials.json",

    #config files
    "experiments/exp1/exp1.0-config.json",

    # gridsearch files
    "analyses/dvgc-gridsearch/results/gridsearch.json",
]

def zip_files():
    for dirfile in files_to_zip:
        dir, file = os.path.split(dirfile)
        with zipfile.ZipFile(dirfile+".zip", mode="w") as zipper:
            zipper.write(
                dirfile,
                arcname=file,
                compress_type=zipfile.ZIP_DEFLATED
            )
        print(f"Zipped {dirfile} to {dirfile+'.zip'}")

def unzip_files():
    for dirfile in files_to_zip:
        dir, file = os.path.split(dirfile)
        with zipfile.ZipFile(dirfile+".zip", "r") as unzipper:
            unzipper.extractall(dir)
        print(f"Unzipped {dirfile+'.zip'} to {dirfile}")

notebooks = [
    "exp-1.ipynb",
    # "exp-2.ipynb",
    # "exp-3.ipynb",
    # "exp-4.ipynb",
    # "exp-controls.ipynb",
    # "plot-grid-measure-figs.ipynb",
    # "plot-critical-mazes.ipynb",
    # "plot-pairwise-analyses.ipynb",
    # "plot-qbin-figure.ipynb",
    # "plot-global-lesion-tables.ipynb",
    # "dvgc-gridsearch.ipynb",
]
ANALYSIS_DIR = "./analyses"

def run_analysis_notebooks():
    for notebook in notebooks:
        notebook_path = os.path.join(ANALYSIS_DIR, notebook)
        toprint = f"Running {notebook_path}"
        print("="*len(toprint))
        print(toprint)
        print("="*len(toprint))

        __run_cmd(
            cmd_list=[
                "ipython",
                notebook,
            ],
            cwd=ANALYSIS_DIR
        )
        print("-------------------------------------------")
    print("SUCCESS")

if __name__ == "__main__":
    fire.Fire()
