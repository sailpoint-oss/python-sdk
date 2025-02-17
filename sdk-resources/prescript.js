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

  
    // remove the complex transform schema
    if (file.includes(path.join("schemas","Transform.yaml"))) {
      for (let line of rawDataArra) {
        if (line.includes('oneOf')) {
          line = line.replaceAll("oneOf:", "type: object")
          madeChange = true;
        }
        if (line.includes('- $ref:')) {
          
        } else {
          fileOut.push(line);
        }
        
      }
      rawDataArra = fileOut.slice();
      fileOut = [];
    }

    // remove the complex account schema
    if (file.includes(path.join("paths","accounts.yaml"))) {
      
      for (let line of rawDataArra) {
        if (line.includes('oneOf')) {
          line = line.replaceAll("oneOf:", "$ref: '../schemas/SlimAccount.yaml'")
          madeChange = true;
        }
        if (line.includes("- $ref: '../schemas/SlimAccount.yaml'") || line.includes("- $ref: '../schemas/FullAccount.yaml'")) {
          
        } else {
          fileOut.push(line);
        }
        
      }
      rawDataArra = fileOut.slice();
      fileOut = [];
    }

    // remove the complex search schema
    if (file.includes(path.join("documents", "SearchDocument.yaml"))) {
          fileOut.push("type: object");
          rawDataArra = fileOut.slice();
          fileOut = [];
          madeChange = true;
    }
  
    // remove the complex search schema
    if (file.includes(path.join("documents", "SearchDocuments.yaml"))) {
      fileOut.push("type: object");
      rawDataArra = fileOut.slice();
      fileOut = [];
      madeChange = true;
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