# printer2D

A python script to intercept and work with clawPDF print jobs.

## Architecture

We are using clawPDF to capture print jobs as PDFs, then using `PDFtoPrinter.exe` to route them to physical printers. This is a common pattern for print job manipulation.

## Note

* `PDFtoPrinter.exe` file:
   * It is downloaded from [here](https://mendelson.org/pdftoprinter.html)
   * It is placed next to the run script
   * Its size is around 11 MB
* [clawPDF](https://github.com/clawsoftware/clawPDF) printer:
   * It has to be installed on the system
* Python version:
   * `3.12.3` is preferred to have a smooth PIP package installation process
* Microsoft Visual C++ Redistributables:
   * The x86 redistributable is needed even on x64 Windows
