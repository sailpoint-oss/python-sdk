const fs = require("fs");
const path = require("path");
const getAllFiles = function (dirPath, arrayOfFiles) {
  files = fs.readdirSync(dirPath);
  arrayOfFiles = arrayOfFiles || [];
  files.forEach(function (file) {
    if (fs.statSync(dirPath + "/" + file).isDirectory()) {
      arrayOfFiles = getAllFiles(dirPath + "/" + file, arrayOfFiles);
    } else {
      arrayOfFiles.push(path.join(__dirname.replaceAll('sdk-resources',''), dirPath, "/", file));
    }
  });
  return arrayOfFiles;
};


const fixFiles = function (myArray) {
  let fixCheck = 0;
  for (const file of myArray) {

    let fileOut = [];
    let madeChange = false;
    let rawdata = fs.readFileSync(file).toString();
    let rawDataArra = rawdata.split("\n");

    // fix syntax error in model_patch 
    if (file.includes("export_payload.py")) {
      for (const line of rawDataArra) {
        if (line.includes("from sailpoint.beta.models.dict[str,_object_export_import_options] import Dict[str, ObjectExportImportOptions]")) {
          fileOut.push(line.replaceAll("from sailpoint.beta.models.dict[str,_object_export_import_options] import Dict[str, ObjectExportImportOptions]", ""));
          madeChange = true;
        } else if (line.includes("from sailpoint.v2024.models.dict[str,_object_export_import_options] import Dict[str, ObjectExportImportOptions]")) {
          fileOut.push(line.replaceAll("from sailpoint.v2024.models.dict[str,_object_export_import_options] import Dict[str, ObjectExportImportOptions]", ""));
          madeChange = true;
        } else {
          fileOut.push(line);
        }
      }
      rawDataArra = fileOut.slice();
      fileOut = [];
    }
  
    if (madeChange) {
      fixCheck += 1;
      fs.writeFileSync(file, rawDataArra.join("\n"));
    }
  }
  console.log(`fixed ${fixCheck} files`)
}




let myArray = [];
getAllFiles(process.argv[2], myArray);

fixFiles(myArray)
