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

const mergeCodeExampleFiles = async (srcDir) => {
  try {
    // Check if the source directory exists asynchronously
    await fs.access(srcDir);

    const destFile = path.join(srcDir, 'python_code_examples_overlay.yaml');
    const files = await fs.readdir(srcDir);

    // Use writeFile instead of createWriteStream to simplify handling in async/await context
    let allContent = '';

    for (const file of files) {
      const filePath = path.join(srcDir, file);
      const stat = await fs.stat(filePath);

      if (stat.isFile()) {
        const fileContent = await fs.readFile(filePath, 'utf8');
        allContent += fileContent;  // Concatenate file contents
        await fs.unlink(filePath);  // Delete the original file after merging
      }
    }

    // Write all content into the destination file
    await fs.writeFile(destFile, allContent);

    console.log(`All files have been merged into ${destFile}`);
  } catch (error) {
    console.error(`Error processing the directory: ${error.message}`);
  }
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
  const examplesDir = await createDir(srcDir, 'Examples');
  const methodsDir = await createDir(srcDir, 'Methods');
  const modelsDir = await createDir(srcDir, 'Models');

  for (const file of files) {
    const currentPath = path.join(srcDir, file);
    const destExamplePath = path.join(examplesDir, file);
    const destMethodPath = path.join(methodsDir, file);
    const destModelPath = path.join(modelsDir, file);

    try {
      const stat = await fs.stat(currentPath);
      if (stat.isDirectory()) {
        if (file.includes('developerSite_code_examples')) {
          await moveFiles(currentPath, examplesDir);
        } else if (file.includes('Api.md')) {
          await moveFiles(currentPath, methodsDir);
        } else if (file.includes('index.md') || file.includes('Methods') || file.includes('Models')) {
          if (file.includes('Methods')) {
            await moveFiles(currentPath, methodsDir);
          } else {
            await moveFiles(currentPath, modelsDir);
          }
        } else {
          await moveFiles(currentPath, modelsDir);
        }
      } else {
        if (file.includes('developerSite_code_examples')) {
          await fs.rename(currentPath, destExamplePath);
        } else if (file.includes('Api.md')) {
          await fs.rename(currentPath, destMethodPath);
        } else {
          await fs.rename(currentPath, destModelPath);
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
  await mergeCodeExampleFiles(path.join(process.argv[2], 'docs/Examples'));
};

main().catch((error) => {
  console.error(`Error in script: ${error.message}`);
});
