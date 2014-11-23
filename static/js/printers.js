var nav_bar_offset = 50;
var image_base_width = 1348;
var image_base_height = 856;

var icon_width = 32;
var icon_height = 32;

var Printer = function (id, printerName, x, y) {
	this.id = id;
	this.name = printerName;
	this.x = x;
	this.y = y;
}
var printer_info = undefined;
$.getJSON("/index/printers/", function( data ) {
  	printer_info = data;
  	addPopovers();
});
var printers = [
	
	//Condense
	// Hunt, Wean, Hammerschlag, INIHS
	// Spread out
	// Gates, Baker, CFA
	new Printer("Baker1B&W", "Baker 1", 777, 685),
	new Printer("Baker2B&W", "Baker 2", 807, 685),
	new Printer("CFAB&W", "CFA Black & White", 956, 559),
	new Printer("CFAColor", "CFA Color", 965, 600),
	new Printer("CyertB&W", "Cyert", 726, 369),
	new Printer("DohertyB&W", "Doherty", 785, 570),
	new Printer("DonnerB&W", "Donner", 1145, 407),
	new Printer("GatesHall3B&W", "Gates 3", 728, 473),
	new Printer("GatesHall5B&W", "Gates 5", 731, 505),
	new Printer("Hammerschlag", "Hammerschlag Building", 637,689),
	/*new Printer("ECE1B&W", "Hammerschlag 1", 629, 666),
	new Printer("ECE2B&W", "Hammerschlag 2", 637, 689),
	new Printer("ECE3B&W", "Hammerschlag 3", 631, 676),
	new Printer("ECE4B&W", "Hammerschlag 4", 613, 678),*/
	new Printer("TheHillB&W", "Hill Residence", 1225, 339),
	new Printer("Hunt", "Hunt Library", 932, 650),
	//new Printer("HuntB&W", "Hunt 1", 913, 646),
	//new Printer("Hunt1Ref2B&W", "Hunt 2", 928, 639),
	//new Printer("Hunt1Ref4B&W", "Hunt 3", 941, 635),
	//new Printer("Hunt2B&W", "Hunt 4", 916, 660),
	//new Printer("Hunt3B&W", "Hunt 5", 935, 653),
	//new Printer("Hunt4ArtsB&W", "Hunt Arts B&W", 950, 647),
	//new Printer("Hunt4ArtsColor", "Hunt Arts Color", 950, 647),
	//new Printer("Hunt4MusicB&W", "Hunt Music", 950, 647),
	new Printer("MellonB&W", "Mellon Institute 1", 150, 500),
	new Printer("MellonColor", "Mellon Institute 2", 175, 525),
	new Printer("MorewoodB&W", "Morewood", 702, 234),
	new Printer("MudgeB&W", "Mudge", 636, 76),
	new Printer("PosnerB&W", "Posner", 1026, 604),
	new Printer("Res5B&W", "Residence on 5th", 394, 278),
	new Printer("UC2B&W", "UC", 906, 366),
	new Printer("INIHS", "UTDC", 283, 450),
	/*new Printer("INIHS1B&W", "UTDC 1", 278, 440),
	new Printer("INIHS2B&W", "UTDC 2", 283, 450),
	new Printer("INIHSBB&W", "UTDC 3", 288, 455),*/
	new Printer("WeanB&W", "Wean 1", 690, 600),
	new Printer("WeanColor", "Wean 2", 715, 590),
	new Printer("Sorrels", "Sorrels Library", 668, 610),
	//new Printer("Sorrels1B&W", "Sorrels 1", 652, 618),
	//new Printer("Sorrels2B&W", "Sorrels 2", 663, 612),
	//new Printer("Sorrels3Color", "Sorrels 3", 663, 612),
	new Printer("WestWingB&W", "West Wing", 1040, 366)
];

var map = document.getElementById('map');
window.onresize = updatePrinterIconHeights;
window.onload = updatePrinterIconHeights;

addPrintersIcons();

function updatePrinterIconHeights() {
	for (var i = printers.length - 1; i >= 0; i--) {
		var icon = document.getElementById(get_icon_id(printers[i].id));

		icon.style.top = Math.round((map.clientHeight/image_base_height) * (printers[i].y - (icon_height/2) + nav_bar_offset)) + "px";
	};
}
function get_icon_id(id) {
	return id.replace(/&/g,"") + "_icon";
}
function get_icon(printer_id) {
	var printer_list = [];
	var good = true;
	switch(printer_id) {
		//Groups are special
		case "Hammerschlag":
			printer_list = ["ECE1B&W", "ECE2B&W", "ECE3B&W", "ECE4B&W"];
			good = false;
			break;
		case "Hunt":
			good = false;
			printer_list = ["HuntB&W", "Hunt1Ref2B&W", "Hunt2B&W", "Hunt3B&W", "Hunt4ArtsB&W", "Hunt4ArtsColor", "Hunt4MusicB&W"];
			break;
		case "INIHS":
			good = false;
			printer_list = ["Sorrells1B&W", "Sorrells2B&W", "Sorrells3Color"];
			break;
		case "Sorrels":
			good = false;
			printer_list = ["Sorrells1B&W", "Sorrells2B&W", "Sorrells3Color"];
			break;
		default: 
			if(printer_info[printer_id].icon == "not working") {
				good = false;
			}
			break;
	}
	for(var i = printer_list.length - 1; i >= 0; i--) {
		if(printer_info[printer_id].icon != "not working") {
			good = true;
		}			
	}
	if(good) return "/static/images/good.png";
	return "/static/images/bad.png";

}
function addPrintersIcons() {

	var printer_div = document.getElementById("printer_container");

	for (var i = printers.length - 1; i >= 0; i--) {
		var icon = document.createElement("img");
		icon.setAttribute("class", "printer");
		icon.setAttribute("id", get_icon_id(printers[i].id));
		icon.setAttribute("src", get_icon(printer_id));
		icon.setAttribute("data-toggle", "popover");
		icon.setAttribute("data-trigger", "focus");
		icon.setAttribute("tabindex", i + "");
		icon.style.left = Math.round((100 * (printers[i].x - (icon_width/2))/image_base_width)) + "%";
		printer_div.appendChild(icon);
	};
	updatePrinterIconHeights();
}
function getPopoverContent(id) {
	switch(id) {
		//Groups are special
		case "Hammerschlag":
			return printerGroupData(["ECE1B&W", "ECE2B&W", "ECE3B&W", "ECE4B&W"]);
		case "Hunt":
			return printerGroupData(["HuntB&W", "Hunt1Ref2B&W", "Hunt2B&W", "Hunt3B&W", "Hunt4ArtsB&W", "Hunt4ArtsColor", "Hunt4MusicB&W"]);
		case "INIHS":
			return printerGroupData(["Sorrells1B&W", "Sorrells2B&W", "Sorrells3Color"]);
		case "Sorrels":
			return printerGroupData(["Sorrells1B&W", "Sorrells2B&W", "Sorrells3Color"]);
		default: 
			return printerData(id);
	}
}
function printerGroupData(list) {
	var str = "";
	for (var i = list.length - 1; i >= 0; i--) {
		str += "<strong>";
		str += printer_info[list[i]].fullName;
		str += "</strong></br>";
		str += printer_info[list[i]].icon;

		if(printer_info[list[i]].error != "")
		{
			str += " (";
			str += printer_info[list[i]].error;
			str += ")";
		}
		str += "</br></br>";
	}
	return str;
}
function printerData(id) {
	if (printer_info === undefined) return "Dataload Failure";
	var str = "";
	str += "<strong>";
	str += printer_info[id].icon;
	str += "</strong> </br>";
	str += printer_info[id].error;

	return str;

}
function popoverPlacement(id) {
	switch(id) {
		case "MudgeB&W":
			return "bottom";
		default:
			return "top";
	}
}
function addPopovers() {
	for (var i = printers.length - 1; i >= 0; i--) {
		var icon = $("#" + get_icon_id(printers[i].id));
		icon.popover({
			trigger: 'focus',
			html: true,
			placement: popoverPlacement(printers[i].id),
			title: printers[i].name,
			content: getPopoverContent(printers[i].id)
		});
	}
}
function update() {

}