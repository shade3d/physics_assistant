//---------------------------------------------------------.
// 外部のテキストファイルを読み込んで、テキストを返す関数.
//---------------------------------------------------------.

// ブラウザがIEか判定.
function checkBrowserIE() {
	var userAgent  = window.navigator.userAgent.toLowerCase();

	if (userAgent.indexOf('msie') != -1) {
		return true;
	} else if (userAgent.indexOf('trident/7') != -1) {
		return true;
	}
	return false;
}

// 外部のテキストファイルを読み込み.
function readFileToString(fileName) {
	// ファイル読み込み用.
	var xmlHttp;
	if (checkBrowserIE()) {
		xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
	} else if (window.XMLHttpRequest) {
		xmlHttp = new XMLHttpRequest();
	} else {
		xmlHttp = null;
	}
	if (xmlHttp == null) return "";

	var str = "";
	try {
		xmlHttp.open("GET", fileName, false);
		xmlHttp.send(null);
		str = xmlHttp.responseText;
	} catch(e) {
		window.alert(e);
	}
	return str;
}
