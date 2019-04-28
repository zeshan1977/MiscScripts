function Pharmacy(name,location,numemployees){
    this.name=name;
    this.location=location;
    this.numemployees=numemployees;

    this.ToString = function () {
        console.log( "Class|Pharmacy:"+this.name +"|"+this.location +"|"+this.numemployees);
    }
}



var newPharmacy = new Pharmacy("munnawar Rx ","vaughn,ON L7AX43",45);
newPharmacy.ToString();




newCar.ToString();

function Car(name,make,model,country){
    this.car=name;
    this.make=make;
    this.model= model;
    this.country=country;
    this.ToString = function () {
        console.log( "Hi I am :"+this.car+"|"+this.make+"|"+this.model +"|"+this.country);
    }
}



var newCar = new Car ("toyota","Corolla","sedan","Japan");

newCar.ToString();
/*
mongodb is running at 
Spring.data.mongodb.uri=mongodb://zesham2: hammed4567@192.168.0.24:27017/din

db.din_activeIngredient.insertMany([{"dosage_unit":"","dosage_value":"","drug_code":48905,"ingredient_name":"VITAMIN A","strength":"1250","strength_unit":"UNIT"},
    {"dosage_unit":"","dosage_value":"","drug_code":48906,"ingredient_name":"VITAMIN C","strength":"125","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":48907,"ingredient_name":"CHROMIUM","strength":"0.5","strength_unit":"MCG"},
    {"dosage_unit":"","dosage_value":"","drug_code":48980,"ingredient_name":"MOLYBDENUM (MOLYBDENUM PROTEINATE)","strength":"2.5","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":48982,"ingredient_name":"MANGANESE (MANGANESE GLUCONATE)","strength":"1.25","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":489054,"ingredient_name":"VITAMIN B6","strength":"5","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":489055,"ingredient_name":"POTASSIUM (POTASSIUM CHLORIDE)","strength":"15","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":489056,"ingredient_name":"ZINC (ZINC GLUCONATE)","strength":"7.5","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":489057,"ingredient_name":"FOLIC ACID","strength":"0.2","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":489058,"ingredient_name":"VITAMIN B12","strength":"9","strength_unit":"MCG"},
    {"dosage_unit":"","dosage_value":"","drug_code":489059,"ingredient_name":"SELENIUM","strength":"100","strength_unit":"MCG"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890511,"ingredient_name":"IODINE (POTASSIUM IODIDE)","strength":"0.075","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890512,"ingredient_name":"NICOTINAMIDE","strength":"20","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890513,"ingredient_name":"D-PANTOTHENIC ACID","strength":"10","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890514,"ingredient_name":"CHOLINE","strength":"5","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890518,"ingredient_name":"INOSITOL","strength":"5","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890519,"ingredient_name":"BIOTIN","strength":"75","strength_unit":"MCG"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890562,"ingredient_name":"VITAMIN D2 (VITAMIN D2)","strength":"200","strength_unit":"UNIT"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890564,"ingredient_name":"VITAMIN B1","strength":"2.25","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890565,"ingredient_name":"VITAMIN B2","strength":"3.75","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890566,"ingredient_name":"BETA-CAROTENE (PROVITAMIN A)","strength":"2916","strength_unit":"UNIT"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890567,"ingredient_name":"COPPER (CUPRIC OXIDE)","strength":"1.5","strength_unit":"MG"},
    {"dosage_unit":"","dosage_value":"","drug_code":4890568,"ingredient_name":"VITAMIN E","strength":"200","strength_unit":"UNIT"}])
    */