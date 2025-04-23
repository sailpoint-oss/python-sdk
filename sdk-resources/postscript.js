const fs = require("fs").promises; // Use promises-based fs
const path = require("path");

const getAllFiles = async function (dirPath, arrayOfFiles) {
  const files = await fs.readdir(dirPath);
  arrayOfFiles = arrayOfFiles || [];
  for (const file of files) {
    const fullPath = path.join(dirPath, file);
    const stat = await fs.stat(fullPath);
    if (stat.isDirectory()) {
      arrayOfFiles = await getAllFiles(fullPath, arrayOfFiles);
    } else {
      arrayOfFiles.push(fullPath);
    }
  }
  return arrayOfFiles;
};

const renameFileToIndices = async (filePath) => {
  try {
    const newFilePath = path.join(path.dirname(filePath), "Indices.md");
    await fs.rename(filePath, newFilePath);
  } catch (error) {
    console.error(`Failed to rename file: ${error.message}`);
  }
};

const createDir = async (srcDir, dirName) => {
  const newDir = path.join(srcDir, dirName);
  try {
    await fs.mkdir(newDir, { recursive: true });
  } catch (err) {
    console.error(`Error creating directory: ${err.message}`);
  }
  return newDir;
};

const moveFiles = async (srcPath, destPath, filename = null) => {
  try {
    if (!await fs.stat(destPath)) {
      await fs.mkdir(destPath, { recursive: true });
    }

    if (filename) {
      const filePath = path.join(srcPath, filename);
      if (await fs.stat(filePath)) {
        await fs.rename(filePath, path.join(destPath, filename));
      } else {
        console.error(`File ${filename} does not exist in the source path.`);
      }
    } else {
      const files = await fs.readdir(srcPath);
      for (const file of files) {
        const filePath = path.join(srcPath, file);
        if ((await fs.stat(filePath)).isFile()) {
          await fs.rename(filePath, path.join(destPath, file));
        }
      }
    }
  } catch (error) {
    console.error(`Error moving files: ${error.message}`);
  }
};

const processDirectory = async (srcDir) => {
  const files = await fs.readdir(srcDir);
  const methodsDir = await createDir(srcDir, 'Methods');
  const modelsDir = await createDir(srcDir, 'Models');

  for (const file of files) {
    const currentPath = path.join(srcDir, file);
    const destMethodPath = path.join(methodsDir, file);
    const destModelPath = path.join(modelsDir, file);

    try {
      const stat = await fs.stat(currentPath);
      if (stat.isDirectory()) {
        if (file.includes('Api.md')) {
          await moveFiles(currentPath, methodsDir);
        } else if (file.includes('Methods')) {
          await moveFiles(currentPath, methodsDir);
        } else if (file.includes('Models')) {
          await moveFiles(currentPath, modelsDir);
        } else {
          await moveFiles(currentPath, currentPath); // default for directories
        }
      } else {
        if (file === 'python_code_examples_overlay.yaml') {
          continue; 
        }
      
        if (file.includes('Api.md')) {
          await fs.rename(currentPath, destMethodPath);
        } else {
          await fs.rename(currentPath, destModelPath); // default for files
        }
      }
    } catch (err) {
      console.error(`Error processing file: ${file}, ${err.message}`);
    }
  }
};

const fixFiles = async function (myArray) {
  let fixCheck = 0;
  for (const file of myArray) {
    let fileOut = [];
    let madeChange = false;
    const rawdata = await fs.readFile(file, 'utf-8');
    let rawDataArra = rawdata.split("\n");

    if (file.includes(".md")) {
      for (const line of rawDataArra) {
        if (line.includes("(list-error-message-dto)")) {
          fileOut.push(line.replace("(list-error-message-dto)", "(error-message-dto)"));
          madeChange = true;
        } else if (line.includes("(list-error-message-dto1)")) {
          fileOut.push(line.replace("(list-error-message-dto1)", "(error-message-dto)"));
          madeChange = true;
        } else if (line.includes("(list)")) {
          fileOut.push(line.replace("(list)", "(https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)"));
          madeChange = true;
        } else {
          fileOut.push(line);
        }
      }
      rawDataArra = fileOut.slice();
      fileOut = [];
    }

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
      await fs.writeFile(file, rawDataArra.join("\n"));
    }
  }
  console.log(`Fixed ${fixCheck} files`);
};

const main = async () => {
  let myArray = [];

  await processDirectory(path.join(process.argv[2], '/docs'));
  await renameFileToIndices(path.join(process.argv[2], '/docs/Models/Index.md'));
  await getAllFiles(process.argv[2], myArray);
  await fixFiles(myArray);
  await moveFiles(process.argv[2], path.join(process.argv[2], '/docs/Models'), "Index.md");
};

main().catch((error) => {
  console.error(`Error in script: ${error.message}`);
});
