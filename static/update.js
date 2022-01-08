const modelViewerTransform = document.querySelector("model-viewer#transform");
const frame = document.querySelector('#frame');
var r = 0;
var p = 0;
var y = 0;
var resp = 0;
function setr(data) {
  r = data;
}
function setp(data) {
  p = data;
}
function sety(data) {
  y = data;
}

frame.addEventListener('click', () => {
  modelViewerTransform.updateFraming();
  setInterval(function() {
    fetch('/static/r.txt')
      .then(response => response.text())
      .then(data => setr(data));
    fetch('/static/p.txt')
      .then(response => response.text())
      .then(data => setp(data));
    fetch('/static/y.txt')
      .then(response => response.text())
      .then(data => sety(data));
      updateOrientation(r, p, y);
      modelViewerTransform.updateFraming();
      function readTextFile(file)
      {
        var rawFile = new XMLHttpRequest();
        rawFile.open("GET", "static/r.txt", false);
        rawFile.onreadystatechange = function ()
        {
          if(rawFile.readyState === 4)
          {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
              var allText = rawFile.responseText;
                resp = allText;
            }
          }
        }
        rawFile.send(null);
      }
      console.log(resp)
  }, 100);
});

const updateOrientation = (r, p, y) => {
  modelViewerTransform.orientation = (r+"deg "+p+"deg "+y+"deg");
};

