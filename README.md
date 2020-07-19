<img align="right" src="https://miro.medium.com/max/700/1*aTuWWHnk0-FeyetCxyNCCg.png" alt="notion" width=250 height=250 />

# notion-markdown-updater

automatically parse & upload markdown file from document at notion database by just a click.   
using [notion-py](https://github.com/jamalex/notion-py)

## Prepare
### on notion
add **Select** property to your notion database like example below. *One option* (**🚀Ready to Publish**) will be the trigger to publish and *one option* (**📰Published**) will be the result.   
<img align="left" src="./image/property-example.png" alt="property example" width=100% height=100% />   
<br/>

### on local
install `notion-py` to local.
```shell
pip install notion
```

## Install & Quick Start
1. clone this repository to your local.   
    ```shell
    $ git clone https://github.com/shinjawkwang/notion-markdown-updater.git`
    ```
2. make directory `/home/ubuntu/.notion` and move cloned repository to `/home/ubuntu/.notion`.
    ```shell
    $ mkdir /home/ubuntu/.notion
    $ mv notion-markdown-updater /home/ubuntu/.notion/notion-markdown-updater
    ```
    > any directory can be used, but it needs modify `ExecStart` on `notion.service` if any other directory.
3. fill `secret` with your personal information and move the file to `/home/ubuntu/.config/`
    ```shell
    $ mv secret /home/ubuntu/.config/secret
    ```
    > any directory can be used, but it needs modify `EnvironmentFile` on `notion.service` if any other directory.
