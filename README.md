<img align="right" src="https://miro.medium.com/max/700/1*aTuWWHnk0-FeyetCxyNCCg.png" alt="notion" width=250 height=250 />

# notion-markdown-updater

automatically parse & upload markdown document from notion database by just a click.   
using [notion-py](https://github.com/jamalex/notion-py)

## Prepare on notion
add **Select** property to your notion database like example below. *One option* (**🚀Ready to Publish**) will be the trigger to publish and *one option* (**📰Published**) will be the result.   
<img align="left" src="./image/property-example.png" alt="property example" width=80% height=80% />
<br/>

## Install
1. clone this repository to your local.   
    ```shell
    $ git clone https://github.com/shinjawkwang/notion-markdown-updater.git`
    ```
2. make `/home/ubuntu/.notion' and move cloned repository to `/home/ubuntu/.notion`
    ```shell
    $ mkdir /home/ubuntu/.notion
    $ mv notion-markdown-updater /home/ubuntu/.notion/notion-markdown-updater
    ```
3. 
