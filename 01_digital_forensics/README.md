# Digital Forensics Investigations

This module contains digital forensic examination reports, evidence integrity validation materials, and supporting scripts developed as part of graduate cybersecurity laboratory work and forensic analysis training.

## Research Context

Digital forensics is a critical area of cybersecurity focused on the identification, preservation, analysis, and presentation of digital evidence. A sound forensic process ensures that evidence is handled in a manner that preserves integrity, supports reproducibility, and meets legal and investigative standards.

This module demonstrates practical experience in:
- forensic image verification,
- evidence integrity validation using cryptographic hashes,
- deleted file recovery,
- metadata extraction,
- cross-tool validation,
- and structured forensic reporting.

These investigations reflect the use of accepted forensic principles and industry-standard tools to examine storage media and recover relevant evidence without altering the source data.

## Module Overview

The materials in this folder document forensic examinations involving removable media, recovered files, and image metadata analysis. The work emphasizes both the **technical process** of examination and the **documentation discipline** required in professional digital investigations.

## Skills Demonstrated

- Forensic evidence preservation
- MD5 and SHA1 hash verification
- Read-only forensic image mounting
- Deleted file recovery from unallocated space
- EXIF metadata extraction and interpretation
- GPS and device metadata analysis
- Cross-tool validation of recovered evidence
- Professional forensic report writing

## Tools Used

| Tool | Purpose |
| :--- | :--- |
| FTK Imager | Image acquisition review and hash verification |
| Autopsy | Primary forensic analysis and metadata extraction |
| OSFMount | Read-only mounting of forensic images |
| Recuva | Secondary recovery validation and filename reconstruction |
| Python | Automation of evidence integrity verification |

## Files

| File | Description |
| :--- | :--- |
| `UNCC_Theft_Case_Report.pdf` | Digital forensic examination report involving a USB forensic image and recovery of deleted image evidence. |
| `Forensic_Image_Verification_Report.pdf` | Supporting forensic integrity or lab-based verification report. |
| `scripts/hash_validator.py` | Python utility for computing MD5 and SHA1 hashes to verify evidence integrity. |

## Case Highlights

The forensic investigation documented in this module included:
- validation of forensic image integrity using **MD5** and **SHA1** hashes,
- examination of a USB forensic image in **E01** format,
- recovery of deleted files from **Recycle Bin** and **unallocated space**,
- extraction of **EXIF metadata** from image files,
- identification of **camera make and model**,
- recovery of **GPS coordinates** associated with the images,
- and cross-validation of findings using multiple forensic tools.

The recovered evidence included images consistent with a university environment, including Apple hardware and other devices, with metadata indicating capture on an Apple iPhone 6s near UNC Charlotte campus locations.

## Investigation Workflow

1. Verify forensic image integrity using stored and computed hashes.
2. Mount or ingest the evidence in a controlled forensic environment.
3. Run metadata extraction and file carving processes.
4. Recover deleted content from allocated and unallocated areas.
5. Validate findings across multiple tools.
6. Document findings in a structured forensic report.

## Professional Relevance

This module reflects hands-on digital forensics capabilities relevant to:
- incident response,
- forensic examination support,
- evidence handling and validation,
- insider threat investigations,
- and law-enforcement or corporate investigative workflows.

It also demonstrates the ability to translate technical findings into formal documentation suitable for academic, investigative, and professional cybersecurity contexts.