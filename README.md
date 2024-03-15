# je-tool
json encode tool (je for short)

A simple dependency-free python script for generating json in bash

### Usage
```
je [-l|-d] [value1] [value2] ...

-l | --list or -a | --array for list mode 
-d | --dict or -o | --object for object mode

```
## Introduction
If you mess with tools like curl and salt via the command line, you've no doubt had to deal with wrangling input into acceptable json strings while also dealing with the complexity of bash literals.

No more.

Use je.

1. Install it to somewhere in your $PATH. These steps will work on most systems as root
    ```bash
    curl -o je https://raw.githubusercontent.com/jealouscloud/je-tool/main/je.py
    chmod 755 je # set 'executable' bit on the script
    mv je /usr/local/bin/ # as root
    ```
    If you are a user you may need to adopt to your system specific configuration by checking your $PATH and adding a directory if there is not one present
2. Use it
    ```bash
    root@server:~# je 1 2 3
    [1, 2, 3]
    root@server:~# je key=value keys=values
    {"key": "value", "keys": "values"}
    root@server:~# 
    ```
    Marshall into string:
    ```bash
    root@master:~# je version=1.0
    {"version": 1.0}
    root@master:~# je version=\"1.0\"
    {"version": "1.0"}
    ```

3. Chain it
    
    - Notes:
        * Nesting `"` marks to prevent line splitting in bash is surprisingly supported
        * jq is used to prettify output
    ```sh
    root@server:~# je config="$(je -d version=1.0 dependencies="$(je -l python json.decode)")" | jq
    {
    "config": {
        "version": 1,
        "dependencies": [
        "python",
        "json.decode"
        ]
    }
    }
    ```
4. Become wizard
    ```bash
    curl -d "$(je "$(je "$(je "$(je ...
    ```
    Be warned there is no turning back from this point.