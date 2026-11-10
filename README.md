# DocFGP Languages

[![PyPI version](https://img.shields.io/pypi/v/docfgp-languages)](https://pypi.org/project/docfgp-languages/)
[![PyPI downloads](https://img.shields.io/pepy/dt/docfgp-languages)](https://pepy.tech/projects/docfgp-languages)
[![CI](https://github.com/iamzices/docfgp-document-fingerprint-languages/actions/workflows/ci.yml/badge.svg)](https://github.com/iamzices/docfgp-document-fingerprint-languages/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/iamzices/docfgp-document-fingerprint-languages)](LICENSE)

DocFGP Languages provides the Tesseract models that let [DocFGP](https://github.com/iamzices/docfgp-document-fingerprint) OCR scanned documents in every script.

## Features

- English and every language written in a non-Latin script, from [tessdata_fast](https://github.com/tesseract-ocr/tessdata_fast)
- Models pinned to one upstream revision and verified with SHA-256
- Discovered by DocFGP automatically

## Requirements

- Python 3.11+

## Installation

```bash
pip install "docfgp[languages]"
```

## Usage

```python
from docfgp import FingerprintConfig, Fingerprinter

fingerprinter = Fingerprinter(FingerprintConfig(ocr_language="chi_sim"))
fingerprint = fingerprinter.fingerprint("scan.pdf")
```

| Script | `ocr_language` values |
| --- | --- |
| Arabic | `ara`, `fas`, `pus`, `snd`, `uig`, `urd` |
| Armenian | `hye` |
| Bengali | `asm`, `ben` |
| Canadian syllabics | `iku` |
| Cherokee | `chr` |
| Chinese | `chi_sim`, `chi_sim_vert`, `chi_tra`, `chi_tra_vert` |
| Cyrillic | `aze_cyrl`, `bel`, `bul`, `kaz`, `kir`, `mkd`, `mon`, `rus`, `srp`, `tat`, `tgk`, `ukr`, `uzb_cyrl` |
| Devanagari | `hin`, `mar`, `nep`, `san` |
| Ethiopic | `amh`, `tir` |
| Georgian | `kat`, `kat_old` |
| Greek | `ell`, `grc` |
| Gujarati | `guj` |
| Gurmukhi | `pan` |
| Hebrew | `heb`, `yid` |
| Japanese | `jpn`, `jpn_vert` |
| Kannada | `kan` |
| Khmer | `khm` |
| Korean | `kor`, `kor_vert` |
| Lao | `lao` |
| Latin | `eng` |
| Malayalam | `mal` |
| Myanmar | `mya` |
| Odia | `ori` |
| Sinhala | `sin` |
| Syriac | `syr` |
| Tamil | `tam` |
| Telugu | `tel` |
| Thaana | `div` |
| Thai | `tha` |
| Tibetan | `bod`, `dzo` |

Models combine with `+`, such as `eng+chi_sim`.
