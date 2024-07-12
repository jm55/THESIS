# VT Scraper

The notebooks under this subdirectory (`AV Type.ipynb` & `Family.ipynb`) were used to scrape data from VirusTotal to obtain malware type and family labels of the verified malicious samples of the dataset.

## `AV Type.ipynb`

This notebook scrapes for the malware type of a given list of malicious samples (via hashes) VirusTotal. The notebook produces a raw results from the various AV engines VT uses to designate the type of malware for a given sample. Parsing the outputs was done using `VirusTotal.ipynb` which parses the results into simplified labels (e.g., `trojan`, `adware`, `pua`, etc).

## `Family.ipynb`

This notebook scrapes for the family of the malicious samples (via hashes) using VirusTotal.