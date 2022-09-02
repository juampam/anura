# CREATE TAG


# FUNCTIONS

CreateContent(){
	NAME=$1
	PROPS="class = \"container\"" # Obtener datos seg[un el nombre
	START="<$NAME $PROPS>"
	CON="$2"
	END="<$NAME/>"
	tag=$START$CON$END
	echo $tag >> bcontent
}
CreateContent $1 $2 
