# Anura
## For now
- We can create a directory with a html index file and a css style file.
- The name of the directory is the title of the page
- the style is taked of the styles directory, is just a copy
## To do
- command to generate, publicate and save styles in the respective directory
- add differents components to the html file
- Download and upload styles to the page

## Usage
- create:

in the project diretory execute:
```
./anura create ProjectName Stylename
```
Example using default css style
```
./anura create MyProject
```
## Commands 

| Command       | description               | options                           | arguments  
| ------------- | ------------------------- | --------------------------------- |----------|
| `create`      | create a new project      | `name` `style`                    |
| `new`         | add new file in project   | `in` `--name`                     |
| `add`         | Add a component in a file | `in` `--class` `--place` `--type` |
| `style`       | Manage css files          | `build` `get` `upload`            | `name` `colors` `images` 

## Build Style example
```
anura style build MyStyle red,green,yellow,blue favicon.ico,background.svg
```
## Upload Style example
```
anura style upload MyStyle
```
## Get Style example
```
anura style get someuser/somestyle
```
### Need Fix:
- write options in any order
