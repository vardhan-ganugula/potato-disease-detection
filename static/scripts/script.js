const loader = document.getElementById('loader');
const result = document.getElementById('result');


loader.style.display = 'none';

async function handleSubmit(e) {
  e.preventDefault();
  loader.style.display = 'flex';
  const form = e.target;
  const url = "/predict";
  const formData = new FormData(form);


  if (!formData.has('image') || !formData.get('image').name) {
    result.innerHTML = '<p>Please upload an image file.</p>'
    loader.style.display = 'none';
    return;
  }

  try {
    const response = await fetch(url, {
        method: "POST",
        body: formData
    });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    console.log(json);
    result.innerHTML = `
      <h4>Prediction</h4>
      <p style="margin:10px;">output: ${json.prediction}</p>
    `;
  } catch (error) {
    console.error(error.message);
  }
  finally{
    loader.style.display = 'none';
  }
}


function handleFileChange(event){
  const file = event.target.files[0];
  const reader = new FileReader();
  const fileName = file.name;
  const fileArr = fileName.split('.');
  const fileExtension = fileArr[fileArr.length - 1].toLowerCase();
  if(fileExtension !== 'jpg' && fileExtension !== 'jpeg' && fileExtension !== 'png'){
    alert('Invalid file type. Please upload an image file.');
    return;
  }
  let modifiedFileName = fileName;
  if(fileArr[0].length > 10){
    modifiedFileName = fileArr[0].substring(0, 20) + '...' + fileExtension;
  }

  document.getElementById('file-name').innerText = modifiedFileName;
  reader.onload = function(e) {
    const image = document.getElementById("image-preview");
    image.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

