function shuffle() {
    var sourceElements = document.getElementById('shuffle_source').value.trim().split('\n');
    var resultNumber = parseInt(document.getElementById('result_number').value);
    resultNumber = resultNumber <= sourceElements.length ? resultNumber : sourceElements.length;
    
    fyShuffle(sourceElements)
    var resultElements = sourceElements.slice(0, resultNumber);
    
    var shuffleResult = document.getElementById('shuffle_result');
    shuffleResult.value = resultElements.join('\n');
}

function uploadCSV() {
    var csvFile = document.getElementById('upload_csv').files[0];
    var shuffleSource = document.getElementById('shuffle_source');

    if(csvFile) {
        var reader = new FileReader();
        reader.readAsText(csvFile, 'UTF-8');
        reader.onload = function(e) {
            shuffleSource.value = e.target.result;
        }
        reader.onerror = function(e) {
            alert('File Error!!!');
        }
    }
}

// Fisher-Yates Algorithm for shuffle array
function fyShuffle(array) {
    for(let i = array.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}