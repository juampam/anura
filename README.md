<h1 align="center">
  <img src="https://github.com/juampam/anura-css/blob/master/program/styles/anura.png?sanitize=true" alt="Anura CSS - HTML + CSS Builder" width="75%">
</h1>

<div align="center">

![Commit Activity](https://img.shields.io/github/commit-activity/w/juampam/anura?style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/juampam/anura?style=for-the-badge)
![Licence](https://img.shields.io/github/license/juampam/anura?style=for-the-badge)
![repo size](https://img.shields.io/github/repo-size/juampam/anura?style=for-the-badge)

</div>     

# Structures
## General

	Project
	├── index.html
	|	└── Components 
	|		├── classes
	|		└── Identifiers
	└── style.css 	

## Style

	css file
	├── Identifiers
	└── classes

## Usage (Testing)
- create:

in the project diretory execute:
```
./anura.sh create ProjectName Stylename
```
Example using default css style
```
./anura.sh create MyProject
```
## Commands 

| Command       | description               | options                           | arguments  
| ------------- | ------------------------- | --------------------------------- |------------------------------------
| `create`      | create a new project      | `name` `style`                    
| `new`         | add new file in project   | `in` `--name`                     
| `add`         | Add a component in a file | `in` `--class` `--place` `--type` 
| `in`       	| select project, also can used like a command option           | `project name`  `name`   | `-f` `-p`
| `build`	| build diferent things	    | `colorscheme` `component` `style`	|

## Build Style example
```
./anura.sh build style
```
## Upload Style example
```
./anura.sh sharestyle MyStyle
```
## Get Style example
```
./anura.sh getstyle someuser/somestyle
```
--- 


---
# Contribute 

Together everything is better! Join us

[<img src="https://img.shields.io/badge/Discord-7289DA?style=flat&logo=discord&logoColor=white"/>](https://discord.gg/22XF2sGC)
[<img src="https://img.shields.io/badge/Telegram-2CA5E0?style=flat&logo=telegram&logoColor=white"/>](https://t.me/+axasghbryK9mMWIx)




