window.onload = function() {







var chart = new CanvasJS.Chart("piechart-placeholder", {
	theme: "light2", // "light1", "light2", "dark1", "dark2"
	exportEnabled: true,
	animationEnabled: true,
	title: {
		text: "Labour Attendance"
	},
	data: [{
		type: "pie",
		startAngle: 25,
		toolTipContent: "<b>{label}</b>: {y}%",
		showInLegend: "true",
		legendText: "{label}",
		indexLabelFontSize: 16,
		indexLabel: "{label} - {y}%",
		dataPoints: [
			{ y: 26, label: "No of  Labour Present" },
			{ y: 13, label: "No of Labour Absent " },

		]
	}]
});



var chart1 = new CanvasJS.Chart("task-tab", {
	animationEnabled: true,
	title: {
		text: "Efficiency Rate of Machines"
	},
	axisX: {
		interval: 1
	},
	axisY: {
		title: "Efficiency in Percentage ",
		scaleBreaks: {
			type: "wavy",
			customBreaks: [{
				startValue: 80,
				endValue: 210
				},
				{
					startValue: 230,
					endValue: 600
				}
		]}
	},
	data: [{
		type: "bar",
		toolTipContent: "<img src=\"https://canvasjs.com/wp-content/uploads/images/gallery/javascript-column-bar-charts/\"{url}\"\" style=\"width:40px; height:20px;\"> <b>{label}</b><br>Efficieny:{y}% ",
		dataPoints: [
			{ label: "RF17", y: 88.1, url: "    " },
			{ label: "RF18", y: 50.5, gdp: 5.7, url: "" },
			{ label: "RF39", y: 67.9, gdp: 1.3, url: ""},
			{ label: "RF40", y: 73, gdp: 2.0, url: "" },
			{ label: "RF58", y: 48.4, gdp: 2.7, url: "" },
			{ label: "RF59", y: 87.6, gdp: 1.2, url: "" },
			{ label: "RF60", y: 57.3, gdp: 1.0, url: "" },
			{ label: "RF61", y: 60.6, gdp: 1.9, url: ""},
			{ label: "RF62", y: 77.1, gdp: 2.5, url: "" },
			{ label: "RF64", y: 43.5, gdp: 5.3, url: "" },
			{ label: "RF66", y: 84.6, gdp: 1.9, url: "" },
			{ label: "RF67", y: 57.2, gdp: 3.3, url: "" }
		]
	}]
});


var chart2 = new CanvasJS.Chart("prod", {
	animationEnabled: true,
	title: {
		text: "Efficiency Rate of Machines"
	},
	axisX: {
		interval: 1
	},
	axisY: {
		title: "Efficiency in Percentage ",
		scaleBreaks: {
			type: "wavy",
			customBreaks: [{
				startValue: 80,
				endValue: 210
				},
				{
					startValue: 230,
					endValue: 600
				}
		]}
	},
	data: [{
		type: "bar",
		toolTipContent: "<img src=\"https://canvasjs.com/wp-content/uploads/images/gallery/javascript-column-bar-charts/\"{url}\"\" style=\"width:40px; height:20px;\"> <b>{label}</b><br>Efficieny:{y}% ",
		dataPoints: [
			{ label: "RF17", y: 88.1, url: "    " },
			{ label: "RF18", y: 50.5, gdp: 5.7, url: "" },
			{ label: "RF39", y: 67.9, gdp: 1.3, url: ""},
			{ label: "RF40", y: 73, gdp: 2.0, url: "" },
			{ label: "RF58", y: 48.4, gdp: 2.7, url: "" },
			{ label: "RF59", y: 87.6, gdp: 1.2, url: "" },
			{ label: "RF60", y: 57.3, gdp: 1.0, url: "" },
			{ label: "RF61", y: 60.6, gdp: 1.9, url: ""},
			{ label: "RF62", y: 77.1, gdp: 2.5, url: "" },
			{ label: "RF64", y: 43.5, gdp: 5.3, url: "" },
			{ label: "RF66", y: 84.6, gdp: 1.9, url: "" },
			{ label: "RF67", y: 57.2, gdp: 3.3, url: "" }
		]
	}]
});




chart.render();
chart1.render();
chart2.render();




}








