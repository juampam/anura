
# Anura      ![Commit Activity](https://img.shields.io/github/commit-activity/w/juampam/anura) ![Contributors](https://img.shields.io/github/contributors/juampam/anura) ![Licence](https://img.shields.io/github/license/juampam/anura) ![repo size](https://img.shields.io/github/repo-size/juampam/anura)

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
| `style`       | Manage css files          | `build` `get` `upload`            | `-name` `-colors` `-media` `class` 

## Build Style example
```
anura style build -name MyStyle -colors red,green,yellow,blue -media favicon.ico,background.svg
```
## Upload Style example
```
anura style upload MyStyle
```
## Get Style example
```
anura style get someuser/somestyle
```
--- 

### Need Fix:
- write options in any order

---
# Contribute 

contributions are welcome, join us

[<img src="https://img.shields.io/badge/Discord-7289DA?style=plastic&logo=discord&logoColor=indigo"/>](https://discord.com/channels/996898483401396384/996898483401396387)




