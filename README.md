<img align="right" src="https://miro.medium.com/max/700/1*aTuWWHnk0-FeyetCxyNCCg.png" alt="notion" width=25% height=25% />

# Notion Markdown Updater

automatically parse & upload markdown file from document at notion database by just a click.   
- Used Unofficial Python 3 client for Notion.so API v3, [notion-py](https://github.com/jamalex/notion-py)
- Check if there is any post ready for publish every interval you want, then parse the post into markdown & save it.
- After saving file, you can also automate deploying your blog by `git push` (On Working)

## Prepare
### on notion
add **Select** property to your notion database like example below. *One option* (**🚀Ready to Publish**) will be the trigger to publish and *one option* (**📰Published**) will be the result.   
<img align="left" src="./image/property-example.png" alt="property example" width=100% height=100% />   
<br/>

### on local
install `notion-py` to your python environment.
```shell
pip install notion
```

## Install & Quick Start
On `config.py`, edit the option text to your option that you set on [Prepare](#Prepare). You can use emoji.
```python
# post status str
publish_ready = "Your Option 1"
published = "Your Option 2"
```
Clone this repository to your local.   
```shell
$ git clone https://github.com/shinjawkwang/notion-markdown-updater.git
```
Install cron if not exist.
### Ubuntu
```shell
$ sudo apt-get install -y cron 
```
### CentOS **(Not tested)**
```shell
$ yum -y install cronie
```
Run `crontab -e` and set environment variable. **The variable name should be accurate!**
`DOCUMENTS_URL` is just link of the page you want to register; it should be kind of database.
```shell
$ crontab -e
NOTION_TOKEN=<YOUR_NOTION_TOKEN>
DOCUMENTS_URL=<URL_OF_THE_PLACE_WHERE_YOUR_DATABASE_IS>
```
Before saving, determine the intervals to monitor and register cron job. Below is the rule of interval.
```shell
# .---------------- minute (0 - 59)
# | .------------- hour (0 - 23)
# | | .---------- day of month (1 - 31) 
# | | | .------- month (1 - 12) OR jan,feb,mar,apr ... 
# | | | | .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat 
# | | | | | 
# * * * * * user-name command to be executed
# Example - every 10:05 and 10:45 on monday to friday:
45,5 10 * * 1-5 root /usr/bin/rdate -s time.bora.net && clock -w
```
This script makes computer run the python script every one minute.
```shell
# Without log output
* * * * * python3 /absolute/path/of/repo/notion-markdown-updater/notion_updater.py
# With log of output or error (Recommend)
* * * * * python3 /absolute/path/of/repo/notion-markdown-updater/notion_updater.py >> ~/.log/log_`date +\%Y-\%m-\%d`.log 2>&1
```
Restart cron service.
### Ubuntu
```shell
sudo service cron restart
```
### CentOS **(Not tested)**
```shell
sudo service crond restart
```
Done! Check out whether it is working.

## Auto deploy on your service
On `config.py`, set `auto_deploy` to `True`.
```python
# config.py
auto_deploy = True
```
On `deploy.sh` line 10, set your absolute path of directory where you want to push to github.
```shell
# navigate into the build output directory
cd /path/to/directory
```
If your blog service need build to deploy, add the script between `cd` and `git push`
```shell
cd /home/ubuntu/blog

# add your build script here, if build is necessary
npm run build
cd build

git init
...
```
The important thing is that you should add remote of github to the target directory.
```shell
git remote add origin "https or ssh"
```