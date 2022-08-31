# Anura, styles settings
## ORG

Work with separated configurations, using very classes, one for each characteristic.
example

```
.btn{ button settings }
.bg-sec{ secundary color as background }
.rounded{ rounded corners }
```
```
<a class = "btn bg-sec rounded" href="#">I am a Button</a>
```

### Position Settings

...

### Visual Settings

...

# Program Performance

## Create

Just create a new directory with the name asigned in the command line, inside the folder has two files (index.html, style.css).
The `index.html` file, is based in a file that contains html tags to be used like an objects.
The `style.css` file is based in a file that contains css classes. This file is created with the Build command.

## Projects control

The script is disigned to run in any directory, for this reason, the projects are created without modify permmissions. (you can disable this adding `-f` at the moment to create the project). For modify the projects need to be used the program, but, if the projects are not in the same directory when you run the command, how the program knows where is the project? For that exists a file that contains the information of each project (name,path,status). Status is the indicator of the life of the project, i mean, if it is alive yet. For this reason is recommendable dont use the free mode "-f", because if you delete the project using `rm -rf` or `rmdir` or any other way diferent to the `anura remove` command; this changed will not be reported to the project history file.

## Branches
(comming soon)
Every change must be recorded, for name the changes you can add `#NAME` to the end of the command, or automactly has been named like the hour exactly when the change was saved

