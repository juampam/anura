<h1 align="center">
  <img src="https://github.com/juampam/anura-css/blob/master/program/Example/img/anura.png?sanitize=true" alt="Anura CSS - HTML + CSS Builder" width="75%">
</h1>

<div align="center">

![Commit Activity](https://img.shields.io/github/commit-activity/w/juampam/anura?style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/juampam/anura?style=for-the-badge)
![Licence](https://img.shields.io/github/license/juampam/anura?style=for-the-badge)
![repo size](https://img.shields.io/github/repo-size/juampam/anura?style=for-the-badge)

</div>     

## For now
- We can create a directory with a html index file and a css style file.
- The name of the directory is the title of the page
- the style is taked of the styles directory, is just a copy
## To do
- command to generate, publicate and save styles in the respective directory
- add differents components to the html file
- Download and upload styles to the page

## Usage (Testing)
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
anura build style
```
## Upload Style example
```
anura sharestyle MyStyle
```
## Get Style example
```
anura getstyle someuser/somestyle
```
--- 

### Need Fix:
- write options in any order

---
# Contribute 

Together everything is better! Join us

[<img src="https://img.shields.io/badge/Discord-7289DA?style=flat&logo=discord&logoColor=white"/>](https://discord.gg/22XF2sGC)
[<img src="https://img.shields.io/badge/Telegram-2CA5E0?style=flat&logo=telegram&logoColor=white"/>](https://t.me/+axasghbryK9mMWIx)




