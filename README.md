# Replication of People Construct Simplified Mental Representations to Plan

<p align="center" style="font-size: smaller">
  <img width="65%" src="https://github.com/psych251/ho2022/assets/51468707/257ed673-e6dc-4538-bc0f-d6955184123b"></img><br/>
  From <a href="https://socialsciences.nature.com/posts/people-construct-simplified-mental-representations-to-plan">Behind the Paper: People construct simplified mental representations to plan</a>
</p>
  

Replication project of initial experiment from Ho, M. K., Abel, D., Correa, C. G., Littman, M. L., Cohen, J. D., & Griffiths, T. L. (2022). *People construct simplified mental representations to plan.* Nature, 606(7912), 129-136.

RPubs link to report: [https://rpubs.com/justintheyang/wu2021replication](https://rpubs.com/justintheyang/ho2022_replication) <br>
Link to original paper: [Ho et al. - 2022 - People construct simplified mental representations.pdf](https://github.com/psych251/ho2022/blob/main/original_paper/Ho%20et%20al.%20-%202022%20-%20People%20construct%20simplified%20mental%20representations.pdf)

## Project directory
- `analyses`: contains notebooks and files to analyse data
- `experiments`: contains configuration files and processed datasets 
- `experiment.psiturkapp`: contains the experiment application code, used to host the experiment on Heroku
- `vgc_project`: a custom python package implementing value guided construal. Should be installed in the base directory in a virtual environment via `pip install -e ./vgc_project`
- `original_paper`: contains the original study
- `writeup`: contains the replication report

## Experiment
### Local server setup
You can run the study as a psiturk experiment by running:
```
$ cd experiment.psiturkapp
$ make dev
```

Doing so will start the server. The experiment can then be accessed locally [here](http://localhost:22362/testexperiment?CONFIG_FILE=exp1.0-config.json.zip).

### Heroku server setup
The Heroku setup consists of the following steps: 
```
$ heroku create ho2022replication --buildpack heroku/python
$ heroku git:remote -a ho2022replication
$ heroku addons:create heroku-postgresql
$ git subtree push --prefix experiment.psiturkapp heroku main
$ heroku config:set ON_CLOUD=1
```

The Postgres database url can be found by querying: 
```
heroku config
```

After the server is set up (check the server url with `heroku domains`), you may host the experiment on Prolific using the following URL parameters: 
``` 
https://project_name.herokuapp.com/exp?CONFIG_FILE=exp1.0-config.json.zip&assignmentId={{%SESSION_ID%}}&hitId={{%STUDY_ID%}}&workerId={{%PROLIFIC_PID%}}&mode=live
```


## Analyses

To process & get data, run the following sequence of commands in the project directory (`ho2022/`) using the `jupyter_notebook` conda environment: 

on `(jupyter_notebook) justyang:ho2022/ (main✗) $`: 
1. `python project.py unzip_files`
2. `python experiments/exp1/pull_results.py pull_data_from_server --EXP_NAME=pilot_a --RAWRESULTS_DIR=data/pilot_a --CREDENTIALS_FILE=.creds.json`
3. `python experiments/exp1/pull_results.py parse_raw_datafiles --BASEGRIDS_FILENAME=experiments/mazes/mazes_0-11.json --RAWRESULTS_DIR=data/pilot_a --EXP_CONFIG_FILE=experiment.psiturkapp/static/config/exp1.0-config.json --EXP_RESULTS_DIR=experiments/exp1/data/pilot_a/`
4. `python experiments/exp1/prep_results.py do_exclusions --BASEGRIDS_FILENAME=experiments/mazes/mazes_0-11.json --RESULTSDIR=experiments/exp1/data/pilot_a/`
