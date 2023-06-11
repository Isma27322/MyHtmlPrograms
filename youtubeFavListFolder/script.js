var videoList = [];

function addVideo() {
	var link = document.getElementById("link").value;
	var name = document.getElementById("name").value;
	var video = {link: link, name: name};
	videoList.push(video);
	document.getElementById("videos").innerHTML += "<option value='" + link + "'>" + name + "</option>";
	document.getElementById("link").value = "";
	document.getElementById("name").value = "";
	saveVideos();
}

function playVideo() {
	var selectedLink = document.getElementById("videos").value;
	window.open(selectedLink, "_blank");
}

function saveVideos() {
	localStorage.setItem("videoList", JSON.stringify(videoList));
}

function loadVideos() {
	var storedVideos = localStorage.getItem("videoList");
	if (storedVideos) {
		videoList = JSON.parse(storedVideos);
		for (var i = 0; i < videoList.length; i++) {
			document.getElementById("videos").innerHTML += "<option value='" + videoList[i].link + "'>" + videoList[i].name + "</option>";
		}
	}
}
